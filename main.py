import pandas as pd

from functions_methods.utils import load_data, separate_train_set, X_y_separation

from experimental_pipelines.experiments import first_experiment, second_experiment, third_experiment
from experimental_pipelines.experiments import fourth_experiment, fifth_experiment, sixth_experiment, seventh_experiment
from sklearn.pipeline import Pipeline

from models_metrics.MLmodels import test_models

from models_metrics.catboost_tuning import model_tuning
from models_metrics.eval_model import model_testing

from models_metrics.eval_model import one_prediction

from app.app_streamlit import SatisfactionPredictionApp

from config.models import ModelDataClients

from config.database import engine


if __name__ == "__main__":
    df = load_data('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/proyecto_airlines_equipo_2/functions_methods/airlinedataset.csv')
    
    df_train = separate_train_set(df, 0.15)
    
    X_train, y_train = X_y_separation(df_train, 'satisfaction')
    
    #TRANSFORMACIONES SELECCIONADAS!!!
    X_transformed3 = third_experiment(X_train, y_train)
    # test_models(X_transformed3, y_train)

    # one_prediction()

    ModelDataClients.metadata.create_all(bind = engine)

    app = SatisfactionPredictionApp()
    app.run()

    # X_transformed1 = first_experiment(X_train, y_train)
    # test_models(X_transformed1, y_train)

    # X_transformed2 = second_experiment(X_train, y_train)
    # test_models(X_transformed2, y_train)

    # X_transformed4 = fourth_experiment(X_train, y_train)
    # test_models(X_transformed4, y_train)

    # X_transformed5 = fifth_experiment(X_train, y_train)
    # test_models(X_transformed5, y_train)

    # X_transformed6 = sixth_experiment(X_train, y_train)
    # test_models(X_transformed6, y_train)

    # X_transformed7 = seventh_experiment(X_train, y_train)
    # test_models(X_transformed7, y_train)
    
    # pipeline_final = Pipeline(steps = [('pipeline', full_pipeline), ('model', results_rs)])
    
    # pipeline_final.fit(X_transformed3, y_transformed3)

    # model_tuning(X_transformed3, y_train)

    # model_testing()