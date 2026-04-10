from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional

from database import SessionLocal, engine, Base
from models.customer import Customer
from services.ingestion import ingest_data

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# INGEST
@app.post("/api/ingest")
def ingest(db: Session = Depends(get_db)):
    total = ingest_data(db)
    return {"status": "success", "records_processed": total}

# GET ALL + SEARCH
@app.get("/api/customers")
def get_customers(
    page: int = 1,
    limit: int = 10,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit

    query = db.query(Customer)

    # 🔍 SEARCH (TAMBAHAN)
    if search:
        query = query.filter(
            or_(
                Customer.first_name.ilike(f"%{search}%"),
                Customer.last_name.ilike(f"%{search}%"),
                Customer.email.ilike(f"%{search}%")
            )
        )

    total = query.count()
    data = query.offset(offset).limit(limit).all()

    return {
        "data": data,
        "total": total,
        "page": page,
        "limit": limit
    }

# GET BY ID
@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter_by(
        customer_id=customer_id
    ).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer