# 🏥 Medical Appointment System API

A **RESTful backend application** built using **FastAPI** to manage doctors, patients, and medical appointments.  
This project was developed as part of my **Advanced Generative AI Internship at Innomatics Research Labs**.

The system demonstrates real-world backend concepts such as **API design, data validation, workflow management, search, sorting, and pagination**.

---

# 🚀 Project Highlights

✔ RESTful API development using **FastAPI**  
✔ Structured data validation with **Pydantic**  
✔ Appointment lifecycle workflow (**Book → Check-in → Checkout**)  
✔ Doctor search functionality  
✔ Sorting and pagination support  
✔ Combined browsing with filtering and sorting  
✔ Interactive API testing using **Swagger UI**

---

# 🛠 Tech Stack

| Technology | Purpose |
|-----------|--------|
| Python | Core programming language |
| FastAPI | Backend API framework |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| Swagger UI | API testing and documentation |

---

# 📂 Project Structure


Fastapi_Medical_Appointment_System
│
├── main.py # FastAPI application with all API endpoints
├── README.md # Project documentation


---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

git clone https://github.com/Joharika0/Fastapi-Medical-Appointment-System.git
cd Fastapi-Medical-Appointment-System

## 2️⃣ Install Dependencies
pip install fastapi uvicorn

## 3️⃣ Run the Application
python -m uvicorn main:app --reload

--- 

# 🌐 API Documentation

Once the server starts, open the following in your browser:

Swagger API Docs

http://127.0.0.1:8000/docs

Alternative Documentation

http://127.0.0.1:8000/redoc

Swagger provides an interactive interface to test all APIs directly from the browser.

---

# 📌 API Endpoints
## Doctors
GET /doctors

GET /doctors/{doctor_id}

GET /doctors/search

GET /doctors/sort

GET /doctors/page

GET /doctors/browse

## Patients
GET /patients

## Appointments
GET /appointments

POST /appointments

PUT /appointments/{appointment_id}

DELETE /appointments/{appointment_id}

## Appointment Workflow
POST /appointments/{appointment_id}/checkin

POST /appointments/{appointment_id}/checkout

## System Summary
GET /summary

# 📊 Example API Request

## Create Appointment

**POST /appointments**

{
  "patient_id": 1,
  "doctor_id": 2,
  "date": "2026-03-25"
}


**Response**

{
  "id": 1,
  "patient_id": 1,
  "doctor_id": 2,
  "date": "2026-03-25",
  "status": "booked"
}

---

# 📚 What I Learned

Through this project I gained practical experience in:

• Backend API development with FastAPI

• Designing scalable REST APIs

• Input validation with Pydantic

• Implementing search, sorting, and pagination

• Managing multi-step workflows in backend systems

• Testing APIs with Swagger UI

---

# 👩‍💻 Author

Joharika

Advanced Generative AI Intern

Innomatics Research Labs


# ⭐ Acknowledgment

This project was developed as part of the Advanced Generative AI Internship Program at Innomatics Research Labs, which focuses on building real-world AI and backend development skills.

If you find this project helpful, consider giving it a ⭐ on GitHub!
