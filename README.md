# FastAPI Student Management API

This is a FastAPI-based project that provides an API for managing student records. It includes database integration, data validation, and structured routes for handling student-related operations.

## Features
- FastAPI framework for efficient and scalable API development
- CRUD operations for student management
- Database integration for persistent storage
- Pydantic schemas for data validation

## Installation

1. Clone the repository:
   ```sh
   git clone <https://github.com/Chandaluri-Lokesh/FastAPI>
   cd Fastapi
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database (modify `config/db.py` as needed).

5. Run the application:
   ```sh
   uvicorn index:app --reload
   ```

6. Access the API documentation at:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure
```
Fastapi/
│── index.py            # Main application file
│── config/
│   ├── db.py           # Database configuration
│── models/
│   ├── student.py      # Student model definition
│── routes/
│   ├── student.py      # API routes for students
│── schemas/
│   ├── student.py      # Pydantic schemas for data validation
│── requirements.txt    # Required dependencies
```

## API Endpoints

- `GET /students` - Retrieve all students
- `POST /students` - Add a new student
- `GET /students/{id}` - Retrieve a student by ID
- `PUT /students/{id}` - Update a student by ID
- `DELETE /students/{id}` - Delete a student by ID

## License
This project is licensed under the MIT License.

