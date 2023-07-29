import requests
import pandas as pd
import json

res = requests.get('https://dummyjson.com/products')

data = res.text

print(data)

df = pd.read_json(data)
print(df)