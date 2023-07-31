import bentoml
import torch
from hydra import compose, initialize
from transformers import T5TokenizerFast, T5ForConditionalGeneration


with initialize(version_base="1.2", config_path="../config/"):
    cfg = compose(config_name="config")

device = torch.device("cuda")


class T5Runnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("nvidia.com/gpu",)
    SUPPORTS_CPU_MULTI_THREADING = False

    def __init__(self):
        # self.model = bentoml.pytorch.load_model(model_ref).eval()
        self.model = T5ForConditionalGeneration.from_pretrained(cfg.MODELS.save_dir).eval().to(device)
        self.tokenizer = T5TokenizerFast.from_pretrained(cfg.MODELS.save_dir)

    @bentoml.Runnable.method(batchable=False)
    def generate(self, input_texts):
        print(input_texts)
        inputs = [
            f"Text Generation: <type>{input_texts['type']}<classified>{input_texts['classified']}<advertiser>{input_texts['advertiser']}<sender>{input_texts['sender']}<product>{input_texts['product']}<product_detail>{input_texts['product_detail']}<purpose>{input_texts['purpose']}<benefit>{input_texts['benefit']}<period>{input_texts['period']}<target>{input_texts['target']}<season>{input_texts['season']}<weather>{input_texts['weather']}<anniv>{input_texts['anniv']}<selling_point>{input_texts['selling_point']}"
        ]
        encoded = self.tokenizer(inputs, padding=True, truncation=True, return_tensors="pt")
        sample = {k: v.to(device) for k, v in encoded.items()}
        with torch.no_grad():
            outputs = self.model.generate(
                **sample,
                temperature=cfg.PARAMS.temperature,
                do_sample=cfg.PARAMS.do_sample,
                max_length=cfg.PARAMS.max_length,
                penalty_alpha=cfg.PARAMS.penalty_alpha,
                top_k=cfg.PARAMS.top_k,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        # result
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        return result