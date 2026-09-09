from storage import save_applications, load_applications
from application_manager import (
    VALID_STATUSES,
    add_application,
    list_applications,
    update_status,
    delete_application,
    find_application
)

applications = []



#for application in applications:
    #print(application)




def add_application_from_input():
    company = input("Company: ")
    position = input("Position: ")
    status = input("Status: ")

    if status not in VALID_STATUSES:
        print("Invalid status.")
        return

    add_application(applications,company, position, status)

    print("Application added successfully!")





applications = load_applications()

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
    print("6. Find")

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_application_from_input()
        save_applications(applications)

    elif choice == "2":
        list_applications(applications)

    
    elif choice == "3":
        company = input("Company: ")
        new_status = input("New status: ")


        update_status(applications, company, new_status)
        save_applications(applications)

    elif choice == "4":
        company = input("Company: ")

        delete_application(applications, company)
        save_applications(applications)

    elif choice == "6":
        company = input("Company: ")

        find_application(applications, company)
        
    elif choice == "5":
        print("Goodbye!")

        break
    else:
        print("Invalid option.")

