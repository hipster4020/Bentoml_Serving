source .venv/bin/activate

# python src/model_save.py
bentoml build
bentoml containerize advertising:latest