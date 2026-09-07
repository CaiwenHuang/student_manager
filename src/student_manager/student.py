class Student:
    def __init__(self, name, age, student_id):

        if age <= 0:
            raise ValueError("年龄必须大于0")

        self.name = name
        self.age = age
        self.student_id = student_id

    def to_dict(self):
        return {"name": self.name, "age": self.age, "student_id": self.student_id}

    def __str__(self):
        return f"学号:{self.student_id}, " f"姓名:{self.name}, " f"年龄:{self.age}"
