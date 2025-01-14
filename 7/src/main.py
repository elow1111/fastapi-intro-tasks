from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# Модель данных продукта
class Product(BaseModel):
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
    

@app.get("/products", response_model=dict)
async def get_products() -> dict:
    """
    Возвращает список всех продуктов в базе данных.
    """
    return {"products": product_list}  # Возвращаем сам список

@app.post("/product")
async def add_product(data: Product):
    """
    Добавляет новый продукт в базу данных.
    """
    global product_id_counter
    new_product = data.model_dump()  # Используем model_dump
    new_product["id"] = product_id_counter
    product_id_counter += 1
    product_list.append(new_product)
    return {"product": new_product, "message": "Product added successfully"}
