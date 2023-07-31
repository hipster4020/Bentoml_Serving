# 🤖 Advertising Serving

# 👉🏻 model
MBTI type 구분, 마케팅 정보 12개, 소구점을 입력받아 광고 문구를 추출하는 T5 model Inference API<br>
bentoml을 활용하여 Docker image 구축 후 nvidia-docker run<br>
https://www.notion.so/textnet/aaf34164cc234daf93fb0e432217fdcf


# 👉🏻 script
bash containerize.sh<br>
bash startup.sh


# 👉🏻 tree
```bash
.
├── src
│   ├── model_save.py
│   └── runner.py
├── .gitignore
├── bentofile.yaml
├── containerize.sh
├── README.md
├── request.py
├── service.py
└── startup.sh
```