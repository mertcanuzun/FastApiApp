# FastApiApp
FastAPI CRUD API

  This project provides a CRUD (Create, Read, Update, Delete) API built using FastAPI. It exposes endpoints for managing users, tasks, notes, books, and posts, along with authentication      endpoints for login and logout.

  Requirements :  refers to the aggregate of features or specifications used to determine the functionality of a software in Python programming.
  Python v 3.12 
  FastAPI : FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
  uvicorn : Uvicorn is an ASGI server used to run ASGI (Asynchronous Server Gateway Interface) compliant web servers in Python.
  pydantic: Pydantic is a library used for data validation and structure definition in Python.


Installation: 

  Clone the repository: https://github.com/mertcanuzun/FastApiApp.git

Usage: 

  Run the FastAPI server: uvicorn main:app --host 127.0.0.1 --port 8000
  Once the server is running, you can access the API documentation at http://127.0.0.1:8000/docs.

Endpoints: 

  Users: CRUD operations for managing users.
  Tasks: CRUD operations for managing tasks.
  Notes: CRUD operations for managing notes.
  Books: CRUD operations for managing books.
  Posts: CRUD operations for managing posts.
  Authentication: Endpoints for user login and logout.
  
API Documentation:

  The API documentation is automatically generated by FastAPI and can be accessed at http://127.0.0.1:8000/docs when the server is running.

