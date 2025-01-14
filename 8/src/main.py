from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# Модель характеристик продукта
class Specifications(BaseModel):
    size: str = Field(..., description="Размер продукта (например, 'M', 'L', 'XL')")
    color: str = Field(..., description="Цвет продукта (например, 'red', 'blue')")
    material: str = Field(..., description="Материал продукта (например, 'cotton', 'leather')")

# Модель продукта
class Product(BaseModel):
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта (должна быть больше 0)")
    specifications: Specifications = Field(..., description="Характеристики продукта")

# Ответ при получении всех продуктов
class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: Specifications

@app.get("/products", response_model=dict)
async def get_products() -> dict:
    """
    Возвращает список всех продуктов в базе данных.
    """
    return {"products":product_list}

@app.post("/product", status_code=200)
async def add_product(data: Product):
    """
    Добавляет новый продукт в базу данных.
    """
    global product_id_counter
    new_product = data.dict()
    new_product["id"] = product_id_counter
    product_id_counter += 1
    product_list.append(new_product)
    return {"message": "Product added successfully", "product": new_product}
