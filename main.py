from fastapi import FastAPI, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  # Instance the FastAPI object, fastapi-instance-variable


@app.get("/", status_code=status.HTTP_200_OK)
def index() -> dict:
    return {"message": "Hello World!"}


# We won't have written data into our code like the dict so to persist this data, this is when the database comes in
students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    },
    2: {
        "name": "Jane",
        "age": 14,
        "year": "year 9"
    },
    3: {
        "name": "Julia",
        "age": 16,
        "year": "year 11"
    }
}


class Student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


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
    # This is where we would return a status 404 Not Found
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


@app.delete("/student/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int):
    if student_id not in students:
        # This is where we would return a status 404 Not Found
        return {"error": "No student was found."}
    del students[student_id]
    return {"message": "Student with ID " + str(student_id) + " was successfully deleted."}


"""
Something to consider:
If the same endpoint name is used and the same method is used, like so:

@app.get("/students/{student_id}", status_code=status.HTTP_200_OK)
@app.get("/students/{age}", status_code=status.HTTP_200_OK)

even if they have different path parameters, the endpoint that will be called will be the one that was declared first,
so in this case, it would be:

@app.get("/students/{student_id}", status_code=status.HTTP_200_OK)
"""
