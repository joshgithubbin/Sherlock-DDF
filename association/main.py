#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 12:18:44 2025

@author: joshuaweston
"""

def lestrade(sample,field,catalogues, #list of transients, deep drilling field, catalogues for matching
             metric, #method of association
             overwrite=True, #overwrite relevant columns
             annotate=True, #check for annotations
             score=True, #get additional features
             savemodel=False,#save model
             check=False, #compare to true hosts in sample
             compare=False,
             aides=False,
             
             plot=True,
             
             r=15,
             ms=0.8,
             n=2
             ):
    
    
    art = r"""
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                   &&&                                                                              
                   &&&                                                    &&&                       
                   &&&                        &&                          &&&                       
                   &&&        &&&&&&  &&&&&&&&&&&&&&&& &&&  &&&&&    &&&&&&&&  &&&&&&&              
                   &&&      &&&   && &&&&    &&&   &&&&    &   &&&  &&&   &&& &&&   &&&             
                   &&&      &&&&&&&&& &&&&   &&&   &&&       &&&&& &&&    &&& &&&&&&&&&             
                   &&&      &&&         &&&& &&&   &&&    &&&  &&& &&&    &&& &&&                   
                  &&&&&&&&&&&&&&&  & &&  &&& &&&& &&&&    &&&  &&&  &&&&  &&& &&&&&  &              
                  &&&&&&&&&   &&&&&& &&&&&&   &&&&&&&&     &&&&&&&   &&&&&&&&   &&&&&&                                  
                                                                                           
                                              Version 0.10.0            
                                                                                                    
                                              
                                                                                                    
    """
    
    print(art)

    import lestrade
    import os
    import pandas as pd

        
    #######################################################################
    #
    #                           GENERATE SAMPLE
    #
    #######################################################################
    
    #define folders
    
    fp_a = f'{os.path.dirname(lestrade.__file__)}/output/'

    fp_b = f'{os.path.splitext(os.path.basename(sample))[0]}/{field}'
        
    parent_folder =  f"{fp_a}{fp_b}" #parent folder
    base_folder = f"{parent_folder}/base/"   #base folder
    annotated_folder = f"{parent_folder}/annotation/"     #annotation folder
    complete_folder = f"{parent_folder}/complete/"     #complete folder
    annotated_complete_folder = f"{parent_folder}/annotation & complete/"     #complete folder
    
    os.makedirs(parent_folder, exist_ok=True)
    os.makedirs(base_folder, exist_ok=True)
    os.makedirs(annotated_folder, exist_ok=True)
    os.makedirs(complete_folder, exist_ok=True)
    os.makedirs(annotated_complete_folder, exist_ok=True)
    
    fn = f'{os.path.splitext(os.path.basename(sample))[0]}_{field}' #base file name
    
    #get the filepath of the sample being loaded
    if annotate:
        
        if check:
            
            ifp = annotated_complete_folder
            
            ext = '_annotated_complete'
            
        else:
            
            ifp = annotated_folder
            
            ext = '_annotated'
        
    elif check:
        
        ifp = complete_folder
        
        ext = '_complete'
        
    else:
        
        ifp = base_folder     
        
        ext = ''
        
    input_file = f'{ifp}{fn}{ext}.csv'
        
    
    #If file exists and not overwrite, load it
    if os.path.exists(input_file) and not overwrite:
        
        subset = pd.read_csv(input_file)
        
        import lestrade.association.catalogue_init as l_cinit
        from lestrade.browser import fields,search
                
        ddfs, ddfs_pd = fields.load_ddfs(
                path=os.path.dirname(lestrade.__file__)+'/tools/fields/fields.csv'
            )

        rac = ddfs[field]['RAdeg']
        dec = ddfs[field]['DECdeg']
        d = ddfs[field]['Diameter']*1.2
        
        print(parent_folder)
        
        field_cat = l_cinit.gen_ls_cat(rac,dec,d,catalogues,config=f'{parent_folder}config.py')
        
        field_cat['GalID'] = range(1, len(field_cat) + 1)
        
    #else create it, either from base or from scratch  
    elif os.path.exists(f'{base_folder}{fn}.csv') and not overwrite:
        
        subset = pd.read_csv(f'{base_folder}{fn}.csv')
        
        import lestrade.association.catalogue_init as l_cinit
        from lestrade.browser import fields,search
                
        ddfs, ddfs_pd = fields.load_ddfs(
                path=os.path.dirname(lestrade.__file__)+'/tools/fields/fields.csv'
            )

        rac = ddfs[field]['RAdeg']
        dec = ddfs[field]['DECdeg']
        d = ddfs[field]['Diameter']*1.2
        
        field_cat = l_cinit.gen_ls_cat(rac,dec,d,catalogues,config=f'{parent_folder}config.py')
        
        field_cat['GalID'] = range(1, len(field_cat) + 1)
        
    else:
        
        transients = pd.read_csv(sample)
        
        #build the catalogue
        import lestrade.association.catalogue_init as l_cinit
        from lestrade.browser import fields,search
                
        ddfs, ddfs_pd = fields.load_ddfs(
                path=os.path.dirname(lestrade.__file__)+'/tools/fields/fields.csv'
            )

        rac = ddfs[field]['RAdeg']
        dec = ddfs[field]['DECdeg']
        d = ddfs[field]['Diameter']*1.2
        
        field_cat = l_cinit.gen_ls_cat(rac,dec,d,catalogues,f'{parent_folder}config.py')
        
        field_cat['GalID'] = range(1, len(field_cat) + 1)
    
    
        #constrain the sample
        subset = search.search(
            ddfs[field]['RAdeg'],
            ddfs[field]['DECdeg'],
            ddfs[field]['Diameter'] * 1.2,
            transients,
            'RA',
            'DEC'
        )
        
        overwrite = True
    
    subset_output = subset #needs fixing more tidily later (v0.8.2)    
    
    #######################################################################
    #
    #                           BASE ASSOCIATION
    #
    #######################################################################
    
        
    #now we need to apply the relevant method to the subset
    
    from lestrade.association.base_assoc import apply_method
    
    association_method = f'lestrade.association.methods.{metric}'
    
    import importlib
    
    module = importlib.import_module(association_method)
    
    subset_output = apply_method(subset, field_cat, module, metric,r,ms,n)
    
    subset_output.to_csv(f'{base_folder}{fn}.csv',index=False)
    
    
    #######################################################################
    #
    #                           ANNOTATION
    #
    #######################################################################

    if annotate:
        
        from lestrade.association.annotate import annotate_matches
        
        config_folder = f"{fp_a}{fp_b}/config"
        
        # Ensure the directory exists
        os.makedirs(config_folder, exist_ok=True)
                
        files = ['blended','ds']
        
        for fname in files:
            
            file_path = os.path.join(config_folder, f"{fname}.csv")
            
            if not os.path.exists(file_path):
                # Create empty dataframe and save it
                df = pd.DataFrame(columns=['GalID'])
                df.to_csv(file_path, index=False)
            else:
                # Read existing dataframe
                df = pd.read_csv(file_path,index_col=False)
                
                #now go through and identify catalogue items to annotate
                #for each item in subset_output, if host id exists in catalogue, flag
                subset_output = annotate_matches(subset_output,df,fname)                    

            #save
            subset_output.to_csv(f'{annotated_folder}{fn}_annotated.csv',index=False)
                
                
    #######################################################################
    #
    #                           INSPECT MATCHES
    #
    #######################################################################
    
    #if the sample has 'real' hosts identified, how well does the method identify them?
    if check:
        
        from lestrade.association.inspect_truth import does_true_exist,is_match_consistent
        from lestrade.association.annotate import overwrite_matches
        
        subset_output = does_true_exist(subset_output,field_cat,r * (1./3600.))
        #check if the true host exists in the catalogue
        
        #if so, check whether the true host is consistent with the method-identified host
        
        subset_output = is_match_consistent(subset_output,metric)
        
        #overwrite where necessary
        
        config_folder = f"{fp_a}{fp_b}/config"
        
        # Ensure the directory exists
        os.makedirs(config_folder, exist_ok=True)
        
        file_path = os.path.join(config_folder, f"overwrite_{metric}.csv")
        
        if not os.path.exists(file_path):
            # Create empty dataframe and save it
            df = pd.DataFrame(columns=['SNID'])
            df.to_csv(file_path, index=False)
            
        else:
            # Read existing dataframe
            df = pd.read_csv(file_path,index_col=False)
            
            #now go through and identify catalogue items to annotate
            #for each item in subset_output, if host id exists in catalogue, flag
            subset_output = overwrite_matches(subset_output,df,metric)  
        
        
        
        if annotate:
            
            subset_output.to_csv(f'{annotated_complete_folder}{fn}_annotated_complete.csv',index=False)
            
        else:
            
            subset_output.to_csv(f'{complete_folder}{fn}_complete.csv',index=False)
        
        
    field_cat.to_csv(f"{fp_a}{fp_b}/catalogue.csv",index=False) 
    
    #######################################################################
    #
    #                               SCORE
    #
    #######################################################################
    
    if score and n > 1:
        
        from lestrade.association.score import get_score_metrics, ls_model
        import importlib
        
        association_method = f'lestrade.association.methods.{metric}'
             
        module = importlib.import_module(association_method)
        
        subset_output = get_score_metrics(subset_output,metric,module)
    
    
        if annotate:
            
            if check:
            #annotate complete
                fp = f'{annotated_complete_folder}'
                                
            else:
            #annotate
                fp = f'{annotated_folder}'
                           
        elif complete:
            #complete
            fp = f'{complete_folder}'
            
        else:
            #base            
            fp = f'{base_folder}'
    
        mpfp = f'{fp}plots/{metric}/model/'
        
        os.makedirs(mpfp,exist_ok=True)
    
        if check:
            
            model = ls_model(subset_output,metric)
            
            model.feature_selection()
            model.train_test_split()
            model.train_xgb()
            model.get_threshold_for_mdr()
            model.compute_confusion_matrix(plot=True,fp=f'{mpfp}{fn}_{metric}_cm.png')
            model.plot_feature_importance(fp=f'{mpfp}{fn}_{metric}_fi.png')
            model.plot_histogram(fp=f'{mpfp}{fn}_{metric}_sd.png')
            
            subset_output = model._output
            
            
        else:
            
            # Get all matching models
            pattern = os.path.join(model_dir, f"{model_subname}_*.pkl")
            files = glob.glob(pattern)
            
            if len(files) > 0:
                
                import pickle
                
                # Sort by filename (timestamp is part of name)
                files.sort()
                
                model_filepath = files[-1]
                
                with open(latest_model_path, "rb") as f:
                    
                    model = pickle.load(f)
            
                    # Grab only the features the model expects
                    X = df[model.feature_names_in_]

                    
                    df["score"] = model.predict_proba(X)[:, 1]
                    
                    df["prediction"] = model.predict(X)
                                                            
                            
            
        if savemodel:
            
            from datetime import datetime
            
            model_folder = f'{os.path.dirname(lestrade.__file__)}/tools/models/{metric}/'
            
            os.makedirs(model_folder,exist_ok=True)
            
            mn = f'{fn}_{datetime.now().strftime("%y%m%d%H%M%S")}'
        
            import pickle
            
            with open(f'{model_folder}{mn}.pkl', "wb") as f:
                
                    pickle.dump(model._model, f)
        
        
        
    #######################################################################
    #
    #                           PLOT AIDES
    #
    #######################################################################
    
    if plot:
        
        from lestrade.plot.plot_aides import plot_method, aide
        consistency_split=False
        if annotate:
        
            if check:
                
                fp = f'{annotated_complete_folder}plots/{metric}/'
                consistency_split=True
            
            else:
                
                fp = f'{annotated_folder}plots/{metric}/'
        
        elif check:
            
            fp = f'{complete_folder}plots/{metric}/'
            consistency_split=True
            
        else:
            
            fp = f'{base_folder}plots/{metric}/'
        
        if aides:
            os.makedirs(fp, exist_ok=True)
            plot_method(subset_output,metric,n,fp,annotate,consistency_split)
        
        if score and n >1:
            
            from lestrade.plot.plot_features import plot_features, histplot
            
            feature_fp = f'{fp}Features/'
            os.makedirs(feature_fp, exist_ok=True)
            
            #generate histograms for method
            plot_features(subset_output,metric,feature_fp,consistency_split)


    #######################################################################
    #
    #                           COMPARE METHODS
    #
    #######################################################################
    
    if compare:
        from lestrade.plot.confusion import compare_methods
        
        #get list of other metrics
        import lestrade.association.methods as methods

        # Get the folder path of the package
        methods_path = methods.__path__[0]
        # List all .py files except __init__.py
        metrics = [
                    f[:-3]  # strip ".py"
                    for f in os.listdir(methods_path)
                    if f.endswith(".py") and f != "__init__.py" and f[:-3] != metric
                ]
        
        if annotate:
                
            folder = f'{annotated_complete_folder}'
            
        else:
                
            folder = f'{complete_folder}'
        
        for i in metrics:
            colname = f"{i} MATCH"
            
            if colname in subset_output:
                outpath = (f"{folder}plots/summary/")
                os.makedirs(outpath, exist_ok=True)
                compare_methods(subset_output, metric, i, fp=f'{outpath}{metric}_vs_{i}.png', cmap="Blues")      
    
    return subset_output




