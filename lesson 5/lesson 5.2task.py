import requests

url = "https://script.googleusercontent.com/macros/echo?user_content_key=0Y1M-JDzWXjjjRUelwlfgVz3yKLaAvwxWaLuwawFR" \
      "2cG8knaMan2sYH0vynVONb6qIk-ORcb736IKDZAPKryCgJKIpa28CP-m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZ" \
      "EnCi8PQ6N_8eYeTe5LfK-X_ax0H946o-rMnLp2n2MCHyp9P3JDrH9UW-YhLbCKEJyWcgpJFBzELIxbIX5A2H1SqfNb8k7Iz8qotz9Jw9Md" \
      "8uu&lib=MkSKfxhejqWsGOYOheri7m_3N76I4c7sb"

response = requests.get(url)
our_products = response.json()

products = our_products.get("goods", [])

total_cost = 0
total_without_gluten_cost = 0

for product in products:
    product_price = product.get("price", 0)
    product_stock = product.get("remainder", 0)
    product_cost = product_price * product_stock

    if isinstance(product_price, (int, float)) and isinstance(product_stock, (int, float)):
        total_cost += product_cost

        if not product.get("gluten"):
            total_without_gluten_cost += product_cost


print(total_cost)
print(total_without_gluten_cost)

