applications = []


def add_application(company, position, status):
    application = {
        "company": company,
        "position": position,
        "status": status
    }

    applications.append(application)


add_application(
    "Nokia",
    "Junior Software Developer",
    "Applied"
)

add_application(
    "BDO",
    "Junior Data Analyst",
    "Saved"
)


for application in applications:
    print(application)

def list_applications():
    for application in applications:
        print(
            application["company"],
            "-",
            application["position"],
            "-",
            application["status"]
        )
list_applications()