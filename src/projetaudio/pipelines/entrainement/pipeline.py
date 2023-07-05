"""
This is a boilerplate pipeline 'entrainement'
generated using Kedro 0.18.10
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
                node(
                func=create_model,
                inputs=["train_data", "train_label", "test_data", "test_label"],
                outputs=None,
                name="create"
                )
    ])
