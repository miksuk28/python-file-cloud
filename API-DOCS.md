# Python File Cloud (working title) API Documentation

## Headers
```token: <valid token>```

**NOTE: Unless explicitly stated, all requests must contain a valid token header. On authentication failure, returns 403 ACCESS DENIED**

## Generic API Errors
### 400 BAD REQUEST - Missing Token: 
```json
{
    "error":   "Access Denied",
    "message": "No token header"
}
```
### 400 BAD REQUEST - JSON Validation Error: 
```json
{
    "error":            "JSON validation error",
    "errorMessage":     <JSONScema Error Message>,
    "expectedSchema":   <schema>
}
```

### 401 UNAUTHORIZED - Invalid token:
```json
{
    "error":   "Access Denied",
    "message": "Supplied token is invalid. Please sign in again"
}
```

### 405 METHOD NOT ALLOWED
```json
{
    "error": "Method not allowed for this endpoint"
}
```

# User Management
## Get User Info
### ```GET /user/<username>```

### Responses:
200 OK
```json
{
    "username":                     {"type": "string"},
    "password":                     {"type": "string"},
    "autoGeneratePassword":         {"type": "boolean"},
    "changePasswordOnFirstLogin":   {"type": "boolean"},
    "fname":                        {"type": "string"},
    "lname":                        {"type": "string"},
    "blockLogin":                   {"type": "boolean"},
    "blockLoginReason":             {"type": "string"},
    "email":                        {"type": "string"}
}
```

404 NOT FOUND
```json
{
    "error": "User with username <username> does not exist"
}
```


## Create New user
### ```POST /user/<username>```
#### Expected Schema:
```json
{
    "username":                     {"type": "string"},
    "password":                     {"type": "string"},
    "autoGeneratePassword":         {"type": "boolean"},
    "changePasswordOnFirstLogin":   {"type": "boolean"},
    "fname":                        {"type": "string"},
    "lname":                        {"type": "string"},
    "blockLogin":                   {"type": "boolean"},
    "blockLoginReason":             {"type": "string"},
    "email":                        {"type": "string"}
}

required: ["username", "autoGeneratePassword", "email"]
```
### Responses:
201 CREATED
```json
{
    "message": "User <username> was created successfully"
}
```
409 CONFLICT
```json
{
    "error": "User <username> already exists"
}
```
409 CONFLICT - Forbidden Username
```json
{
    "error": "Username <username> is not allowed"
}
```

## Delete Single User
### ```DELETE /user/<username>```
### Responses:
200 OK
```json
{
    "message": "User <username> has been deleted"
}
```
404 NOT FOUND
```json
{
    "message": "User <username> does not exist"
}
```

## Delete Multiple Users
### ```DELETE /users```
#### Expected Schema:
```json
{
    "usersToDelete": {"type": "array"}
}

required: ["usersToDelete"]
```
### Responses:
200 OK
```json
{
    "message": "user <username> has been deleted"
}
```
404 NOT FOUND:
```json
{
    "message": "User <username> does not exist"
}
```

## Authenticate and Receive token
### ```POST /authenticate```
> This endpoint does *not* require the **token** header, as it is the one that generates it. Use this token as the *token* header for future requests to authenticate yourself
#### Expected Schema:
```json
{
    "username" : {"type" : "string"},
    "password" : {"type" : "string"}
}

required: ["username", "password"]
```

### Responses:
200 OK
```json
{
    "token": {"type": "string"},
    "exp":   {"type": "string"}
}
```
404 NOT FOUND
```json
{
    "error": "User does not exist"
}
```
403 FORBIDDEN
```json
{
    "error": "Incorrect password"
}
```