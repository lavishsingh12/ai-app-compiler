def repair_schema(schema, errors):

    repairs = []

    for error in errors:

        if error == "Contacts page exists but Contacts API missing":

            schema["api_schema"]["endpoints"].append(
                "/contacts"
            )

            repairs.append(
                "Added /contacts endpoint"
            )

        if error == "Payments page exists but Payments API missing":

            schema["api_schema"]["endpoints"].append(
                "/payments"
            )

            repairs.append(
                "Added /payments endpoint"
            )

    return schema, repairs