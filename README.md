# Job Application Tracker

A command-line job application tracking system built with Python and SQLite.

This project helps users manage job applications by recording companies,
positions, application statuses, and application IDs.

## Features

- Add a job application
- List all job applications
- Find an application by ID
- Update application status
- Delete an application
- Store data persistently using SQLite
- Validate application statuses
- Automated tests using pytest

## Technologies

- Python 3
- SQLite
- pytest
- Git

## Project Structure

```text
job-application-tracker/
├── main.py
├── application_manager.py
├── database.py
├── test_application_manager.py
├── README.md
└── .gitignore


Application Statuses

The supported application statuses are:

Saved

Applied

Interview

Rejected

Offer

Withdrawn

How to Run
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd job-application-tracker
2. Run the application
python main.py

The program will automatically create the SQLite database table if it does not already exist.

3. Run tests
pytest -v
Example
================================
   Job Application Tracker
================================
1. Add application
2. List applications
3. Update status
4. Delete application
5. Exit
6. Find

Choose an option: 1
Company: Tesla
Position: Software Engineer
Status: Applied

Application added successfully!
What I Learned

How to organize a Python project into multiple modules

How to use SQLite for persistent data storage

How to write SQL queries with parameters

How to use pytest for automated testing

How to use Git for version control

How to separate user interface, business logic, and database operations

Future Improvements

Add a FastAPI REST API

Add filtering by application status

Add search by company name

Add application dates

Add a web interface

Add Docker support
```
