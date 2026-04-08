# 1. Designing a RESTful API Endpoint

## **Base URL: /api/v1/users** 

## Endpoints Overview

| Action          | Method | Endpoint      | Description      |
| --------------- | ------ | ------------- | ---------------- |
| Get all users   | GET    | `/users`      | Fetch all users  |
| Get single user | GET    | `/users/{id}` | Fetch user by ID |
| Create user     | POST   | `/users`      | Create new user  |
| Update user     | PUT    | `/users/{id}` | Replace user     |
| Delete user     | DELETE | `/users/{id}` | Delete user      |

-----

# 2. Request & Response Payloads

## Create User (POST /users)

- **/api/v1/users**

### Request Body

{
  "id": 1,
  "name": "Rahul"
}

### Response (201 Created)

{
  "id": 1,
  "name": "Rahul"
}



## Get User (GET /users/{id})

- **/api/v1/users/1**


### Response (200 OK)

{
  "id": 1,
  "name": "Rahul"
}


## Update User (PUT /users/{id})

- - **/api/v1/users/1**

### Request Body

{
  "id": 1,
  "name": "Rahul"
}

### Response (200 OK)

{
  "message": "User updated successfully"
}

## Delete User (DELETE /users/{1})

### Response (204 No Content)

(no body)



-----

# 3. Naming Convention for REST Resources

## General Rules

* Use plural nouns → /users, /orders
* Use lowercase
* Use hyphens (-) for readability → /user-profiles
* Avoid verbs → use HTTP methods instead

| Operation     | Method | Endpoint      | 
| ------------- | ------ | ------------- | 
| Get all users | GET    | `/users`      | 
| Get one user  | GET    | `/users/{id}` | 
| Create user   | POST   | `/users`      | 
| Update user   | PUT    | `/users/{id}` | 
| Delete user   | DELETE | `/users/{id}` | 


### Bad Examples (Avoid These)

| Bad Endpoint      | Problem                 |
| ----------------- | ----------------------- |
| `/getUsers`       | Uses verb               |
| `/createUser`     | Not RESTful             |
| `/deleteUserById` | Too verbose             |
| `/user`           | Singular (inconsistent) |


### Good Examples

| Good Endpoint       | Why               |
| ------------------- | ----------------- |
| `/users`            | Clean collection  |
| `/users/123`        | Specific resource |
| `/users/123/orders` | Nested resource   |









