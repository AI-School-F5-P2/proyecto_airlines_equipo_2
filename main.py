import pandas as pd

from functions_methods.utils import load_data, separate_train_set, X_y_separation

from experimental_pipelines.experiments import first_experiment, second_experiment, third_experiment
from experimental_pipelines.experiments import fourth_experiment, fifth_experiment, sixth_experiment, seventh_experiment
from sklearn.pipeline import Pipeline

from models_metrics.MLmodels import test_models

from models_metrics.catboost_tuning import model_tuning


if __name__ == "__main__":
    df = load_data()
    
    df_train = separate_train_set(df, 0.15)
    
    X_train, y_train = X_y_separation(df_train, 'satisfaction')
    
    # X_transformed1, y_transformed1 = first_experiment(X_train, y_train)
    # test_models(X_transformed1, y_transformed1)

    # X_transformed2, y_transformed2 = second_experiment(X_train, y_train)
    # test_models(X_transformed2, y_transformed2)

    X_transformed3, y_transformed3 = third_experiment(X_train, y_train)
    # test_models(X_transformed3, y_transformed3)

    # X_transformed4, y_transformed4 = fourth_experiment(X_train, y_train)
    # test_models(X_transformed4, y_transformed4)

    # X_transformed5, y_transformed5 = fifth_experiment(X_train, y_train)
    # test_models(X_transformed5, y_transformed5)

    # X_transformed6, y_transformed6 = sixth_experiment(X_train, y_train)
    # test_models(X_transformed6, y_transformed6)

    # X_transformed7, y_transformed7 = seventh_experiment(X_train, y_train)
    # test_models(X_transformed7, y_transformed7)

    model_tuning(X_transformed3, y_transformed3)

    #pipeline_final = Pipeline(steps = [('pipeline', full_pipeline), ('model', results_rs)])
    
    #pipeline_final.fit(X_transformed3, y_transformed3)