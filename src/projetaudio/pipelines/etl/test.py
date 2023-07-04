import pandas as pd
import numpy as np
import pytest

from .nodes import preprocess, splitTrainTest

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

def test_answer():

    df2 = preprocess(df_test)

    # Vérifie si les deux DataFrames sont identiques
    are_equal = df2.equals(df_corriger.astype(int))

    assert are_equal == True