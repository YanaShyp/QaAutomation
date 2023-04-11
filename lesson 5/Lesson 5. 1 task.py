from pprint import pprint

import requests

url = "https://dummyjson.com/users?limit=100"

response = requests.get(url)
our_users = response.json()

users = our_users.get("users", [])

for user in users:
    addresses = user.get("address", {})
    if user.get("address", {}).get("city") == "Louisville":
        print(user.get("firstName"))

    # print(isinstance(addresses, dict))

    # total_users_Louisville = []
    # for address in addresses:
    #     if "city" == "Louisville":
    #         print(address)

    # for address in addresses:
    #     if addresses["city"] == "Louisville":
    #         print(addresses.get("city"))





# for user in users:
#     if user.get('age') > 30:
#         total_users_Louisville.append(user)
#         print(total_users_Louisville)









pass
