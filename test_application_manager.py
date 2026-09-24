import os
import pytest

os.environ["DB_NAME"] = "test_applications.db"

from database import (
    create_table,
    add_application as db_add_application,
    list_applications as db_list_applications,
    update_status as db_update_status,
    delete_application as db_delete_application,
    find_application as db_find_application
)


@pytest.fixture
def setup_database():
    create_table()

    from database import get_connection

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM applications")

    connection.commit()
    connection.close()


def test_add_application(setup_database):
    db_add_application(
        "Tesla",
        "Software Engineer",
        "Applied"
    )

    applications = db_list_applications()

    assert len(applications) == 1
    assert applications[0][1] == "Tesla"
    assert applications[0][2] == "Software Engineer"
    assert applications[0][3] == "Applied"


def test_find_application(setup_database):
    db_add_application(
        "Apple",
        "Backend Developer",
        "Saved"
    )

    applications = db_list_applications()
    application_id = applications[0][0]

    result = db_find_application(application_id)

    assert result is not None
    assert result[1] == "Apple"


def test_update_status(setup_database):
    db_add_application(
        "Google",
        "Python Developer",
        "Saved"
    )

    applications = db_list_applications()
    application_id = applications[0][0]

    db_update_status(application_id, "Interview")

    result = db_find_application(application_id)

    assert result[3] == "Interview"


def test_delete_application(setup_database):
    db_add_application(
        "Microsoft",
        "Software Engineer",
        "Applied"
    )

    applications = db_list_applications()
    application_id = applications[0][0]

    db_delete_application(application_id)

    result = db_find_application(application_id)

    assert result is None