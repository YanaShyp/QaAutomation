import requests

url = "https://script.googleusercontent.com/macros/echo?user_content_key=4QyDY0m4tvZ1dEAZFtNfGWM8_jz4FR6rkB" \
      "sBe1YmMRBzsIRbMV7okMHwXzlWqe_auAmcMzBgLvxTP7vS3vfyegBHTBCSza4-m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncG" \
      "Qajx_ryfhECjZEnJeaAzlB7fGN7B1MHFCc8w9rFZkIFMbzYaQ6ew-oWK47SUICYEJjWO7IH20wYIzNwGlI6_8EDLjZdnSlwFGk1U" \
      "YRsWkzviUWgNz9Jw9Md8uu&lib=MkSKfxhejqWsGOYOheri7m_3N76I4c7sb"

response = requests.get(url)
our_goods = response.json()

goods = our_goods.get("data", [])

total_cost = 0
total_without_gluten_cost = 0

for good in goods:
    good_price = good.get("price", 0)

    if isinstance(good_price, int) or isinstance(good_price, float):
        total_cost += good_price

        if good.get("gluten") == False:
            total_without_gluten_cost += good_price


print(total_cost)
print(total_without_gluten_cost)
a = 0