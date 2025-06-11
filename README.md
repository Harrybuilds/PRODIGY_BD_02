# PRODIGY_BD_02

## Django Rest API with Persistent Storage with Database Integration

** Task **

'''
Extend the previous REST API to use a relational database(e.g., MYSQL, MongoDB) for persistent storage

- Integrate a SQL or NoSQL  database using an ORM/ODM
- Use database migtrations if required to create the users table with the appropraite schema
- Implement connection pooling and environment-specific configurations using .env files
- Use environment variables for database credentials.
'''

*previous task*

# PRODIGY_BD_01
## Basic REST API with CRUD Operations

*TASK*
"
Create an API with endpoints to perform basic CRUD (Create, Read, Update Delete)
operations on a user's resource

- Each user should have fields: id(UUID), name, email and age
- Use an in-memory data structure (like an hashmap) for storage
- Ensure proper status code and error handling (e.g., 404 for not found, 400 for bad requests)
- include basic input validation (e.g., checking if email is valid)
"


## Requirement
 - Python 3.8+
 - MYSQL Server
 - pip (pythonpackage manager)

------

##  Setup Instruction

### 1. clone the repository
```bash
git clone https://github.com/yourusername/persistant_storage.git
cd persistant_storage ```



## Features

    - Full CRUD operations on User
    - Uses MYSQL as a relational database
    - Persistent storage with ORM (Django ORM)
    - Environment-specific configurations using `.env`
    - Secure handling of database credentials
    - Connection pooling(MYSQL)
    - Input validation and Error handling
    - UUID as primary key for users


------

## Example API Endpoints

Method          Endpoint                    Description
POST            /storage/user/              Creates a new user
GET             /storage/users/             Gets all users
GET             /storage/user/<str:id>/     Get a single user
PUT             /storage/user/<str:id>/     Update a user
DELET           /storage/user/<str:id>/     Delete a user

-------

# Tools Used
*Django 5.x
*MYSQL 8+
*Python Decouple
*mysqlclient