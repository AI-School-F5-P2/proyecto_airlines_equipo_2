#importación modelo y métodos tuning
from catboost import CatBoostClassifier, Pool

import pickle


def model_tuning(X_transformed, y_transformed):
    '''
    Esta función busca los mejores hiperparámetros del modelo seleccionado CatBoost
    '''
    train_pool = Pool(data = X_transformed, label = y_transformed)
    
    param_grid = {'iterations': [300, 400, 500],
                  'learning_rate': [0.01, 0.05, 0.1], 
                  'depth': [6, 8, 10, 12],
                  'l2_leaf_reg': [1, 3, 5, 7],
                  'border_count': [32, 64, 128],
                  'bagging_temperature': [0.6, 0.8, 1.0],
                  'grow_policy': ['SymmetricTree', 'Depthwise', 'Lossguide'],
                  'auto_class_weights': ['None', 'Balanced']}

    # results_rs = CatBoostClassifier().randomized_search(param_grid, train_pool, n_iter = 10, cv = 3, verbose = 5)
    
    # best_params = results_rs['params']
    # print(best_params)

    best_params = {'border_count': 64, 'depth': 6, 'l2_leaf_reg': 7, 'iterations': 500, 'bagging_temperature': 1.0, 
                   'learning_rate': 0.1, 'grow_policy': 'SymmetricTree', 'auto_class_weights': 'None'}

    final_model = CatBoostClassifier(**best_params)

    #entrenamos el modelo con todos los datos de entrenamiento
    final_model.fit(train_pool)

    #guardamos en un archivo.pkl
    final_cat_boost = 'catboost_airplanes.pkl'
    with open(final_cat_boost, 'wb') as archivo:
        pickle.dump(final_model, archivo)
