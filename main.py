from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Medical Appointment System")


# ---------------------------
# Dummy Data
# ---------------------------

doctors = [
    {"id": 1, "name": "Dr. Rao", "specialization": "Cardiologist"},
    {"id": 2, "name": "Dr. Sharma", "specialization": "Dermatologist"},
    {"id": 3, "name": "Dr. Reddy", "specialization": "Orthopedic"},
]

patients = [
    {"id": 1, "name": "Rahul", "age": 25},
    {"id": 2, "name": "Anita", "age": 30},
]

appointments = []


# ---------------------------
# Pydantic Models
# ---------------------------

class AppointmentCreate(BaseModel):
    patient_id: int = Field(..., gt=0)
    doctor_id: int = Field(..., gt=0)
    date: str


class AppointmentUpdate(BaseModel):
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    date: Optional[str] = None


# ---------------------------
# Helper Functions
# ---------------------------

def find_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor
    return None


def find_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


def find_appointment(appointment_id: int):
    for appt in appointments:
        if appt["id"] == appointment_id:
            return appt
    return None


# ---------------------------
# Home Route
# ---------------------------

@app.get("/")
def home():
    return {"message": "Medical Appointment System API"}


# ---------------------------
# SEARCH
# ---------------------------

@app.get("/doctors/search")
def search_doctors(keyword: Optional[str] = Query(None)):
    results = doctors

    if keyword:
        results = [
            d for d in doctors
            if keyword.lower() in d["name"].lower()
        ]

    return results


# ---------------------------
# SORT
# ---------------------------

@app.get("/doctors/sort")
def sort_doctors(order: str = "asc"):

    sorted_list = sorted(doctors, key=lambda x: x["name"])

    if order == "desc":
        sorted_list.reverse()

    return sorted_list


# ---------------------------
# PAGINATION
# ---------------------------

@app.get("/doctors/page")
def paginate_doctors(page: int = 1, limit: int = 2):

    start = (page - 1) * limit
    end = start + limit

    return doctors[start:end]


# ---------------------------
# COMBINED BROWSE
# ---------------------------

@app.get("/doctors/browse")
def browse_doctors(
    keyword: Optional[str] = None,
    sort: Optional[str] = None,
    page: int = 1,
    limit: int = 2
):

    results = doctors

    if keyword:
        results = [
            d for d in results
            if keyword.lower() in d["name"].lower()
        ]

    if sort == "asc":
        results = sorted(results, key=lambda x: x["name"])

    if sort == "desc":
        results = sorted(results, key=lambda x: x["name"], reverse=True)

    start = (page - 1) * limit
    end = start + limit

    return results[start:end]


# ---------------------------
# GET APIs
# ---------------------------

@app.get("/doctors")
def get_all_doctors():
    return doctors


@app.get("/doctors/{doctor_id}")
def get_doctor_by_id(doctor_id: int):

    doctor = find_doctor(doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


@app.get("/patients")
def get_all_patients():
    return patients


@app.get("/appointments")
def get_all_appointments():
    return appointments


# ---------------------------
# Summary Endpoint
# ---------------------------

@app.get("/summary")
def summary():
    return {
        "total_doctors": len(doctors),
        "total_patients": len(patients),
        "total_appointments": len(appointments)
    }


# ---------------------------
# CREATE Appointment
# ---------------------------

@app.post("/appointments", status_code=201)
def create_appointment(data: AppointmentCreate):

    if not find_doctor(data.doctor_id):
        raise HTTPException(status_code=404, detail="Doctor not found")

    if not find_patient(data.patient_id):
        raise HTTPException(status_code=404, detail="Patient not found")

    new_appointment = {
        "id": len(appointments) + 1,
        "patient_id": data.patient_id,
        "doctor_id": data.doctor_id,
        "date": data.date,
        "status": "booked"
    }

    appointments.append(new_appointment)

    return new_appointment


# ---------------------------
# UPDATE Appointment
# ---------------------------

@app.put("/appointments/{appointment_id}")
def update_appointment(appointment_id: int, data: AppointmentUpdate):

    appt = find_appointment(appointment_id)

    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")

    if data.patient_id is not None:
        appt["patient_id"] = data.patient_id

    if data.doctor_id is not None:
        appt["doctor_id"] = data.doctor_id

    if data.date is not None:
        appt["date"] = data.date

    return {"message": "Appointment updated", "appointment": appt}


# ---------------------------
# DELETE Appointment
# ---------------------------

@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):

    appt = find_appointment(appointment_id)

    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointments.remove(appt)

    return {"message": "Appointment deleted"}


# ---------------------------
# Multi Step Workflow
# ---------------------------

@app.post("/appointments/{appointment_id}/checkin")
def checkin(appointment_id: int):

    appt = find_appointment(appointment_id)

    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appt["status"] = "checked-in"

    return appt


@app.post("/appointments/{appointment_id}/checkout")
def checkout(appointment_id: int):

    appt = find_appointment(appointment_id)

    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appt["status"] = "completed"

    return appt