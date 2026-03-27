# 🏋️ Gym Management System - FastAPI Project

This project is a complete backend system built using FastAPI as part of internship training.

## 🚀 Features

- REST API development using FastAPI
- Pydantic validation
- CRUD operations
- Multi-step workflows (Membership → Booking → Management)
- Search, Sorting, Pagination
- Swagger UI testing

## 📌 Endpoints Covered

- GET APIs (Home, Plans, Memberships)
- POST APIs (Create Plans, Memberships, Bookings)
- PUT APIs (Update Plans, Freeze/Reactivate Membership)
- DELETE APIs (Delete Plans, Cancel Bookings)

## 🔧 Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## ▶️ Run Project

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
