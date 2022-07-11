class UserManagerSchemas:
    register = {
        "type": "object",
        "properties": {
            "password":                 {"type": "string"},
            "fname":                    {"type": "string"},
            "lname":                    {"type": "string"},
            "blockLogin":               {"type": "boolean"},
            "blockLoginReason":         {"type": "string"},
            "email":                    {"type": "string"},
        },
        "required": ["password", "email"]
    }