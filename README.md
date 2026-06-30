# Learning-api
FASTapi project soon...
First project using FASTapi


# FastAPI Blog Application 🚀

> **Project Status:** 🚧 Under Development

A blog application built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **Jinja2 Templates**. This project is being developed as a learning project to understand modern backend development, REST APIs, asynchronous programming, and database management with FastAPI.

## Features Completed

- User Management
  - Create User
  - Get User
  - Update User
  - Delete User

- Post Management
  - Create Post
  - Get Single Post
  - Get All Posts
  - Update Post (PUT)
  - Partial Update Post (PATCH)
  - Delete Post

- HTML Pages
  - Home Page
  - Individual Post Page
  - User Posts Page

- Database
  - SQLite
  - SQLAlchemy ORM
  - One-to-Many Relationship (User → Posts)

- Async Support
  - Async SQLAlchemy
  - Async FastAPI Routes

- Error Handling
  - Custom HTML Error Pages
  - JSON Error Responses for API

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (Async)
- SQLite
- Jinja2
- Pydantic
- Uvicorn

## Project Structure

```
.
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   ├── users.py
│   └── posts.py
├── templates/
├── static/
├── media/
└── blog.db
```

## API Endpoints

### Users

- `POST /api/users`
- `GET /api/users/{user_id}`
- `PATCH /api/users/{user_id}`
- `DELETE /api/users/{user_id}`

### Posts

- `POST /api/posts`
- `GET /api/posts`
- `GET /api/posts/{post_id}`
- `PUT /api/posts/{post_id}`
- `PATCH /api/posts/{post_id}`
- `DELETE /api/posts/{post_id}`

## Running the Project

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
fastapi dev main.py
```

Visit

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

## Upcoming Features

- Authentication & Authorization
- Password Hashing
- User Login
- Image Upload
- Pagination
- Search Functionality
- Comments System
- User Profiles
- Deployment
- Docker Support
- Unit Testing

## Learning Objectives

This project is focused on learning:

- REST API Development
- FastAPI Framework
- Async Programming
- SQLAlchemy ORM
- Database Relationships
- CRUD Operations
- Template Rendering
- Backend Project Structure
- Error Handling
- API Design

---

**Note:** This project is actively under development. New features and improvements are being added regularly.