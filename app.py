
import requests
# get all products
api = "http://127.0.0.1:8000/products"
res = requests.get(api)
print(res.json())

# product by id
api = "http://127.0.0.1:8000/products/25"
res = requests.get(api)
print(res.json())

# update product
api = "http://127.0.0.1:8000/products/1"
updated_product = {
    "name": "iPhone 16 Pro",
    "category": "Mobiles",
    "price": 125000,
    "stock": 15,
    "brand": "Apple"
}
res = requests.put(api, json=updated_product)
print(res.json())

# products by category
api = "http://127.0.0.1:8000/category/Mobiles"
res = requests.get(api)
print(res.json())
 
# products by brand
api = "http://127.0.0.1:8000/brand/Apple"
res = requests.get(api)
print(res.json())

# Products Under a Price
api = "http://127.0.0.1:8000/price/5000"
res = requests.get(api)
print(res.json())