def validate_schema(schema):

    errors = []

    ui_pages = schema["ui_schema"]["pages"]
    api_endpoints = schema["api_schema"]["endpoints"]
    db_tables = schema["db_schema"]["tables"]
    roles = schema["auth_schema"]["roles"]

    if not ui_pages:
        errors.append("Missing UI pages")

    if not api_endpoints:
        errors.append("Missing API endpoints")

    if not db_tables:
        errors.append("Missing DB tables")

    if not roles:
        errors.append("Missing roles")

    # Cross-layer validation

    if "Contacts" in ui_pages and "/contacts" not in api_endpoints:
        errors.append("Contacts page exists but Contacts API missing")

    if "Payments" in ui_pages and "/payments" not in api_endpoints:
        errors.append("Payments page exists but Payments API missing")

    return errors