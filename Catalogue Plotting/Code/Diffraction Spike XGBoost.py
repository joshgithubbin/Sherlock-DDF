import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import xgboost as xgb
import pickle

df = pd.read_csv('XMM_Sample_Set_Notes_matt_2.csv')

def extract_spikes_old(df):
    """
    Extracts relevant columns based on the 'Spike' column values and creates a new dataframe.
    If 'Spike' is empty (NaN) AND 'DLR MATCH' == 'YES', it is treated as '1'.
    Adds a 'Spike' column in the new dataframe indicating whether the original 'Spike' column was empty (False) or had values (True).
    """
    mappings = {
        "1": ['DLR Host RA', 'DLR Host Dec', 'DLR Host a', 'DLR Host b', 'DLR Host pa'],
        "2": ['DLR Host RA 2', 'DLR Host Dec 2', 'DLR Host a 2', 'DLR Host b 2', 'DLR Host pa 2'],
        "3": ['A-Value Host RA', 'A-Value Host Dec', 'A-Value Host a', 'A-Value Host b', 'A-Value Host pa'],
        "4": ['A-Value Host RA 2', 'A-Value Host Dec 2', 'A-Value Host a 2', 'A-Value Host b 2', 'A-Value Host pa 2']
    }

    spikes = pd.DataFrame(index=df.index, columns=['RA', 'DEC', 'A', 'B', 'PA', 'Spike'])
    spikes[:] = np.nan  

    for idx, row in df.iterrows():
        is_spike_present = not pd.isna(row['Spike'])  

        if not is_spike_present and row.get('DLR MATCH') == 'YES':
            spike_values = ["1"]
            is_spike_present = False
        else:
            spike_values = str(row['Spike']).split(',') if is_spike_present else []

        selected_data = []

        for spike in spike_values:
            if spike in mappings and all(col in df.columns for col in mappings[spike]):
                selected_data.append(row[mappings[spike]].values) 

        if selected_data:
            selected_data = np.array(selected_data, dtype=float)
            spikes.loc[idx, ['RA', 'DEC', 'A', 'B', 'PA']] = np.nanmean(selected_data, axis=0)
        
        spikes.loc[idx, 'Spike'] = is_spike_present  

    return spikes

import pandas as pd
import numpy as np

def extract_spikes(df):
    """
    Extracts and prints SNID values separately for cases where 'Spike' contains "1", "2", "3", or "4".
    """

    spike_categories = {"1": [], "2": [], "3": [], "4": []}

    for idx, row in df.iterrows():
        if pd.isna(row['Spike']):
            continue  # Skip NaN values

        spike_values = str(row['Spike']).split(',')

        for spike in spike_values:
            if spike in spike_categories:
                spike_categories[spike].append(row['SNID'])

    # Print SNID values for each spike type
    for spike_type, snid_list in spike_categories.items():
        print(f"Spike Type {spike_type}: {snid_list}")

    return spike_categories  # Return the categorized SNID lists if needed


# Function to plot feature importance bar chart
def plot_feature_importance(feature_importance):
    plt.figure(figsize=(10, 6))
    feature_importance.sort_values().plot(kind='barh', color='royalblue')
    plt.xlabel('Feature Importance')
    plt.ylabel('Features')
    plt.title('Feature Importance for RandomForest (100 Estimators)')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

# Function to plot the histogram with FPR and MDR
def plot_histogram(y_pred_prob, y_test, fpr_percentage, mdr_percentage):
    plt.figure(figsize=(10, 6))

    # Plot for target = 1 (in green)
    plt.hist(y_pred_prob[y_test == 1], bins=30, alpha=0.6, color='green', label='Target = 1')

    # Plot for target = 0 (in red)
    plt.hist(y_pred_prob[y_test == 0], bins=30, alpha=0.6, color='red', label='Target = 0')

    # Set logarithmic scale for y-axis
    plt.yscale('log')

    # Labels and title
    plt.xlabel('Model Score (Probability of Target = 1)', fontsize=14)
    plt.ylabel('Frequency (Log scale)', fontsize=14)
    plt.title('Histogram of Model Scores by Target Value', fontsize=18)
    plt.legend()

    # Create the text string with percentages
    textstr = f'False Positive Rate: {fpr_percentage:.2f}%\nMissed Detection Rate: {mdr_percentage:.2f}%'

    # Place the text box at the top center of the plot
    fig = plt.gcf()
    fig.text(0.5, 0.80, textstr, ha='center', va='top', fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))

    # Show grid and plot
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Function to plot confusion matrix
def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Target = 0', 'Target = 1'])
    disp.plot(cmap='Blues', ax=ax)
    plt.title('Confusion Matrix')
    plt.show()
    
def generate_X_y(df):
    """
    Generates the feature matrix X and target vector y for the model.
    
    Features:
    - 'A': Ellipticity parameter
    - 'ellipticity': Ellipticity calculated as 1 - (B/A)
    - 'PA_norm': Normalized PA between 0 and 1
    
    Target:
    - 'Target': 1 if Spike is True, 0 if Spike is False
    
    Returns:
    - X (features): A DataFrame with features
    - y (target): A Series with target labels (0 or 1)
    """
    # Normalize PA between 0 and 1
    df['PA_norm'] = (df['PA'] + 90) / 180
    
    # Compute ellipticity, handling NaN values
    df['ellipticity'] = 1 - (df['B'].fillna(df['A']) / df['A'])
    
    # Convert 'A', 'ellipticity', and 'PA_norm' to float (if they are not already)
    df['A'] = pd.to_numeric(df['A'], errors='coerce')
    df['ellipticity'] = pd.to_numeric(df['ellipticity'], errors='coerce')
    df['PA_norm'] = pd.to_numeric(df['PA_norm'], errors='coerce')
    
    # Create the feature matrix X
    X = df[['A']].copy()
    X['ellipticity'] = df['ellipticity']
    X['PA'] = df['PA_norm']
    
    # Generate target vector y
    df['Target'] = np.where(df['Spike'], 1, 0)
    y = df['Target']
    
    return X, y

def plot_mdr_vs_fpr_range(y_test, y_pred_prob, num_points=10000):
    """
    Plots the Missed Detection Rate (MDR) vs False Positive Rate (FPR) for a range of classification thresholds.
    
    Parameters:
    - y_test: True target labels
    - y_pred_prob: Predicted probabilities for the target = 1
    - num_points: Number of points in the range of thresholds (default is 1000)
    """
    thresholds = np.linspace(0, 1, num_points)  # Thresholds from 0% to 100%
    fpr_values = []
    mdr_values = []

    # Loop through all thresholds and calculate FPR and MDR
    for threshold in thresholds:
        # Make predictions based on the current threshold
        y_pred = (y_pred_prob >= threshold).astype(int)

        # Calculate confusion matrix components
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

        # Compute FPR and MDR
        fpr = fp / (fp + tn)  # False Positive Rate
        mdr = fn / (fn + tp)  # Missed Detection Rate
        
        # Append the values to the lists
        fpr_values.append(fpr * 100)  # Convert to percentage
        mdr_values.append(mdr * 100)  # Convert to percentage
    
    # Plotting FPR vs MDR across different thresholds
    plt.figure(figsize=(8, 6))
    plt.plot(fpr_values, mdr_values, color='purple', lw=2)  # Removed the 'marker' argument
    
    # Labels and title
    plt.xlabel('False Positive Rate (%)', fontsize=14)
    plt.ylabel('Missed Detection Rate (%)', fontsize=14)
    plt.title('MDR vs FPR for Range of Thresholds', fontsize=18)
    
    # Set the axis limits from 0% to 100%
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    
    # Add gridlines for better visualization
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Show the plot
    plt.show()
    

def get_threshold_for_fpr_mdr(y_test, y_pred_prob, target_value, metric='fpr', num_points=1000):
    """
    Returns the threshold value corresponding to a given FPR or MDR.
    
    Parameters:
    - y_test: True target labels
    - y_pred_prob: Predicted probabilities for the target = 1
    - target_value: Desired FPR or MDR value (between 0 and 100)
    - metric: Specify 'fpr' to find threshold for FPR, or 'mdr' for MDR (default is 'fpr')
    - num_points: Number of points in the range of thresholds (default is 1000)
    
    Returns:
    - threshold: Corresponding threshold value for the target FPR or MDR
    """
    thresholds = np.linspace(0, 1, num_points)  # Thresholds from 0% to 100%
    fpr_values = []
    mdr_values = []

    # Loop through all thresholds and calculate FPR and MDR
    for threshold in thresholds:
        # Make predictions based on the current threshold
        y_pred = (y_pred_prob >= threshold).astype(int)

        # Calculate confusion matrix components
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

        # Compute FPR and MDR
        fpr = fp / (fp + tn)  # False Positive Rate
        mdr = fn / (fn + tp)  # Missed Detection Rate
        
        # Append the values to the lists
        fpr_values.append(fpr * 100)  # Convert to percentage
        mdr_values.append(mdr * 100)  # Convert to percentage
    
    # Choose the corresponding metric (FPR or MDR)
    if metric == 'fpr':
        # Find the threshold corresponding to the target FPR
        threshold_idx = np.argmin(np.abs(np.array(fpr_values) - target_value))
        return thresholds[threshold_idx]
    elif metric == 'mdr':
        # Find the threshold corresponding to the target MDR
        threshold_idx = np.argmin(np.abs(np.array(mdr_values) - target_value))
        return thresholds[threshold_idx]
    else:
        raise ValueError("Metric must be either 'fpr' or 'mdr'")


def plot_ellipticity_vs_A(X, y_pred_prob):
    """
    Plots a scatter plot of ellipticity vs A, color-coded by the probabilistic score.

    Parameters:
    - X: Feature matrix containing 'A' and 'ellipticity' columns.
    - y_pred_prob: Probabilistic scores (probability of target = 1).
    """
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X['A'], X['ellipticity'], c=y_pred_prob, cmap='viridis', alpha=0.7, edgecolors='k')

    # Add colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label('Probability Score (Target = 1)')
    # Set x-axis to log scale
    plt.xscale('log')
    # Labels and title
    plt.xlabel('A (Semi-major Axis Length)', fontsize=14)
    plt.ylabel('Ellipticity (1 - B/A)', fontsize=14)
    plt.title('Ellipticity vs A (Color-coded by Model Probability Score)', fontsize=16)

    # Show grid
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()

def plot_ellipticity_vs_A_true(X, y_test):
    """
    Plots a scatter plot of ellipticity vs A, color-coded by the true target value (1 or 0),
    with target = 1 on top of target = 0 to avoid overlap.
    
    Parameters:
    - X: Feature matrix containing 'A' and 'ellipticity' columns.
    - y_test: True target labels (0 or 1).
    """
    plt.figure(figsize=(10, 6))
    
    # First plot the points where y_test == 0 (target = 0) with lower alpha
    plt.scatter(X['A'][y_test == 0], X['ellipticity'][y_test == 0], c='purple', alpha=0.5, edgecolors='k', label='Target = 0')
    
    # Then plot the points where y_test == 1 (target = 1) with a higher alpha to be on top
    plt.scatter(X['A'][y_test == 1], X['ellipticity'][y_test == 1], c='yellow', alpha=0.7, edgecolors='k', label='Target = 1')

    # Set x-axis to log scale
    plt.xscale('log')

    # Add labels, title, and legend
    plt.xlabel('A (Semi-major Axis Length)', fontsize=14)
    plt.ylabel('Ellipticity (1 - B/A)', fontsize=14)
    plt.title('Ellipticity vs A', fontsize=16)
    plt.legend()

    # Add gridlines
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()



# Run function
spdf = extract_spikes_old(df)
spdf.dropna(subset=['RA', 'DEC', 'A', 'B', 'PA'], how='all', inplace=True)

# Normalize PA between 0 and 1
spdf['PA_norm'] = (spdf['PA'] + 90) / 180
spdf['ellipticity'] = 1 - (spdf['B'].fillna(spdf['A']) / spdf['A'])

df = spdf.copy()

X, y = generate_X_y(spdf)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=42)

# Train model with 100 estimators
xgb_model = xgb.XGBClassifier(objective="binary:logistic", random_state=42)
xgb_model.fit(X_train, y_train)

# Get feature importances
feature_importance = pd.Series(xgb_model.feature_importances_, index=X_train.columns)

# Predict the probabilities for the test set (probability of target = 1)
y_pred_prob = xgb_model.predict_proba(X_test)[:, 1]  # probability for target = 1

# Calculate confusion matrix components for FPR and MDR
y_pred = xgb_model.predict(X_test)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# Compute False Positive Rate (FPR) and Missed Detection Rate (MDR)
fpr = fp / (fp + tn)  
mdr = fn / (fn + tp)  

# Convert FPR and MDR to percentages
fpr_percentage = fpr * 100
mdr_percentage = mdr * 100

# Plot feature importance, histogram, and confusion matrix
plot_feature_importance(feature_importance)
plot_histogram(y_pred_prob, y_test, fpr_percentage, mdr_percentage)
plot_confusion_matrix(y_test, y_pred)

plot_mdr_vs_fpr_range(y_test, y_pred_prob)

fpr_threshold = get_threshold_for_fpr_mdr(y_test, y_pred_prob, target_value=5, metric='fpr')
print(f"Threshold for FPR = 5%: {fpr_threshold}")

plot_ellipticity_vs_A(X_test, y_pred_prob)
plot_ellipticity_vs_A_true(X_test, y_test)

# open('xgb_model.pkl', 'wb') as model_file:
#    pickle.dump(xgb_model, model_file)
