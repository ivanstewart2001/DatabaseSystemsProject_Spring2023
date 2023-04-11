compute_grade_for_student_with_lowest_score_dropped = """
    WITH MinGrade AS (
        SELECT MIN(points_earned / total_points) AS min_grade
        FROM Grade
        JOIN Assignment ON Grade.assignment_id = Assignment.assignment_id
        JOIN Category ON Assignment.category_id = Category.category_id
        WHERE Grade.student_id = 1
    )
    SELECT AVG(points_earned / total_points) * weight
    FROM Grade
    JOIN Assignment ON Grade.assignment_id = Assignment.assignment_id
    JOIN Category ON Assignment.category_id = Category.category_id
    WHERE Grade.student_id = 1 AND points_earned / total_points > (SELECT min_grade FROM MinGrade);
"""