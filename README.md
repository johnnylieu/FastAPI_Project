# FastAPI Team Management API

This FastAPI project allows you to manage a team by performing CRUD (Create, Read, Update, Delete) operations on team members.

## Features

-   **Create** a new team member
-   **Read** all team members, or retrieve a specific member by ID or name
-   **Update** a team member by ID
-   **Delete** a team member by ID

## Requirements

-   Python 3.x installed on your machine.
-   FastAPI and Uvicorn installed in your virtual environment.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate Virtual Environment

#### On Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

Once the virtual environment is activated, install the required packages using `pip`:

```bash
pip install fastapi uvicorn
```

## Running the Application

After installing the dependencies, you can run the FastAPI application using `uvicorn`:

```bash
uvicorn main:app --reload
```

-   The app will be available at `http://127.0.0.1:8000`
-   To access the interactive API docs, go to `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint            | Description                |
| ------ | ------------------- | -------------------------- |
| POST   | `/team/`            | Create a new team member   |
| GET    | `/team/`            | Get all team members       |
| GET    | `/team/{member_id}` | Get a team member by ID    |
| GET    | `/team/name/{name}` | Get a team member by name  |
| PUT    | `/team/{member_id}` | Update a team member by ID |
| DELETE | `/team/{member_id}` | Delete a team member by ID |
