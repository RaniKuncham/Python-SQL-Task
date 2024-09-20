Project Description:** FastAPI CRUD Application for Institute Management**
This project is a FastAPI-based web application that allows users to perform CRUD (Create, Read, Update, Delete) operations on an educational institute database. The system is designed to manage institutes, courses, and students efficiently. It also provides advanced features like search functionality, a reporting system, and file handling (upload and download). The application interacts with a PostgreSQL database, and testing is facilitated using Postman APIs.

Key Features:
CRUD Operations:

Manage Institutes: Create, view, update, and delete institute records.
Manage Courses: Associate courses with institutes and perform CRUD operations.
Manage Students: Enroll students in institutes and courses, perform CRUD operations on student records.
Search Functionality:

A flexible search API that allows users to search for institutes, courses, or students by full or partial name, providing a structured JSON response with relevant records.
Report Generation:

A stored procedure that generates a report on student enrollments in various courses, broken down by month and year.
The report provides insights into student registration trends across different institutes and courses.
File Handling:

Photo Upload API: Allows users to upload and save student photos to the server using file upload capabilities.
ID Card Download API: Generates a student ID card in PDF format, including details such as the student’s name, course, institute, photo, and joining date.
Tech Stack:
Backend: FastAPI (Python)
Database: PostgreSQL (with SQLAlchemy ORM)
Data Validation: Pydantic
Testing: Postman API tests for endpoints
Project Structure:
FastAPI Backend: The backend is built using FastAPI, a modern web framework that provides asynchronous support and automatic generation of OpenAPI documentation.
Database Integration: SQLAlchemy is used for ORM-based interaction with the PostgreSQL database.
Stored Procedures: A PostgreSQL stored procedure is created to handle the generation of a monthly student enrollment report.
File Management: The application supports file upload (student photos) and PDF generation (student ID cards) with specified parameters.
API Endpoints:
Institute API:

POST /institute/: Create a new institute.
GET /institute/{id}: Retrieve an institute by ID.
PUT /institute/{id}: Update institute details.
DELETE /institute/{id}: Delete an institute.
Course API:

POST /course/: Create a new course.
GET /course/{id}: Retrieve a course by ID.
PUT /course/{id}: Update course details.
DELETE /course/{id}: Delete a course.
Student API:

POST /student/: Enroll a new student.
GET /student/{id}: Retrieve student details by ID.
PUT /student/{id}: Update student details.
DELETE /student/{id}: Delete a student.
POST /student/upload-photo/: Upload a student’s photo.
GET /student/download-id/: Download a student’s ID card as a PDF.
Search API:

GET /search?query={search_term}: Perform a full or partial text search across institute names, course names, and student names.
Report API:

GET /report/: Generate a monthly student enrollment report.
How to Run the Project:
Set Up the Environment:

Install Python dependencies using pip install -r requirements.txt.
Set up the PostgreSQL database with the provided schema.
Run the FastAPI Application:

bash
Copy code
uvicorn main:app --reload
Use Postman for Testing:

A Postman collection (FastAPI-CRUD.postman_collection.json) is provided for testing all API endpoints.
Database Setup:

Ensure PostgreSQL is installed and running.
Create tables and insert data using the provided .sql scripts.
Conclusion:
This project demonstrates a comprehensive application for managing institutes, courses, and students, showcasing the use of FastAPI for RESTful APIs, SQLAlchemy for database interaction, and file handling for both uploads and downloads. The application is flexible, scalable, and easy to maintain, making it suitable for educational institutions or training centers.






