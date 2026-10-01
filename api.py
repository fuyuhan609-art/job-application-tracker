import swagger_ui
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


from application_manager import VALID_STATUSES

from database import (
    create_table,
    add_application as db_add_application,
    list_applications as db_list_applications,
    find_application as db_find_application,
    update_status as db_update_status,
    delete_application as db_delete_application
)
app = FastAPI(docs_url=None)
app.mount(
    "/swagger-static",
    StaticFiles(directory=str(swagger_ui.__path__[0] + "/static")),
    name="swagger-static",
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        swagger_js_url="/swagger-static/swagger-ui-bundle.js",
        swagger_css_url="/swagger-static/swagger-ui.css",
    )


class Application(BaseModel):
    company: str
    position: str
    status: str

class StatusUpdate(BaseModel):
    status: str

class ApplicationResponse(BaseModel):
    id: int
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


@app.get(
    "/applications/{application_id}",
    response_model=ApplicationResponse
)
def get_application(application_id: int):
    application = db_find_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application_to_dict(application)

@app.get(
    "/applications",
    response_model=list[ApplicationResponse]
)
def get_applications():
    applications = db_list_applications()

    return [
        application_to_dict(application)
        for application in applications
    ]

@app.post("/applications")
def create_application(application: Application):
    application_id = db_add_application(
        application.company,
        application.position,
        application.status
    )

    return {
        "message": "Application created successfully",
        "application_id": application_id
    }

@app.patch("/applications/{application_id}")
def update_application(
    application_id: int,
    status_update: StatusUpdate
):
    application = db_find_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    if status_update.status not in VALID_STATUSES:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    db_update_status(
        application_id,
        status_update.status
    )

    return {
        "message": "Application status updated successfully"
    }

@app.delete("/applications/{application_id}")
def delete_application(application_id: int):
    application = db_find_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    db_delete_application(application_id)

    return {
        "message": "Application deleted successfully"
    }