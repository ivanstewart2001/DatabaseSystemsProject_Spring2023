# -- Compute the average score of an assignment
average_score = """
SELECT AVG(points_earned) FROM Grade WHERE assignment_id = 1;
"""

# -- Compute the highest score of an assignment
highest_score = """
SELECT MAX(points_earned) FROM Grade WHERE assignment_id = 1;
"""

# -- Compute the lowest score of an assignment
lowest_score = """
SELECT MIN(points_earned) FROM Grade WHERE assignment_id = 1;
"""