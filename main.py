applications = []



def add_application(company, position, status):
    application = {
        "company": company,
        "position": position,
        "status": status
    }
    applications.append(application)



#company = input("Company: ")

#position = input("Position: ")
#status = input("Status: ")


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

def update_status(company, new_status):
    for application in applications:
        if application["company"] == company:
            application["status"] = new_status
            print(f"{company} status updated to {new_status}")
            return

    print(f"{company} not found")

def delete_application(company):
    for application in applications:
        if application["company"] == company:
            applications.remove(application)
            print(f"{company} application deleted")
            return

    print(f"{company} not found")


def add_application_from_input():
    company = input("Company: ")
    position = input("Position: ")
    status = input("Status: ")
    
    if status not in VALID_STATUSES:
        print("Invalid status.")
        return

    add_application(company, position, status)

    print("Application added successfully!")

def show_menu():
    print()
    print("================================")
    print("   Job Application Tracker")
    print("================================")
    print("1. Add application")
    print("2. List applications")
    print("3. Update status")
    print("4. Delete application")
    print("5. Exit")

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_application_from_input()

    elif choice == "2":
        list_applications()

    elif choice == "5":
        print("Goodbye!")

    elif choice == "3":
        company = input("Company: ")
        new_status = input("New status: ")


        update_status(company, new_status)

    elif choice == "4":
        company = input("Company: ")

        delete_application(company)
        break

VALID_STATUSES = [
    "Saved",
    "Applied",
    "Interview",
    "Rejected",
    "Offer",
    "Withdrawn"
]