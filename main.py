from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session 
import crud 
import schema
from database import Base, engine, SessionLocal 
Base.metadata.create_all(bind=engine) 
app = FastAPI() 
def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 
@app.get("/") 
def welcome(): 
    return {"message": "Welcome to E-Commerce Application"} 
@app.post("/products", response_model=schema.ProductResponse) 
def create(product: schema.ProductCreate, db: Session = Depends(get_db)): 
    return crud.create_product(db, product) 
@app.get("/products", response_model=list[schema.ProductResponse]) 
def read_all(db: Session = Depends(get_db)): 
    return crud.get_products(db) 
@app.get("/products/{product_id}", response_model=schema.ProductResponse) 
def read_one(product_id: int, db: Session = Depends(get_db)): 
    product = crud.get_product(db, product_id) 
    if not product: 
        raise HTTPException(status_code=404, detail="Product not found") 
    return product 
@app.put("/products/{product_id}", response_model=schema.ProductResponse) 
def update(product_id: int, product: schema.ProductCreate, 
           db: Session = Depends(get_db)): 
    updated = crud.update_product(db, product_id, product) 
    if not updated: 
        raise HTTPException(status_code=404, detail="Product not found") 
    return updated 
@app.delete("/products/{product_id}") 
def delete(product_id: int, db: Session = Depends(get_db)): 
    deleted = crud.delete_product(db, product_id) 
    if not deleted: 
        raise HTTPException(status_code=404, detail="Product not found") 
    return {"message": "Product deleted successfully"} 
@app.get("/category/{category_name}") 
def category_products(category_name: str, db: Session = Depends(get_db)): 
    product_list = crud.get_by_category(db, category_name) 
    if not product_list: 
        raise HTTPException(status_code=404, detail="No products found in this category") 
    return product_list