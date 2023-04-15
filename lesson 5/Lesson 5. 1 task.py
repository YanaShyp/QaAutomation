from pprint import pprint

import requests

url = "https://dummyjson.com/users?limit=100"

response = requests.get(url)
our_users = response.json()

users = our_users.get("users", [])

for user in users:
    addresses = user.get("address", {})
    if user.get("address", {}).get("city") == "Louisville":
        print(user.get("firstName") + " lives in Louisville")

age = []
for user in users:
    hair = user.get("hair", {})
    if hair.get("color") == "Brown":
        for key, value in user.items():
            if key == "age":
                age.append(value)


avg_age = sum(age)/len(age)
print("Average age of people with brown hair is", int(avg_age))












pass
