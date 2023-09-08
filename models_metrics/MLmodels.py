#librería de tratamiento de datos
import numpy as np
import pandas as pd

#importación de métricas de modelos de clasificación
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

#librería para la validación cruzada
from sklearn.model_selection import cross_validate

#modelos de ensemble
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


def prediction(model, data_to_predict):
    '''
    Esta función recibe el modelo que debe aplicarse y la matriz X (variables predictoras)
    Retorna la y que predice
    '''
    y_predicted = model.predict(data_to_predict)
    
    return y_predicted


def test(y_predicted, y_true):
    '''
    Esta función calcula las métricas del modelo y las imprime    
    '''
    acc = accuracy_score(y_true, y_predicted)
    conf_matrix = confusion_matrix(y_true, y_predicted)
    precision = precision_score(y_true, y_predicted)
    recall = recall_score(y_true, y_predicted)
    f1 = f1_score(y_true, y_predicted)
    
    print(f"Exactitud (Accuracy): {acc}")
    print("Matriz de Confusión:")
    print(conf_matrix)
    print(f"Precisión: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1}")


# def cross_validation(model, data_to_predict, y_true):
#     '''
#     Recibe el modelo, la matriz X y el vector y transformados para hacer la validación cruzada
#     Devuelve una media del 'accuracy'
#     '''
#     cross_val = cross_validate(model, data_to_predict, y_true, cv = 10, scoring = 'accuracy', error_score = 'raise')
#     acc_mean = np.mean(cross_val['test_score'])
#     print(f"Validación cruzada: {acc_mean}")


def train_predict_test_cross(model, data_to_predict, y_true):
    '''
    Esta función agrupa las dos anteriores para hacer un sólo llamado
    '''
    print(f"Métricas de {model}:")
    model.fit(data_to_predict, y_true)
    y_predicted = prediction(model, data_to_predict)
    test(y_predicted, y_true)
    # cross_validation(model, data_to_predict, y_true)


def test_models(X_transformed, y_transformed):
    '''
    Testea 4 modelos de ensamble que podrían funcionar
    '''
    random_forest = RandomForestClassifier()
    train_predict_test_cross(random_forest, X_transformed, y_transformed)

    gradient_boosting = GradientBoostingClassifier()
    train_predict_test_cross(gradient_boosting, X_transformed, y_transformed)

    light_gbm = LGBMClassifier(verbosity = 0)
    train_predict_test_cross(light_gbm, X_transformed, y_transformed)

    cat_boost = CatBoostClassifier()
    train_predict_test_cross(cat_boost, X_transformed, y_transformed)

