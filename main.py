from application_manager import (
    VALID_STATUSES,
    add_application,
    list_applications,
    update_status,
    delete_application,
    find_application
)

from database import create_table


def add_application_from_input():
    company = input("Company: ")
    position = input("Position: ")
    status = input("Status: ")

    if status not in VALID_STATUSES:
        print("Invalid status.")
        return

    add_application(company, position, status)

    print("Application added successfully!")


def show_applications():
    applications = list_applications()

    if not applications:
        print("No applications found.")
        return

    print()

    for application in applications:
        print(
            f"ID: {application[0]} | "
            f"Company: {application[1]} | "
            f"Position: {application[2]} | "
            f"Status: {application[3]}"
        )


def update_application_status():
    try:
        application_id = int(input("Application ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    new_status = input("New status: ")

    if new_status not in VALID_STATUSES:
        print("Invalid status.")
        return

    application = find_application(application_id)

    if application is None:
        print("Application not found.")
        return

    update_status(application_id, new_status)

    print("Application status updated successfully!")


def delete_application_from_input():
    try:
        application_id = int(input("Application ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    application = find_application(application_id)

    if application is None:
        print("Application not found.")
        return

    delete_application(application_id)

    print("Application deleted successfully!")


def find_application_from_input():
    try:
        application_id = int(input("Application ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    application = find_application(application_id)

    if application is None:
        print("Application not found.")
    else:
        print(
            f"ID: {application[0]} | "
            f"Company: {application[1]} | "
            f"Position: {application[2]} | "
            f"Status: {application[3]}"
        )


create_table()


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

    elif choice == "2":
        show_applications()

    elif choice == "3":
        update_application_status()

    elif choice == "4":
        delete_application_from_input()

    elif choice == "5":
        print("Goodbye!")
        break

    elif choice == "6":
        find_application_from_input()

    else:
        print("Invalid option.")