from fastapi import FastAPI, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  # Instance the FastAPI object

# We won't have written data into our code like the dict so to persist this data, this is when the database comes in
students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Jane",
        "age": 14,
        "class": "year 9"
    },
    3: {
        "name": "Julia",
        "age": 16,
        "class": "year 11"
    }
}


class Student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/", status_code=status.HTTP_200_OK)
def index() -> dict:
    return {"message": "Hello World!"}


@app.get("/students", status_code=status.HTTP_200_OK)
def get_students():
    return students


@app.get("/students/{student_id}", status_code=status.HTTP_200_OK)  # Path parameters
def get_student_by_id(student_id: int):
    return students[student_id]


@app.get("/students/name", status_code=status.HTTP_200_OK)  # Query parameters
def get_student_by_name(name: str):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]
    return {"error": "The student was not found."}


@app.get("/students/age/{age}", status_code=status.HTTP_200_OK)  # Both path and query parameters
def get_student_by_name_and_age(name: str, age: int):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower() and students[student_id]["age"] == age:
            return students[student_id]
    # This is where we would return a status 404 Not Found
    return {"error": "The student was not found."}


@app.post("/student", status_code=status.HTTP_201_CREATED)  # When trying this out, go to the get_students and show dict
def create_student(student: Student):
    new_id = len(students) + 1
    students[new_id] = student
    # Normally, this would only return a status 201 Created with no body so in the front end part would call another
    # action like cleaning the form or returning to the home page, etc.
    return students[new_id]


@app.put("/student/{student_id}", status_code=status.HTTP_200_OK)
def update_student(student: Student, student_id: int):
    if student_id not in students:
        # This is where we would return a status 404 Not Found
        return {"error": "No student was found."}
    students[student_id] = student
    # Normally, this would only return a status 204 No Content with no body so in the front end part would call another
    # action like cleaning the form or returning to the home page, etc.
    return students[student_id]


@app.patch("/student/{student_id}", status_code=status.HTTP_200_OK)
def update_part_of_student(student: Student, student_id: int):
    if student_id not in students:
        # This is where we would return a status 404 Not Found
        return {"error": "No student was found."}
    # I added the "string" validation because of swagger, but normally I would just leave the other two.
    if student.name != "string" and student.name is not None and student.name != "":
        students[student_id]["name"] = student.name
    if student.age is not None:
        if student.age > 0:  # Because of error TypeError: '>' not supported between instances of 'NoneType' and 'int'
            students[student_id]["age"] = student.age
    if student.year != "string" and student.year is not None and student.year != "":
        students[student_id]["year"] = student.year
    # Normally, this would only return a status 204 No Content with no body so in the front end part would call another
    # action like cleaning the form or returning to the home page, etc.
    return students[student_id]


@app.get("/student/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int):
    if student_id not in students:
        # This is where we would return a status 404 Not Found
        return {"error": "No student was found."}
    del students[student_id]
    return {"message": "Student with ID " + str(student_id) + " was successfully deleted."}
