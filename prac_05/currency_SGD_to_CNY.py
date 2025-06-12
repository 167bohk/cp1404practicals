import requests

THRESHOLD = 5.5

URL = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/sgd.json'
response = requests.get(URL)
country_to_exchange_rate = response.json()
# print(country_to_exchange_rate)
current_exchange_rate = country_to_exchange_rate['sgd']['cny']
print(country_to_exchange_rate['date'])
print(f"1 SGD can buy {current_exchange_rate} CNY")
if current_exchange_rate < THRESHOLD:
    print("Time to buy some SGD :)")
else:
    print("Too expensive :(")
