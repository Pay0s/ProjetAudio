import pandas as pd
import numpy as np
import pytest

from .nodes import preprocess, splitTrainTest
from sklearn.model_selection import train_test_split


# Créer un DataFrame avec des entiers aléatoires
df_split = pd.DataFrame(np.random.randint(0, 100, size=(5, 3)), columns=['after_1', 'before', 'after_2'])


def test_answer():

    data = {
    'Colonne1': [1, 2, 23],
    'Colonne2': [2, 18, np.nan],
    'Colonne3': [3, np.nan, np.nan]
    }

    # Créer le DataFrame à partir du dictionnaire
    df_test = pd.DataFrame(data)

    data = {
        'Colonne1': [1],
        'Colonne2': [2],
        'Colonne3': [3]
    }

    # Créer le DataFrame à partir du dictionnaire
    df_corriger = pd.DataFrame(data)

    df2 = preprocess(df_test)

    # Vérifie si les deux DataFrames sont identiques
    are_equal = df2.equals(df_corriger.astype(int))

    assert are_equal == True


def test_after():

    data_train, data_test, train_df, test_df = splitTrainTest(df_split)
    label_col = [col for col in train_df.columns if "after" in col]

     #Verifier si label_col contient bien que les "after"
    if label_col == 2:
        return True
    
def test_dataframe_creation():
    # Créer un DataFrame de test avec des données et des étiquettes
    df = pd.DataFrame({'Colonne1': [1, 2, 3], 'Colonne2': [4, 5, 6], 'after_1': [7, 8, 9], 'after_2': [10, 11, 12]})
    
    # Appeler la fonction splitTrainTest avec le DataFrame de test
    data_train, data_test, train_df, test_df = splitTrainTest(df)
    
    # Vérifier que les DataFrames d'entraînement et de test ont été correctement créés
    # Vérifier les colonnes
    expected_columns = ['Colonne1', 'Colonne2']
    assert all(col in data_train.columns for col in expected_columns)
    assert all(col in data_test.columns for col in expected_columns)
    
    # Vérifier les dimensions
    expected_train_shape = (2, 2)  # Attendu : 2 lignes, 2 colonnes
    expected_test_shape = (1, 2)  # Attendu : 1 ligne, 2 colonnes
    assert data_train.shape == expected_train_shape
    assert data_test.shape == expected_test_shape
    
        
        

    

    
