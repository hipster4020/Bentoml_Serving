import requests


res = requests.post(
    "http://localhost:3000/generate",
    json={
        "input": {
            "type": "SF",
            "classified": "패션/쇼핑",
            "advertiser": "없음",
            "sender": "없음",
            "product": "기획전 [휴가 & 바캉스 샌들샵] 안내",
            "product_detail": "여름 휴가를 대비하여 샌들과 매치한 3가지 리조트룩을 제안",
            "purpose": "판촉 이벤트 안내",
            "benefit": "최대 55% 위클리 특가 할인, 추가 10% 할인 쿠폰 지급",
            "period": "주말까지",
            "target": "모든 고객",
            "season": "여름휴가",
            "weather": "무더위",
            "anniv": "휴가(바캉스)",
            "selling_point": "날씨와 관련된 감성 활용(한파, 폭염, 첫눈, 비오는 날 등)",
        }
    },
)
print(res.text)
