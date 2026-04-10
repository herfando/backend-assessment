# Backend Technical Assessment - Data Pipeline

This project is a backend system built as a technical assessment. It demonstrates a simple data pipeline using Flask, FastAPI, PostgreSQL, and Docker.

---

## 🚀 Architecture Flow

Flask (Mock Customer API)
↓
FastAPI (Ingestion Service)
↓
PostgreSQL (Database Storage)
↓
FastAPI (Query API Layer)

---

## 🧱 Tech Stack

- Python 3.10+
- Flask
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- dlt (data loading tool)

---

## 📦 Services Overview

### 1. Mock Server (Flask)

- Serves customer data from a JSON file
- Runs on port: `5000`
- Endpoints:
  - `GET /api/customers?page=&limit=`
  - `GET /api/customers/{id}`
  - `GET /api/health`

**Purpose:**
Acts as a mock external API source for customer data.

---

### 2. Pipeline Service (FastAPI)

- Fetches data from Flask API
- Processes and ingests data into PostgreSQL
- Provides REST API for querying stored data
- Runs on port: `8000`

**Endpoints:**

- `POST /api/ingest`
- `GET /api/customers?page=&limit=`
- `GET /api/customers/{id}`

**Responsibilities:**

- Auto-pagination from Flask API
- Upsert data into PostgreSQL
- Error handling and validation

---

### 3. PostgreSQL Database

- Stores customer data
- Database name: `customer_db`
- Table: `customers`

**Schema:**

- customer_id (VARCHAR, Primary Key)
- first_name (VARCHAR)
- last_name (VARCHAR)
- email (VARCHAR)
- phone (VARCHAR)
- address (TEXT)
- date_of_birth (DATE)
- account_balance (DECIMAL)
- created_at (TIMESTAMP)

---

## 🔌 API Endpoints Summary

### Flask API

- `GET /api/customers`
- `GET /api/customers/{id}`
- `GET /api/health`

### FastAPI

- `POST /api/ingest`
- `GET /api/customers`
- `GET /api/customers/{id}`

---

## 🐳 How to Run the Project

```bash
1. Build and start all services
docker-compose up --build
2. Run in detached mode
docker-compose up -d
3. Stop all services
docker-compose down

🧪 Testing the System
1. Check Flask health
curl http://localhost:5000/api/health
2. Run data ingestion
curl -X POST http://localhost:8000/api/ingest
3. Get paginated customers
curl "http://localhost:8000/api/customers?page=1&limit=5"
4. Get customer by ID
curl http://localhost:8000/api/customers/1

✅ Assessment Checklist
The following features have been implemented and tested:
1. Flask mock server successfully loads JSON data
2. Pagination works on Flask API
3. FastAPI ingestion service successfully fetches and stores data
4. PostgreSQL integration is working properly
5. Docker Compose runs all services successfully
6. All API endpoints are functional and tested
7. Data is successfully persisted and retrievable

🚀 Project Status
All required components are implemented:
1. Mock API (Flask)
2. Data pipeline (FastAPI)
3. Database storage (PostgreSQL)
4. Docker orchestration
5. Working ingestion flow
```
