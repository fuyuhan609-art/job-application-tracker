VALID_STATUSES = [
    "Saved",
    "Applied",
    "Interview",
    "Rejected",
    "Offer",
    "Withdrawn"
]

def add_application(applications, company, position, status):
    application = {
        "company": company,
        "position": position,
        "status": status
    }
    applications.append(application)

def list_applications(applications):
    for application in applications:
        print(
            application["company"],
            "-",
            application["position"],
            "-",
            application["status"]
        )
   

def update_status(applications,company, new_status):
    if new_status not in VALID_STATUSES:
        print("Invalid status.")
        return

    for application in applications:
        if application["company"] == company:
            application["status"] = new_status
            print(f"{company} status updated to {new_status}")
            return

    print(f"{company} not found")

def delete_application(applications,company):
    for application in applications:
        if application["company"] == company:
            applications.remove(application)
            print(f"{company} application deleted")
            return

    print(f"{company} not found")

def find_application(applications,company):
    for application in applications:
        if application["company"].lower() == company.lower():
            print (application["position"],application["status"])
            return application
        return None
    print(f"{company} not found")