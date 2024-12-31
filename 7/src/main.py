from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductBase(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

class ProductInDB(ProductBase):
    id: int

@app.post("/product", response_model=ProductInDB)
async def create_product(product: ProductBase):
    global product_id_counter
    product_data = product.dict()
    product_data["id"] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return product_data

@app.get("/products", response_model=List[ProductInDB])
async def get_products():
    return product_list
# END
