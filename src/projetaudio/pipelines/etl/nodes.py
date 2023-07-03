"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.18.10
"""
import pandas as pd
import numpy as np

def preprocess(df: pd.DataFrame) -> pd.DataFrame:

    # Code de prétraitement des images
    empty_columns = df.columns[df.isnull().any()]
    empty_rows = df[df[empty_columns].isnull().any(axis=1)]
    
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