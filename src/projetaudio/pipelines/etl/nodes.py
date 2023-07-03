"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.18.10
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess(df: pd.DataFrame) -> pd.DataFrame:

    # Code de prétraitement des images
    empty_columns = df.columns[df.isnull().any()]
    empty_rows = df[df[empty_columns].isnull().any(axis=1)]
    
    # Dans cette condition on affiche les lignes non traitées et on les supprimes
    if not empty_columns.empty:

        for col in empty_columns:
            empty_row_indices = empty_rows.index[empty_rows[col].isnull()]

            for row_index in empty_row_indices:
                print(f"Erreur : La colonne '{col}' est vide dans la ligne {row_index}.")
                print("Toutes les ligne ce dessus on été supprimé")

        df = df.dropna()

        return df

    else:

        print("Aucune colonne vide dans le DataFrame.")

        return df

def splitTrainTest (df: pd.DataFrame) -> pd.DataFrame:

    # Séparation des données et des étiquettes
    label_col = [col for col in df.columns if "after" in col]

    data = df.copy()

    data = data.drop(label_col, axis=1)
    label = df[label_col]

    # Séparation des ensembles d'entraînement et de test pour les données et les étiquettes
    data_train, data_test, label_train, label_test = train_test_split(data, label, test_size=0.2, random_state=42)

    # Création des DataFrames d'entraînement et de test
    train_df = pd.concat([data_train, label_train], axis=1)
    test_df = pd.concat([data_test, label_test], axis=1)

    return data_train, data_test, train_df, test_df