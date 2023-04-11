change_percentages_of_categories_for_course = """
UPDATE Category
SET weight = 0.4
WHERE course_id = 1 AND name = 'Tests';
"""