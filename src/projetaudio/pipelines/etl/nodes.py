"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.18.10
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from kedro.extras.datasets.yaml import YAMLDataSet

import matplotlib.pyplot as plt
 
from sklearn.preprocessing import MinMaxScaler

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

        # Vérifiez si chaque cellule est de type numérique
        is_numeric = df.applymap(lambda x: isinstance(x, (int, float, np.number)))

        # Supprimez les lignes contenant des valeurs non numériques
        df = df[is_numeric.all(axis=1)]

        # Réinitialisez les index du DataFrame
        df = df.reset_index(drop=True)

        return df.astype(int)

    else:

        print("Aucune colonne vide dans le DataFrame.")

        return df

def normalize(df: pd.DataFrame) -> pd.DataFrame:

    parameters_dataset = YAMLDataSet(filepath='conf/base/parameters.yml')

    # Calculer les valeurs minimales et maximales du DataFrame entier
    min_value = df.min().min()
    max_value = df.max().max()  ##SAUVEGARDER LES 2 VALEURS

    variables = {
    'min_value': min_value,
    'max_value': max_value,
    }

    # Sauvegardez les variables dans le fichier parameters.yml
    parameters_dataset.save(variables)

    # Appliquer la formule de normalisation à chaque cellule du DataFrame
    normalized_df = (df - min_value) / (max_value - min_value)

    return normalized_df

# denormalize les lignes du dataframe
def denormalize_data(df: pd.DataFrame) -> pd.DataFrame:

    parameters_dataset = YAMLDataSet(filepath='conf/base/parameters.yml')

    # Charge les valeurs minimales et maximales à partir du fichier parameters.yml
    parameters = parameters_dataset.load()

    min_value = parameters['min_value']
    max_value = parameters['max_value']

    # Applique la formule de dénormalisation à chaque cellule du DataFrame
    denormalized_df = df * (max_value - min_value) + min_value

    return denormalized_df.astype(int)

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

    return data_train, data_test, label_train, label_test
