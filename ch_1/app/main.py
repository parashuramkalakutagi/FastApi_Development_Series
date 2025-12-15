from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{product_id}")
async def products(product_id:int):
    return {"product_id": product_id,"response":"all products are here"}