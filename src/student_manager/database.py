import json
from pathlib import Path

from student_manager.student import Student

DATA_FILE = Path("data/students.json")


def save_students(students):

    DATA_FILE.parent.mkdir(exist_ok=True)

    data = []

    for student in students:
        data.append(
            {"student_id": student.student_id, "name": student.name, "age": student.age}
        )

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_students():

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:

        data = json.load(f)

    students = []

    for item in data:

        student = Student(item["name"], item["age"], item["student_id"])

        students.append(student)

    return students
