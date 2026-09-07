from student_manager.database import load_students, save_students


class StudentManager:

    def __init__(self):
        # 程序启动时，从文件加载学生
        self.students = load_students()

    def add_student(self, student):

        for s in self.students:

            if s.student_id == student.student_id:

                print("学号已存在")

                return False

        self.students.append(student)

        return True

    def show_students(self):

        if not self.students:
            print("暂无学生")
            return

        for student in self.students:
            print(student)

    def delete_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:

                self.students.remove(student)

                print("删除成功")
                return

        print("没有找到该学生")

    def update_student(self, student_id, name, age):

        for student in self.students:

            if student.student_id == student_id:

                student.name = name
                student.age = age

                print("修改成功")
                return

        print("没有找到该学生")

    def save(self):

        save_students(self.students)
