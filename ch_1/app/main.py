from itertools import product

from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{product_id}")
async def products(product_id:int):
    return {"product_id": product_id,"response":"all products are here"}

@app.post("/product")
async def create_product(product:dict):
    return {"products": product}

@app.put("/product/{product_id}")
async def update_product(product:dict, product_id:int):
    return {"products": product}

@app.delete("/product/{product_id}")
async def delete_product(product_id:int):
    return {"products": product}

@app.patch("/product/{product_id}")
async def update_product(product:dict, product_id:int):
    return {"products": product}