class UserManagerSchemas:
    register = {
        "type": "object",
        "properties": {
            "password":                 {"type": "string"},
            "autoGeneratePassword":     {"type": "boolean"},
            "changePassword":           {"type": "boolean"},
            "fname":                    {"type": "string"},
            "lname":                    {"type": "string"},
            "blockLogin":               {"type": "boolean"},
            "blockLoginReason":         {"type": "string"},
            "email":                    {"type": "string"},
            "storageQuota":             {"type": "string"},
            "quotaGroup":               {"type": "string"}
        },
        "required": ["autoGeneratePassword", "email"]
    }