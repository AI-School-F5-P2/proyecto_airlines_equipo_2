import pandas as pd

from functions_methods.utils import load_data, separate_train_set, X_y_separation

from experimental_pipelines.experiments import first_experiment

from models_metrics.MLmodels import test_models


if __name__ == "__main__":
    df = load_data()
    
    df_train = separate_train_set(df, 0.15)
    
    X_train, y_train = X_y_separation(df_train, 'satisfaction')
    
    X_transformed, y_transformed = first_experiment(X_train, y_train)

    test_models(X_transformed, y_transformed)