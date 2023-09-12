#librería de tratamiento de datos
import numpy as np
import pandas as pd

#importación de métricas de modelos de clasificación
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc

#librería para graficar la curva ROC-AUC
import matplotlib.pyplot as plt

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
    
    probability = model.predict_proba(data_to_predict)
    
    #tomamos como clase positiva ('satisfied')
    y_probs = probability[:, model.classes_.tolist().index('satisfied')]
    
    return y_predicted, y_probs


def test(y_predicted, y_true, y_probs):
    '''
    Esta función calcula las métricas del modelo y las imprime
    Toma como clase positiva (pos_label) a 'satisfied'  
    '''
    acc = accuracy_score(y_true, y_predicted)
    conf_matrix = confusion_matrix(y_true, y_predicted)
    precision = precision_score(y_true, y_predicted, pos_label = 'satisfied')
    recall = recall_score(y_true, y_predicted, pos_label = 'satisfied')
    f1 = f1_score(y_true, y_predicted, pos_label = 'satisfied')
    
    print(f"Exactitud (Accuracy): {acc}")
    print("Matriz de Confusión:")
    print(conf_matrix)
    print(f"Precisión: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1}")
    print("Curva ROC-AUC:")
    plot_roc_curve(y_true, y_probs)

def plot_roc_curve(y_true, y_probs):
    fpr, tpr, _ = roc_curve(y_true, y_probs, pos_label = 'satisfied')
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize = (8, 6))
    plt.plot(fpr, tpr, color = 'darkorange', lw = 2, label = 'Curva ROC (Área (AUC) = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color = 'navy', lw = 2, linestyle = '--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title('Curva ROC')
    plt.legend(loc = 'lower right')
    plt.show()


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
    Esta función agrupa todas las anteriores para hacer un sólo llamado
    '''
    print(f"Métricas de {model}:")
    model.fit(data_to_predict, y_true)
    y_predicted, y_probs = prediction(model, data_to_predict)
    test(y_predicted, y_true, y_probs)
    # cross_validation(model, data_to_predict, y_true)


def test_models(X_transformed, y_transformed):
    '''
    Testea 4 modelos de ensamble que podrían funcionar
    '''
    # random_forest = RandomForestClassifier()
    # train_predict_test_cross(random_forest, X_transformed, y_transformed)

    # gradient_boosting = GradientBoostingClassifier()
    # train_predict_test_cross(gradient_boosting, X_transformed, y_transformed)

    # light_gbm = LGBMClassifier(verbosity = 0)
    # train_predict_test_cross(light_gbm, X_transformed, y_transformed)

    # cat_boost = CatBoostClassifier()
    # train_predict_test_cross(cat_boost, X_transformed, y_transformed)

    best_params = {'border_count': 64, 'depth': 6, 'l2_leaf_reg': 7, 'iterations': 500, 'bagging_temperature': 1.0,
                   'learning_rate': 0.1, 'grow_policy': 'SymmetricTree', 'auto_class_weights': 'None'}

    cat_boost_tuned = CatBoostClassifier(**best_params)
    train_predict_test_cross(cat_boost_tuned, X_transformed, y_transformed)

