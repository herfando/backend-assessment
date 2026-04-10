import requests
from sqlalchemy.orm import Session
from models.customer import Customer

FLASK_API = "http://mock-server:5000/api/customers"

def ingest_data(db: Session):
    page = 1
    limit = 10
    total_processed = 0

    while True:
        response = requests.get(f"{FLASK_API}?page={page}&limit={limit}")
        data = response.json()

        customers = data.get("data", [])
        if not customers:
            break

        for cust in customers:
            existing = db.query(Customer).filter_by(
                customer_id=cust["customer_id"]
            ).first()

            if existing:
                # UPDATE
                for key, value in cust.items():
                    setattr(existing, key, value)
            else:
                # INSERT
                new_customer = Customer(**cust)
                db.add(new_customer)

            total_processed += 1

        db.commit()
        page += 1

    return total_processed