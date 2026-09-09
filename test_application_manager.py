from application_manager import (
    add_application,
    update_status,
    delete_application,
    find_application
)

def test_add_application():
    applications = []

    add_application(
        applications,
        "Google",
        "Software Engineer",
        "Applied"
    )

    assert len(applications) == 1


def test_update_status():
    applications = []

    add_application(
        applications,
        "Google",
        "Software Engineer",
        "Applied"
    )

    update_status(
        applications,
        "Google",
        "Interview"
    )

    assert applications[0]["status"] == "Interview"

def test_delete_application():
    applications = []

    add_application(
        applications,
        "Google",
        "Software Engineer",
        "Applied"
    )

    delete_application(
        applications,
        "Google"
    )

    assert len(applications) == 0

def test_find_application():
    applications = []

    add_application(
        applications,
        "Google",
        "Software Engineer",
        "Applied"
    )

    result = find_application(
        applications,
        "Google"
    )

    assert result["company"] == "Google"

 
def test_find_application_not_found():
    applications = []

    result = find_application(
        applications,
        "Google"
    )

    assert result is None