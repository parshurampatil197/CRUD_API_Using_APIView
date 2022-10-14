## Student_api using APIView class

I have created REST API in Django Using DRF. created the class-based view. We will use the APIView class, a subclass of Django's View class. 
We can define the get(), post(), patch(), and delete() methods so that we can perform the CRUD operations.


## Requirements

Last tested successfully with Python 3.6.19 and Ubuntu 16.04.\
Django==2.2\
djangorestframework==3.10.2

[Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).

[DRF](https://github.com/gitgik/django-rest-api/blob/master/www.django-rest-framework.org): A powerful and flexible toolkit for building Web APIs


## Quick Setup

1. Create a folder for your project on your local machine
```bash
  mkdir myproject; 
  cd myproject

```

2. Create a virtual environment and install django

```bash
  virtualenv venv --python=python3; 
  source venv/bin/activate; 

```

Install the dependencies needed to run the app:
```bash
  pip install -r requirements. txt 

```

3. Download this project template from GitHub
```bash
  git clone https://github.com/parshurampatil197/Student_api.git
  cd Student_api

```

4. Initialize the database

```bash
  python manage.py makemigrations
  python manage.py migrate

```




Run the project

```bash
  python manage.py runserver

```






## API Reference
 
Test API by Using POSTMAN
#### Http request: POST 

```http
  http://127.0.0.1:8000/api/crud/
```

#### Request

```http
{
    "first_name": "parikshit",
    "last_name": "patil",
    "address": "akola",
    "roll_number": 1,
    "mobile": "123445"
}
```
#### Http request: GET 

```http
  http://127.0.0.1:8000/api/crud/
```

#### Response

```http
{
    "id": 1,
    "first_name": "parikshit",
    "last_name": "patil",
    "address": "akola",
    "roll_number": 1,
    "mobile": "123445"
}
```

```http
  http://127.0.0.1:8000/api/crud/2/
```


#### Http request: PATCH 

```http
  http://127.0.0.1:8000/api/crud/1/
```

#### Request

```http
{
    "address": "pune",
}
```

#### Http request: DELETE 

```http
  http://127.0.0.1:8000/api/crud/1/
```

## Authors

- [@parshuram](https://github.com/parshurampatil197)


