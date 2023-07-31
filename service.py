import bentoml
from bentoml.io import JSON
from hydra import compose, initialize
import torch

from src.runner import T5Runnable


with initialize(config_path="config/"):
    cfg = compose(config_name="config")

runner = bentoml.Runner(
    T5Runnable,
    name="t5runner",
)
svc = bentoml.Service(cfg.MODELS.service_name, runners=[runner])

@svc.api(input=JSON(), output=JSON())
def generate(inputs):
    input_texts = inputs["inputs"]
    result = runner.generate.run(input_texts)

    return result