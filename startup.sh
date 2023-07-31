source .venv/bin/activate
# docker run --rm -p 3000:3000 advertising:tdlcvxrmvs5kmqqb

# docker run -it -d \
# -e BENTOML_CONFIG=/home/bentoml/bentoml_config.yaml \
nvidia-docker run -it -d \
    -p 3000:3000 \
    --rm \
    --runtime=nvidia \
    --gpus all \
    --name textnet_advertising \
    advertising:uajrsdbpjgnleqqb serve