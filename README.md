
# ** Developed BY: Avinash Kumar Gaurav ** 
## * Django Rest Framework: Create Update Delete Users Api *

### Note** POSTMAN Collection is also added to directly access(first run app)

## ** Create Virtual Env if not, virtual env is already include as avinash_virtual
```
- [Linux] To activate Virtual env (After cloning the code):
    - cd folder name
    - source ./avinash_virtual/bin/activate
```
```
- To Run Code:
    - cd ./accounts
    - python3 manage.py runserver
```
```
- Access application at [Django app](http://localhost:8000/api/v1/users/)
- Admin @ http://localhost:8000/admin/
```
- 1. Operation: Create User, Method: POST
- http://localhost:8000/api/v1/users/
- payload:
    - ex:
    ```
      {
        "first_name": "Black",
        "last_name": "widow",
        "email": "blackwidow@xyz.com",
        "mobile": 1234567856,
        "password": "Enter ur password"
     }
     ** Note** Mobile Number and email must be unique
     ```
- 2. Operation: Update User, Method: PUT
- http://localhost:8000/api/v1/users/<id>
    - ex: http://localhost:8000/api/v1/users/6/
- payload:
    - ex:
    ```
      {
        "id": 6,
        "first_name": "MrAvinash Kumar",
        "last_name": "Gaurav",
        "email": "nothingtoloose719@xyz.com",
        "mobile": 88958353364,
        "password": "<Enter UR Password>"
    }
     ** Note** id in url and payload must be same
     ```
- 3. Operation: Delete User, Method: DELETE
- http://localhost:8000/api/v1/users/<id>
    - ex: http://localhost:8000/api/v1/users/6/
- payload:
    - not needed using query string param
     ** Note** id in url should be populated for delete
     ```
- 4. Operation: GET All user , Method: GET
- http://localhost:8000/api/v1/users/
- payload:
    - None

- 4. Operation: GET user by id , Method: GET
- http://localhost:8000/users/api/v1/<ID>
    - ex: http://localhost:8000/api/v1/users/1/
- payload:
    - None

```
