import hydra
from transformers import T5TokenizerFast, T5ForConditionalGeneration
import bentoml


@hydra.main(config_path="../config/", config_name="config")
def main(cfg):
    t5_model = T5ForConditionalGeneration.from_pretrained(cfg.MODELS.save_dir).cuda()
    t5_bento_model = bentoml.pytorch.save_model(
        cfg.MODELS.t5_model,
        t5_model,
        signatures={
            "generate": {"batchable": False},
        }
    )
    print(t5_bento_model)

if __name__=="__main__":
    main()