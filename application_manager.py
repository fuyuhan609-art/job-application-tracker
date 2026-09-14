VALID_STATUSES = [
    "Saved",
    "Applied",
    "Interview",
    "Rejected",
    "Offer",
    "Withdrawn"
]
from database import (
    add_application as db_add_application,
    list_applications as db_list_applications,
    update_status as db_update_status,
    delete_application as db_delete_application,
    find_application as db_find_application
)

def add_application(company, position, status):
    if status not in VALID_STATUSES:
        print("Invalid status.")
        return
    db_add_application(company, position, status)


def list_applications():
    return db_list_applications()
   

def update_status(application_id, new_status):
    if new_status not in VALID_STATUSES:
        print("Invalid status.")
        return

    db_update_status(application_id, new_status)

def delete_application(application_id):
    deleted_count = db_delete_application(application_id)

    if deleted_count == 0:
        print("Application not found.")
    else:
        print("Application deleted successfully.")

def find_application(application_id):
    return db_find_application(application_id)