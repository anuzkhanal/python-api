A backend for a personal TODO application that requires users to be logged in before they can call 
the APIs

The data model of a todo item & user

    Todo:
        ● Id: Unique identifier
        ● Name: Name of the todo item
        ● Description (optional): Description of the toto item
        ● User id: Id of the user who owns this todo item
        ● Created timestamp: When the item is created
        ● Updated timestamp: When the item is last updated
        ● Status: An enum of either: NotStarted, OnGoing, Completed

    User:
        ● Id: Unique identifier
        ● Email: Email address
        ● Password: Hash of the password
        ● Created timestamp: When the user is created
        ● Updated timestamp: When the user is last updated

EndPoints:

POST /api/v1/signup
POST /api/v1/signin
PUT /api/v1/changePassword
GET /api/v1/todos?status=[status]
POST /api/v1/todos
PUT /api/v1/todos/:id
DELETE /api/v1/todos/:id

All the required dependencies are in the requirement.txt

Steps to run the project

- download all code
- create Python virtual environment
    - python3 -m venv venv
    - source venv/bin/activate
- install dependencies
- migrate database
    - python manage.py makemigrations
    - python manage.py migrate
- create super user
    - python manage.py createsuperuser
- start the project 
    - python manage.py runserver


- unit testing
    - python manage.py test 
- check endpoints docs
    - http://127.0.0.1:8000/admin/
        -login using super user 
    http://127.0.0.1:8000/swagger/
        - swagger to check endpoints


