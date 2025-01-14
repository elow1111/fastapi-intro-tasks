from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# Модель данных продукта
class Specifications(BaseModel):
    size: str = Field(..., description="Размер продукта")
    color: str = Field(..., description="Цвет продукта")
    material: str = Field(..., description="Материал продукта")

# Модель продукта
class Product(BaseModel):
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта (должна быть больше 0)")
    specifications: Specifications = Field(..., description="Характеристики продукта")

class ProductResponse(BaseModel):
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта (должна быть больше 0)")
    id: int = Field(...)

class ProductDetailResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта (должна быть больше 0)")
    specifications: Specifications = Field(..., description="Характеристики продукта")

@app.get("/product/{product_id}", response_model=ProductDetailResponse)
async def get_product(product_id:int) -> ProductDetailResponse:
    product = next((item for item in product_list if item["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products", response_model=List[ProductResponse])
async def get_products() -> List[ProductResponse]:
    """
    Возвращает список всех продуктов в базе данных.
    """
    return product_list

@app.post("/product")
async def add_product(data: Product):
    global product_id_counter
    new_product = data.dict()
    new_product["id"] = product_id_counter
    product_id_counter += 1
    product_list.append(new_product)
    return new_product
# END
