add_2_points_to_score_of_each_student_on_assignment = """
UPDATE Grade
SET points_earned = points_earned + 2
WHERE assignment_id = 1;
"""