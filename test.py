import requests

res = requests.get('https://dummyjson.com/products')

print(res.text)