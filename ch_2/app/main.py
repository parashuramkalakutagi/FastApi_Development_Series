from fastapi import FastAPI,status,Response,Body
from pydantic import BaseModel,Field,AnyUrl
from typing import Optional,Annotated
app = FastAPI()

data = [
  {
    "id": 1,
    "name": "Wireless Mouse",
    "category": "Electronics",
    "price": 799,
    "stock": 120,
    "rating": 4.3
  },
  {
    "id": 2,
    "name": "Bluetooth Headphones",
    "category": "Electronics",
    "price": 2499,
    "stock": 75,
    "rating": 4.5
  },
  {
    "id": 3,
    "name": "Laptop Backpack",
    "category": "Accessories",
    "price": 1299,
    "stock": 60,
    "rating": 4.2
  },
  {
    "id": 4,
    "name": "Smart Watch",
    "category": "Wearables",
    "price": 3999,
    "stock": 40,
    "rating": 4.4
  },
  {
    "id": 5,
    "name": "USB-C Charger",
    "category": "Electronics",
    "price": 699,
    "stock": 200,
    "rating": 4.1
  },
  {
    "id": 6,
    "name": "Running Shoes",
    "category": "Footwear",
    "price": 2999,
    "stock": 90,
    "rating": 4.6
  },
  {
    "id": 7,
    "name": "Office Chair",
    "category": "Furniture",
    "price": 6499,
    "stock": 25,
    "rating": 4.3
  },
  {
    "id": 8,
    "name": "Water Bottle",
    "category": "Home & Kitchen",
    "price": 399,
    "stock": 300,
    "rating": 4.0
  },
  {
    "id": 9,
    "name": "Mechanical Keyboard",
    "category": "Electronics",
    "price": 3499,
    "stock": 50,
    "rating": 4.7
  },
  {
    "id": 10,
    "name": "Desk Lamp",
    "category": "Home & Decor",
    "price": 999,
    "stock": 110,
    "rating": 4.2
  }
]
#
# @app.get("/product")
# async def read_product():
#     return {"data": data}

# @app.get("/products/{id}")
# async def read_product_id(id:int):
#   my_data = data
#   for i in my_data:
#     if i["id"] == id:
#       return i

# @app.post("/products", status_code=status.HTTP_201_CREATED)
# async def read_product_id(datas:dict):
#   my_data = data
#   if datas :
#     my_data.append(datas)
#     return {"data": my_data}


class Products(BaseModel):
  id:Annotated[int,Field(ge=1)]
  name:Annotated[str, Field(max_length=100 , strict=True, min_length=4)]
  price:Annotated[float,Field(gt=0)]
  stock:Optional[int]


@app.post("/product")
async def create_product(data:Products,key:Annotated[str,Body()]):
  dic = data.model_dump()
  stock_off = round(data.stock * 10)
  dic.update({"stock_offer": stock_off})
  return dic