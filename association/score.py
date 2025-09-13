#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:38:47 2025

@author: joshuaweston
"""

def get_score_metrics(df,metric,method):
    
    from lestrade.association.base_assoc import base_ang_sep
    
    #angsep host1-host2
    df[f"{metric} Host 1-2 Sep"] = df.apply(
                                        lambda row: base_ang_sep(
                                            row[f"{metric} Host 1 RA"], row[f"{metric} Host 1 DEC"],
                                            row[f"{metric} Host 2 RA"], row[f"{metric} Host 2 DEC"]
                                        ),
                                        axis=1
                                    )
    
    #metric ratio
    df[f'{metric} Ratio'] = df[f'{metric} Host 1 {metric}'] / df[f'{metric} Host 2 {metric}']
    
    #metric difference
    df[f'{metric} Difference'] = df[f'{metric} Host 1 {metric}'] - df[f'{metric} Host 2 {metric}']
    
    method_features = method.features
    
    df  = method_features(df)
    
    return df

class ls_model:
    
    def __init__(self,df,metric):
        
        import pandas as pd
        from sklearn.model_selection import GridSearchCV
        
        #extract figures
        
        # Exclusion keywords
        exclude = [" A", " B", " PA", " RA", " DEC", "MATCH", "GalID", "Label", " z", "Overwritten"]

        # Select columns that start with the metric and do not contain any exclude keyword
        self._allfeatures = [
            col for col in df.columns
            if col.startswith(metric) and not any(ex in col for ex in exclude)
        ]
        
        self._metric = metric
        
        self._output= df
        
        self._df = df[self._allfeatures]
        
        self._df['target'] = (df[f'{metric} MATCH'] == 'YES').astype(int)
        
    
    def feature_selection(self,features=None):
        
        import pandas as pd
        
        if features:
            
            self._features  = features
            
        else:
            
            self._features = self._allfeatures
            
        self._X = self._df[self._features].copy()
        
        self._X.fillna(0, inplace=True)
        
        self._y = self._df['target'].copy()
        
    def train_test_split(self,fraction=0.2,seed=42,dosmote=False):
        
        from sklearn.model_selection import train_test_split
        
        # Train-test split (80% training, 20% testing)
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=fraction, random_state=seed)

        if dosmote:
            
            from imblearn.over_sampling import SMOTE

            
            smote = SMOTE(random_state=seed)
            self._X_train, self._y_train = smote.fit_resample(self._X_train, self._y_train)
            
    def train_xgb(self,obj="binary:logistic",seed=42):
        
        import xgboost as xgb
        import pandas as pd
        import numpy as np
                
        # Replace inf with NaN in X
        X_clean = self._X_train.replace([np.inf, -np.inf], np.nan)
        
        # Build a mask of rows with no NaNs
        mask = X_clean.notna().all(axis=1)
        
        # Apply the mask to both X and y
        self._X_train = X_clean.loc[mask]
        self._y_train = self._y_train.loc[mask]


        self._model = xgb.XGBClassifier(objective=obj, random_state=seed)
        self._model.fit(self._X_train, self._y_train)
        
        # Get feature importances
        self._feature_importance = pd.Series(self._model.feature_importances_, index=self._X_train.columns)

        # Predict the probabilities for the test set (probability of target = 1)
        self._y_pred_prob = self._model.predict_proba(self._X_test)[:, 1]  # probability for target = 1

        # Calculate confusion matrix components for FPR and MDR
        self._y_pred = self._model.predict(self._X_test)
        
        # Predictions for *all* data
        self._output[f'{self._metric} Score'] = self._model.predict_proba(self._X)[:, 1]
        self._output[f'{self._metric} Prediction'] = self._model.predict(self._X)
        self._output[f'{self._metric} True Label'] = self._y
        
        # Add "test flag" column (1 if row in test set, else 0)
        self._output[f'{self._metric} Test Flag'] = 0
        self._output.loc[self._X_test.index, '{self._metric} Test Flag'] = 1



    def get_threshold_for_mdr(self, target_mdr=3.0):
        
        import numpy as np
        from sklearn.metrics import confusion_matrix

        
        thresholds = np.linspace(0, 1, 1000)  # finer grid
        valid_thresholds = []

        for t in thresholds:
            y_pred = (self._y_pred_prob >= t).astype(int)
            
            tn, fp, fn, tp = confusion_matrix(self._y_test, y_pred).ravel()
            
            if (fn + tp) == 0:
                continue  # avoid division by zero
            mdr = fn / (fn + tp)
            
            if mdr <= target_mdr / 100:
                valid_thresholds.append(t)

        if not valid_thresholds:
            return None

        # Choose the highest threshold that satisfies MDR ≤ target
        self._best_threshold = max(valid_thresholds)
        self._y_pred = (self._y_pred_prob >= self._best_threshold).astype(int)
        
    def compute_confusion_matrix(self,plot=False,fp=False):
        
        from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

        
        self._tn, self._fp, self._fn, self._tp = confusion_matrix(self._y_test, self._y_pred).ravel()
    
        # Compute False Positive Rate (FPR) and Missed Detection Rate (MDR)
        fpr = self._fp / (self._fp + self._tn)  
        mdr = self._fn / (self._fn + self._tp)  

        # Convert FPR and MDR to percentages
        self._fpr_percentage = fpr * 100
        self._mdr_percentage = mdr * 100
        
        if plot:
            
            import matplotlib.pyplot as plt
            
            cm = confusion_matrix(self._y_test, self._y_pred)
            fig, ax = plt.subplots(figsize=(6, 6))
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Target = 0', 'Target = 1'])
            disp.plot(cmap='Blues', ax=ax)
            plt.title('Confusion Matrix')
            
            if fp:
                
                fp = plt.savefig(fp,dpi=400)
            
            plt.close()
        
        
    def plot_feature_importance(self,fp=False):
        
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 6))
        self._feature_importance.sort_values().plot(kind='barh', color='royalblue')
        plt.xlabel('Feature Importance')
        plt.ylabel('Features')
        plt.title('Feature Importance for DLR XGBoost Model')
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        
        if fp:
            
            fp = plt.savefig(fp,dpi=400)
            
        plt.close()
        
        
    def plot_histogram(self,fp = False):
        
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 6))

        # Plot for target = 1 (in green)
        plt.hist(self._y_pred_prob[self._y_test == 1], bins=30, alpha=0.6, color='green', label='Target = 1')

        # Plot for target = 0 (in red)
        plt.hist(self._y_pred_prob[self._y_test == 0], bins=30, alpha=0.6, color='red', label='Target = 0')

        # Set logarithmic scale for y-axis
        plt.yscale('log')

        # Labels and title
        plt.xlabel('Model Score (Probability of Target = 1)', fontsize=14)
        plt.ylabel('Frequency (Log scale)', fontsize=14)
        plt.title('Histogram of Model Scores by Target Value', fontsize=18)
        plt.legend()

        # Create the text string with percentages
        textstr = f'False Positive Rate: {self._fpr_percentage:.2f}%\nMissed Detection Rate: {self._mdr_percentage:.2f}%'

        # Place the text box at the top center of the plot
        fig = plt.gcf()
        fig.text(0.5, 0.80, textstr, ha='center', va='top', fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))

        # Show grid and plot
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        if fp:
            
            fp = plt.savefig(fp,dpi=400)
        
        plt.close()
            
            
        
        
        



