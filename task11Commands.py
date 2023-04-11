compute_grade_for_student = """
    SELECT AVG(points_earned / total_points) * weight
    FROM Grade
    JOIN Assignment ON Grade.assignment_id = Assignment.assignment_id
    JOIN Category ON Assignment.category_id = Category.category_id
    WHERE Grade.student_id = 1;
"""