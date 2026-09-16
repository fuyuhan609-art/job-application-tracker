from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
    create_table,
    add_application as db_add_application,
    list_applications as db_list_applications,
    find_application as db_find_application
)


app = FastAPI()


class Application(BaseModel):
    company: str
    position: str
    status: str


def application_to_dict(application):
    return {
        "id": application[0],
        "company": application[1],
        "position": application[2],
        "status": application[3]
    }

create_table()

@app.get("/")
def read_root():
    return {"message": "Job Application Tracker API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/applications/{application_id}")
def get_application(application_id: int):
    application = db_find_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application_to_dict(application)

@app.get("/applications")
def get_applications():
    applications = db_list_applications()

    return [
        application_to_dict(application)
        for application in applications
    ]

@app.post("/applications")
def create_application(application: Application):
    db_add_application(
        application.company,
        application.position,
        application.status
    )

    return {
        "message": "Application created successfully"
    }