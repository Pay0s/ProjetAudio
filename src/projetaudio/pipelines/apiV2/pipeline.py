"""
This is a boilerplate pipeline 'apiV2'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import prediction
from src.projetaudio.pipelines.etl.nodes import preprocess, normalize, denormalize_data

def create_pipeline(**kwargs) -> Pipeline:
        return pipeline([
        node(
                func=preprocess,
                inputs="user_value_input",
                outputs="user_post_traitement",
                name="user_traitement"
                ),                
        node(
                func=normalize,
                inputs="user_post_traitement",
                outputs="user_post_normalize",
                name="user_normalize"
                ),
        node(
                func=prediction,
                inputs="user_post_normalize",
                outputs="user_value_output",
                name="user_predict"
                ),
        node(
                func=denormalize_data,
                inputs="user_value_output",
                outputs="user_post_denormalize",
                name="user_denormalize"
                ),
        ])