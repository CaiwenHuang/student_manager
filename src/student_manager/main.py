from student_manager.manager import StudentManager
from student_manager.student import Student


def get_valid_age():
    while True:
        try:
            age = int(input("请输入年龄: "))
            return age
        except ValueError:
            print("年龄必须输入数字")


def main():

    manager = StudentManager()

    while True:

        print("""
====================
学生管理系统
====================

1. 添加学生
2. 查看学生
3. 删除学生
4. 修改学生
5. 退出

        """)

        choice = input("请选择:")

        if choice == "1":

            student_id = input("学号:")
            name = input("姓名:")
            age = get_valid_age()

            try:

                student = Student(name, age, student_id)
                success = manager.add_student(student)

                if success:
                    print("添加成功")

            except ValueError as e:

                print(e)

        elif choice == "2":

            manager.show_students()

        elif choice == "3":

            student_id = input("输入删除学生学号:")

            manager.delete_student(student_id)

        elif choice == "4":

            student_id = input("输入修改学生学号:")

            name = input("新姓名:")

            age = get_valid_age()

            manager.update_student(student_id, name, age)

        elif choice == "5":

            manager.save()

            print("数据已保存，退出系统")

            break

        else:

            print("输入错误")


if __name__ == "__main__":
    main()
