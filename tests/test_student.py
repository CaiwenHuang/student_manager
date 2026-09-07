from student_manager.student import Student


def test_create_student():

    student = Student("张三", 18, "001")

    assert student.name == "张三"
    assert student.age == 18
    assert student.student_id == "001"
