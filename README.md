# User Management API
## Table of Contents
- [Project Description](#project-description)
    - [Key Features](#key-features)
- [API Endpoints](#api-endpoints)
- [User Table](#user-table)

## Project Description

The **User Management API** is a lightweight, container-ready RESTful service built with Python and Flask. It provides a simple yet extensible backend for managing user accounts in modern web or mobile applications.

This API allows clients to create, read, update, delete, block, and unblock users via intuitive HTTP endpoints. Designed for clarity and scalability, it uses SQLite as the default database and follows clean architectural practices with a modular codebase.

### Key features:
- Fully RESTful design with standard HTTP methods
- Structured database model with basic user metadata

## API Endpoints
| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| GET    | `/users`             | Retrieve a list of all users         |
| GET    | `/users/<id>`        | Retrieve a single user by ID         |
| POST   | `/users`             | Create a new user                    |
| PUT    | `/users/<id>`        | Update an existing user's data       |
| DELETE | `/users/<id>`        | Delete a user                        |
| PATCH  | `/users/<id>/block`  | Block or unblock a specific user     |

## User Table
| Column       | Type    | Constraints      | Description                    |
| ------------ | ------- | ---------------- | ------------------------------ |
| `id`         | Integer | Primary Key      | Unique identifier for the user |
| `username`   | String  | Unique, Not Null | Username (must be unique)      |
| `email`      | String  | Not Null         | User's email address           |
| `is_blocked` | Boolean | Default: `false` | Indicates if user is blocked   |
