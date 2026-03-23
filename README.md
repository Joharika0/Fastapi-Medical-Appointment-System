# FastAPI Medical Appointment System

This project is a backend API system built using FastAPI for managing medical appointments.

Features
- Doctor management
- Patient management
- Appointment booking
- CRUD operations
- Multi-step workflow (Book → Check-in → Check-out)
- Search functionality
- Sorting
- Pagination
- Combined browsing endpoint

Technologies
- Python
- FastAPI
- Pydantic
- Swagger UI

Run the Project

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

Open API docs:

http://127.0.0.1:8000/docs