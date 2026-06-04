def simulate_execution(schema):

    pages = len(
        schema["ui_schema"]["pages"]
    )

    apis = len(
        schema["api_schema"]["endpoints"]
    )

    tables = len(
        schema["db_schema"]["tables"]
    )

    roles = len(
        schema["auth_schema"]["roles"]
    )

    return {
        "status": "SUCCESS",
        "application_ready": True,
        "pages": pages,
        "apis": apis,
        "tables": tables,
        "roles": roles
    }