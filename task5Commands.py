all_students_in_given_course = """
SELECT Student.first_name, Student.last_name
FROM Student
JOIN Enrollment ON Student.student_id = Enrollment.student_id
WHERE Enrollment.course_id = 1;
"""