# -- Create tables
create_student_table = """
CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
"""

create_course_table = """
CREATE TABLE Course (
    course_id INTEGER PRIMARY KEY,
    department TEXT,
    course_number INTEGER,
    course_name TEXT,
    semester TEXT,
    year INTEGER
);
"""

create_enrollment_table = """
CREATE TABLE Enrollment (
    student_id INTEGER,
    course_id INTEGER,
    grade REAL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
"""

create_category_table = """
CREATE TABLE Category (
    category_id INTEGER PRIMARY KEY,
    course_id INTEGER,
    name TEXT,
    weight REAL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
"""

create_assignment_table = """
CREATE TABLE Assignment (
    assignment_id INTEGER PRIMARY KEY,
    category_id INTEGER,
    name TEXT,
    due_date TEXT,
    total_points REAL,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);
"""

create_grade_table = """
CREATE TABLE Grade (
    student_id INTEGER,
    assignment_id INTEGER,
    points_earned REAL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (assignment_id) REFERENCES Assignment(assignment_id)
);
"""

# -- Insert values

insert_into_student_table_1 = """
INSERT INTO Student (student_id, first_name, last_name) VALUES (1, 'John', 'Doe');
"""
insert_into_student_table_2 = """
INSERT INTO Student (student_id, first_name, last_name) VALUES (2, 'Jane', 'Doe');
"""


insert_into_course_table_1 = """
INSERT INTO Course (course_id, department, course_number, course_name, semester, year) VALUES (1, 'CS', 101, 'Introduction to Computer Science', 'Fall', 2022);
"""
insert_into_course_table_2 = """
INSERT INTO Course (course_id, department, course_number, course_name, semester, year) VALUES (2, 'MATH', 101, 'Calculus I', 'Fall', 2022);
"""


insert_into_enrollment_table_1 = """
INSERT INTO Enrollment (student_id, course_id, grade) VALUES (1, 1, 10);
"""
insert_into_enrollment_table_2 = """
INSERT INTO Enrollment (student_id, course_id, grade) VALUES (1, 2, 10);
"""
insert_into_enrollment_table_3 = """
INSERT INTO Enrollment (student_id, course_id, grade) VALUES (2, 1, 10);
"""


insert_into_category_table_1 = """
INSERT INTO Category (category_id, course_id, name, weight) VALUES (1, 1, 'Participation', 0.1);
"""
insert_into_category_table_2 = """
INSERT INTO Category (category_id, course_id, name, weight) VALUES (2, 1, 'Homework', 0.2);
"""
insert_into_category_table_3 = """
INSERT INTO Category (category_id, course_id, name, weight) VALUES (3, 1, 'Tests', 0.5);
"""
insert_into_category_table_4 = """
INSERT INTO Category (category_id, course_id, name, weight) VALUES (4, 1, 'Projects', 0.2);
"""


insert_into_assignment_table_1 = """
INSERT INTO Assignment (assignment_id, category_id, name, due_date, total_points) VALUES (1, 2, 'Homework 1', '2022-09-01', 10);
"""
insert_into_assignment_table_2 = """
INSERT INTO Assignment (assignment_id, category_id, name, due_date, total_points) VALUES (2, 2, 'Homework 2', '2022-09-08', 10);
"""
insert_into_assignment_table_3 = """
INSERT INTO Assignment (assignment_id, category_id, name, due_date, total_points) VALUES (3, 3, 'Test 1', '2022-09-15', 100);
"""
insert_into_assignment_table_4 = """
INSERT INTO Assignment (assignment_id, category_id, name, due_date, total_points) VALUES (4, 4, 'Project 1', '2022-09-22', 50);
"""


insert_into_grade_table_1 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 1, 9);
"""
insert_into_grade_table_2 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 2, 8);
"""
insert_into_grade_table_3 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 3, 85);
"""
insert_into_grade_table_4 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (1, 4, 45);
"""
insert_into_grade_table_5 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (2, 1, 10);
"""
insert_into_grade_table_6 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (2, 2, 9);
"""
insert_into_grade_table_7 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (2, 3, 90);
"""
insert_into_grade_table_8 = """
INSERT INTO Grade (student_id, assignment_id, points_earned) VALUES (2, 4, 48);
"""