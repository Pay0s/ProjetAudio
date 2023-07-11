"""
This is a boilerplate pipeline 'apiV2'
generated using Kedro 0.18.11
"""

import pandas as pd
import mlflow.sklearn
import tensorflow

def prediction(x_test):
  
    model = mlflow.sklearn.load_model("runs:/ee0b0009b2bb4bb5ba3a43dc82ca6870/model")
    predictions = model.predict(x_test)
    print(predictions)

    return pd.DataFrame(predictions)