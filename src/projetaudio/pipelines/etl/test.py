import pandas as pd
import numpy as np
import pytest

from .nodes import preprocess, splitTrainTest

# Créer un DataFrame avec des entiers aléatoires
df = pd.DataFrame(np.random.randint(0, 100, size=(5, 3)), columns=['Colonne1', 'Colonne2', 'Colonne3'])

def df_parfait(df):

    dfreturn = preprocess(df)
    return dfreturn

def test_answer():

    df2 = df_parfait(df)

    # Vérifier si les deux DataFrames sont identiques
    are_equal = df.equals(df2)

    assert are_equal == False