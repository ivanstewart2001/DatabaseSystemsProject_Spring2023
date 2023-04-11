import sqlite3
from task2Commands import *
import pandas as pd

conn = sqlite3.connect('GradeBook.db')
cursor = conn.cursor()

# create tables for task 2
cursor.execute(create_student_table)
cursor.execute(create_course_table)
cursor.execute(create_enrollment_table)
cursor.execute(create_category_table)
cursor.execute(create_assignment_table)
cursor.execute(create_grade_table)

# insert values for task 2
cursor.execute(insert_into_student_table_1)
cursor.execute(insert_into_student_table_2)

cursor.execute(insert_into_course_table_1)
cursor.execute(insert_into_course_table_2)

cursor.execute(insert_into_enrollment_table_1)
cursor.execute(insert_into_enrollment_table_2)
cursor.execute(insert_into_enrollment_table_3)

cursor.execute(insert_into_category_table_1)
cursor.execute(insert_into_category_table_2)
cursor.execute(insert_into_category_table_3)
cursor.execute(insert_into_category_table_4)

cursor.execute(insert_into_assignment_table_1)
cursor.execute(insert_into_assignment_table_2)
cursor.execute(insert_into_assignment_table_3)
cursor.execute(insert_into_assignment_table_4)

cursor.execute(insert_into_grade_table_1)
cursor.execute(insert_into_grade_table_2)
cursor.execute(insert_into_grade_table_3)
cursor.execute(insert_into_grade_table_4)
cursor.execute(insert_into_grade_table_5)
cursor.execute(insert_into_grade_table_6)
cursor.execute(insert_into_grade_table_7)
cursor.execute(insert_into_grade_table_8)

conn.commit()
conn.close()