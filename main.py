from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# Product Data
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True}
]

# Q1 - Get all products
@app.get("/products")
def get_products():
    return {
        "total_products": len(products),
        "products": products
    }


# Q2 - Filter products by price
@app.get("/products/filter")
def filter_products(min_price: int = Query(0)):
    
    filtered = []

    for product in products:
        if product["price"] >= min_price:
            filtered.append(product)

    return {
        "min_price": min_price,
        "results": filtered,
        "count": len(filtered)
    }


# Q3 - Customer Feedback Model
class CustomerFeedback(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    product_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=300)


# Store feedback
feedback = []


# Q3 - Submit Feedback
@app.post("/feedback")
def submit_feedback(data: CustomerFeedback):

    feedback.append(data.dict())

    return {
        "message": "Feedback submitted successfully",
        "feedback": data.dict(),
        "total_feedback": len(feedback)
    }
@app.get("/products/summary")
def product_summary():

    total_products = len(products)

    total_price = 0
    in_stock = 0
    out_of_stock = 0

    for product in products:
        total_price += product["price"]

        if product["in_stock"]:
            in_stock += 1
        else:
            out_of_stock += 1

    avg_price = total_price / total_products

    return {
        "total_products": total_products,
        "average_price": avg_price,
        "in_stock_products": in_stock,
        "out_of_stock_products": out_of_stock
    }