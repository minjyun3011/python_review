import requests

# zipcode = input("郵便番号<ハイフン無し7桁>は？")
zipcode = "8113103"
response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")
# print(response.text)

address_info = response.json()["results"][0]

prefecture_name = address_info["address1"]
city_name = address_info["address2"]
town_name = address_info["address3"]

address = f"{prefecture_name}{city_name}{town_name}"
print(address)



