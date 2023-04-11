import sqlite3
import unittest
from task2Commands import *
from task5Commands import *
from task4Commands import *
from task7Commands import *
from task8Commands import *
from task9Commands import *
from task10Commands import *
from task11Commands import *
from task12Commands import *

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_create_student_table(self):
        self.cursor.execute(create_student_table)
        self.cursor.execute("PRAGMA table_info(Student);")
        columns = self.cursor.fetchall()
        self.assertEqual(len(columns), 3)
        self.assertEqual(columns[0][1], 'student_id')
        self.assertEqual(columns[1][1], 'first_name')
        self.assertEqual(columns[2][1], 'last_name')

    def test_create_course_table(self):
        self.cursor.execute(create_course_table)
        self.cursor.execute("PRAGMA table_info(Course);")
        columns = self.cursor.fetchall()
        self.assertEqual(len(columns), 6)
        self.assertEqual(columns[0][1], 'course_id')
        self.assertEqual(columns[1][1], 'department')
        self.assertEqual(columns[2][1], 'course_number')
        self.assertEqual(columns[3][1], 'course_name')
        self.assertEqual(columns[4][1], 'semester')
        self.assertEqual(columns[5][1], 'year')

    def test_create_enrollment_table(self):
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute("PRAGMA table_info(Enrollment);")
        columns = self.cursor.fetchall()
        self.assertEqual(len(columns), 3)
        self.assertEqual(columns[0][1], 'student_id')
        self.assertEqual(columns[1][1], 'course_id')
        self.assertEqual(columns[2][1], 'grade')

    def test_create_category_table(self):
      self.cursor.execute(create_category_table)
      self.cursor.execute("PRAGMA table_info(Category);")
      columns =self. cursor.fetchall()
      self.assertEqual(len(columns), 4)
      self.assertEqual(columns[0][1],'category_id')
      self.assertEqual(columns[1][1],'course_id')
      self.assertEqual(columns[2][1],'name')
      self.assertEqual(columns[3][1],'weight')

    def test_create_assignment_table(self):
        self.cursor.execute(create_assignment_table)
        self.cursor.execute("PRAGMA table_info(Assignment);")
        columns = self.cursor.fetchall()
        self.assertEqual(len(columns), 5)
        self.assertEqual(columns[0][1], 'assignment_id')
        self.assertEqual(columns[1][1], 'category_id')
        self.assertEqual(columns[2][1], 'name')
        self.assertEqual(columns[3][1], 'due_date')
        self.assertEqual(columns[4][1], 'total_points')

    def test_create_grade_table(self):
        self.cursor.execute(create_grade_table)
        self.cursor.execute("PRAGMA table_info(Grade);")
        columns = self.cursor.fetchall()
        self.assertEqual(len(columns), 3)
        self.assertEqual(columns[0][1], 'student_id')
        self.assertEqual(columns[1][1], 'assignment_id')
        self.assertEqual(columns[2][1], 'points_earned')

    def test_insert_into_student_table(self):
        self.cursor.execute(create_student_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute("SELECT * FROM Student;")
        row = self.cursor.fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(row[1], 'John')
        self.assertEqual(row[2], 'Doe')

    def test_insert_into_course_table(self):
        self.cursor.execute(create_course_table)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute("SELECT * FROM Course;")
        row = self.cursor.fetchone()
        self.assertEqual(row[1], 'CS')
        self.assertEqual(row[2], 101)
        self.assertEqual(row[3], 'Introduction to Computer Science')
        self.assertEqual(row[4], 'Fall')
        self.assertEqual(row[5], 2022)

    def test_insert_into_enrollment_table(self):
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_enrollment_table_1)

        self.cursor.execute("SELECT * FROM Enrollment;")
        row = self.cursor.fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(row[1], 1)
        self.assertEqual(row[2], 10)

    def test_insert_into_category_table(self):
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)

        self.cursor.execute("SELECT * FROM Category;")
        row = self.cursor.fetchone()
        self.assertEqual(row[1], 1)
        self.assertEqual(row[2], 'Homework')
        self.assertEqual(row[3], 0.2)

    def test_insert_into_assignment_table(self):
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)

        self.cursor.execute("SELECT * FROM Assignment;")
        row = self.cursor.fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(row[1], 2)
        self.assertEqual(row[2], 'Homework 1')
        self.assertEqual(row[3], '2022-09-01')
        self.assertEqual(row[4], 10)

    def test_insert_into_grade_table(self):
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_grade_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)
        self.cursor.execute(insert_into_grade_table_1)

        self.cursor.execute("SELECT * FROM Grade;")
        row = self.cursor.fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(row[1], 1)
        self.assertEqual(row[2], 9)

    def test_compute_assignment_statistics(self):
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_grade_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_student_table_2)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)
        self.cursor.execute(insert_into_grade_table_1)
        self.cursor.execute(insert_into_grade_table_5)

        # Compute average score
        self.cursor.execute(average_score)
        row =self. cursor.fetchone()
        self.assertAlmostEqual(row[0],9.5)

        # Compute highest score
        self.cursor.execute(highest_score)
        row =self. cursor.fetchone()
        self.assertEqual(row[0],10.0)

        # Compute lowest score
        self.cursor.execute(lowest_score)
        row =self. cursor.fetchone()
        self.assertEqual(row[0],9.0)

    def test_list_students_in_course(self):
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_student_table_2)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_enrollment_table_1)
        self.cursor.execute(insert_into_enrollment_table_3)

        # List students in course
        self.cursor.execute(all_students_in_given_course)
        rows =self. cursor.fetchall()
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[0][0],'John')
        self.assertEqual(rows[0][1],'Doe')
        self.assertEqual(rows[1][0],'Jane')
        self.assertEqual(rows[1][1],'Doe')

    def test_list_students_and_scores_in_course(self):
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(create_grade_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_student_table_2)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)
        self.cursor.execute(insert_into_assignment_table_2)
        self.cursor.execute(insert_into_enrollment_table_1)
        self.cursor.execute(insert_into_enrollment_table_3)

        # Test that the data was inserted correctly
        self.cursor.execute("SELECT * FROM Student;")
        students = self.cursor.fetchall()
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0], (1, 'John', 'Doe'))
        self.assertEqual(students[1], (2, 'Jane', 'Doe'))

        self.cursor.execute("SELECT * FROM Course;")
        courses = self.cursor.fetchall()
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0], (1, 'CS', 101, 'Introduction to Computer Science', 'Fall', 2022))
        
        self.cursor.execute("SELECT * FROM Category;")
        categories = self.cursor.fetchall()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0], (2, 1, 'Homework', 0.2))

        self.cursor.execute("SELECT * FROM Assignment;")
        assignments = self.cursor.fetchall()
        self.assertEqual(len(assignments), 2)
        self.assertEqual(assignments[0], (1, 2, 'Homework 1', '2022-09-01', 10))
        self.assertEqual(assignments[1], (2, 2, 'Homework 2', '2022-09-08', 10))

        self.cursor.execute("SELECT * FROM Enrollment;")
        enrollments = self.cursor.fetchall()
        self.assertEqual(len(enrollments), 2)
        self.assertEqual(enrollments[0], (1, 1, 10))
        self.assertEqual(enrollments[1], (2, 1, 10))

    def test_add_assignment_to_course(self):
        # Set up the database and insert some initial data
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(create_grade_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_student_table_2)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)

        # Test adding an assignment to a course
        self.cursor.execute(add_assignment_to_a_course)

        # Test that the assignment was added correctly
        self.cursor.execute("SELECT * FROM Assignment;")
        assignments = self.cursor.fetchall()
        self.assertEqual(len(assignments), 1)
        self.assertEqual(assignments[0], (5, 3, 'Test 2', '2022-10-15', 100))
        
    def test_change_category_percentages_for_course(self):
        # Set up the database and insert some initial data
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(create_grade_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_student_table_2)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_3)

        # Test changing the percentage of a category for a course
        self.cursor.execute(change_percentages_of_categories_for_course)

        # Test that the category percentage was updated correctly
        self.cursor.execute("SELECT * FROM Category;")
        categories = self.cursor.fetchall()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0], (3, 1, 'Tests', 0.4))

    def test_add_points_to_student_scores_on_assignment(self):
        # Set up the database and insert some initial data
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(create_grade_table)
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_student_table_2)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)

        # Insert some initial grades for the students
        insert_grade_1 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 1, 90.0);"
        insert_grade_2 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (2, 1, 80.0);"
        self.cursor.execute(insert_grade_1)
        self.cursor.execute(insert_grade_2)

        # Test adding 2 points to the score of each student on an assignment
        self.cursor.execute(add_2_points_to_score_of_each_student_on_assignment)

        # Test that the grades were updated correctly
        self.cursor.execute("SELECT * FROM Grade;")
        grades = self.cursor.fetchall()
        self.assertEqual(len(grades), 2)
        self.assertEqual(grades[0], (1, 1, 92.0))
        self.assertEqual(grades[1], (2, 1, 82.0))

    def test_add_points_to_student_scores_with_q_in_last_name(self):
        # Set up the database and insert some initial data
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(create_grade_table)

        # Insert some students with and without a 'Q' in their last name
        insert_student_1 = "INSERT INTO Student (first_name, last_name) VALUES ('John', 'Doe');"
        insert_student_2 = "INSERT INTO Student (first_name, last_name) VALUES ('Jane', 'Quincy');"
        insert_student_3 = "INSERT INTO Student (first_name, last_name) VALUES ('Bob', 'Smith');"
        self.cursor.execute(insert_student_1)
        self.cursor.execute(insert_student_2)
        self.cursor.execute(insert_student_3)

        # Insert a course, category, and assignment
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)

        # Insert some initial grades for the students
        insert_grade_1 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 1, 90.0);"
        insert_grade_2 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (2, 1, 80.0);"
        insert_grade_3 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (3, 1, 85.0);"
        self.cursor.execute(insert_grade_1)
        self.cursor.execute(insert_grade_2)
        self.cursor.execute(insert_grade_3)

        # Test adding 2 points to the score of students whose last name contains a 'Q'
        update_grades = """
            UPDATE Grade
            SET points_earned = points_earned + 2
            WHERE student_id IN (
                SELECT student_id
                FROM Student
                WHERE last_name LIKE '%Q%'
            );
        """
        self.cursor.execute(add_2_points_to_last_name_q)

        # Test that the grades were updated correctly
        self.cursor.execute("SELECT * FROM Grade;")
        grades = self.cursor.fetchall()
        self.assertEqual(len(grades), 3)
        self.assertEqual(grades[0], (1, 1, 90.0))
        self.assertEqual(grades[1], (2, 1, 82.0))
        self.assertEqual(grades[2], (3, 1, 85.0))

    def test_compute_grade_for_student(self):
        # Set up the database and insert some initial data
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(create_grade_table)

        # Insert a student, course, category, and assignments
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)
        self.cursor.execute(insert_into_assignment_table_2)

        # Insert some grades for the student
        insert_grade_1 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 1, 90.0);"
        insert_grade_2 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 2, 80.0);"
        self.cursor.execute(insert_grade_1)
        self.cursor.execute(insert_grade_2)

        # Compute the grade for the student
        compute_grade = """
            SELECT AVG(points_earned / total_points) * weight
            FROM Grade
            JOIN Assignment ON Grade.assignment_id = Assignment.assignment_id
            JOIN Category ON Assignment.category_id = Category.category_id
            WHERE Grade.student_id = 1;
        """
        self.cursor.execute(compute_grade_for_student)
        grade = self.cursor.fetchone()[0]

        # Test that the grade was computed correctly
        self.assertAlmostEqual(grade, ((90.0 / 100.0) + (80.0 / 100.0)))

    def test_compute_grade_for_student_with_lowest_score_dropped(self):
        # Set up the database and insert some initial data
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_course_table)
        self.cursor.execute(create_category_table)
        self.cursor.execute(create_assignment_table)
        self.cursor.execute(create_enrollment_table)
        self.cursor.execute(create_grade_table)

        # Insert a student, course, category, and assignments
        self.cursor.execute(insert_into_student_table_1)
        self.cursor.execute(insert_into_course_table_1)
        self.cursor.execute(insert_into_category_table_2)
        self.cursor.execute(insert_into_assignment_table_1)
        self.cursor.execute(insert_into_assignment_table_2)

        # Insert some grades for the student
        insert_grade_1 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 1, 90.0);"
        insert_grade_2 = "INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 2, 80.0);"
        self.cursor.execute(insert_grade_1)
        self.cursor.execute(insert_grade_2)

        # Compute the grade for the student with the lowest score dropped
        compute_grade = """
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
        self.cursor.execute(compute_grade)
        grade = self.cursor.fetchone()[0]

        # Test that the grade was computed correctly
        self.assertAlmostEqual(grade, (0.2 * (90.0 / 100.0))*10)
        
if __name__ == '__main__':
    unittest.main()