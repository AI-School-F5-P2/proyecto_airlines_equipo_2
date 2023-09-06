import pandas as pd

from functions_methods.utils import load_data, separate_train_set, X_y_separation
from functions_methods.custom_transformers import DropColumnsTransformer, DropRowsTransformer, CategoricalDistance 
from functions_methods.custom_transformers import SimpleImputerTransformer, OneHotLabelEncoderTransformer


if __name__ == "__main__":
    df = load_data('airline_passenger_satisfaction.csv')
    df_air = separate_train_set(df, 0.15)
    X_train, y_train = X_y_separation(df_air, 'satisfaction')
