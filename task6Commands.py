list_of_all_students_in_course_and_scores_on_every_assignment = """
SELECT Student.name, Assignment.name, Grade.points_earned
FROM Student
JOIN Enrollment ON Student.student_id = Enrollment.student_id
JOIN Course ON Enrollment.course_id = Course.course_id
JOIN Category ON Course.course_id = Category.course_id
JOIN Assignment ON Category.category_id = Assignment.category_id
JOIN Grade ON Student.student_id = Grade.student_id AND Assignment.assignment_id = Grade.assignment_id
WHERE Course.course_id = 1;
"""