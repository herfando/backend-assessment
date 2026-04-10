# Backend Technical Assessment - Data Pipeline

This project is a backend system built as a technical assessment. It demonstrates a simple data pipeline using Flask, FastAPI, PostgreSQL, and Docker.

## 🚀 Architecture Flow

Flask (Mock API with JSON data)  
→ FastAPI (Data ingestion service)  
→ PostgreSQL (Data storage)  
→ FastAPI (API response layer)

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

## 📦 Services

### 1. Mock Server (Flask)

- Serves customer data from JSON file
- Runs on port: `5000`
- Provides paginated API endpoints

### 2. Pipeline Service (FastAPI)

- Fetches data from Flask API
- Processes and stores data into PostgreSQL
- Provides REST API for database access
- Runs on port: `8000`

### 3. PostgreSQL

- Stores customer data
- Database: `customer_db`

---

## 🔌 API Endpoints

### Flask API

- `GET /api/customers`
- `GET /api/customers/{id}`
- `GET /api/health`

### FastAPI

- `POST /api/ingest`
- `GET /api/customers`
- `GET /api/customers/{id}`

---

## 🐳 Run Project with Docker

```bash
docker-compose up -d
```
