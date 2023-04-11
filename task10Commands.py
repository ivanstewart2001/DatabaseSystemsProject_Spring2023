add_2_points_to_last_name_q = """
UPDATE Grade
SET points_earned = points_earned + 2
WHERE student_id IN (
    SELECT student_id
    FROM Student
    WHERE last_name LIKE '%Q%'
);
"""