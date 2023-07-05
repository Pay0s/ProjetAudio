"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.18.10
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess, splitTrainTest, normalize

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
                node(
                func=preprocess,
                inputs="source_datas",
                outputs="post_traitement_data",
                name="traitement"
                ),
                node(
                func=normalize,
                inputs="post_traitement_data",
                outputs="post_normalize_data",
                name="normalize_data"
                ),
                node(
                func=splitTrainTest,
                inputs="post_normalize_data",
                outputs=["train_data", "test_data", "train_label", "test_label"],
                name="split_data"
                ), 
            ])