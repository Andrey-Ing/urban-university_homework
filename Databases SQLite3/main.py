import sqlite3

db = sqlite3.connect("students.db")
cur = db.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS students
        (id INTEGER NOT NULL PRIMARY KEY, name STR, age INT)
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS grades
        (id PRIMARY KEY, student_id INTEGER REFERENCES students(id), subject STR, grade FLOAT)
""")

db.commit()


class University:
    def __init__(self, name, database=db):
        self.name = name
        self.db = database
        self.cur = database.cursor()

    def add_student(self, name, age):
        cur.execute("""
            INSERT INTO students (name, age) VALUES (?, ?)
        """, (name, age))
        db.commit()

    def add_grade(self, student_id, subject, grade):
        cur.execute("""
            INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)
        """, (student_id, subject, grade))
        db.commit()

    def get_students(self, subject=None):
        if subject is None:
            cur.execute("""
                        SELECT st.name, st.age, gr.subject, gr.grade
                        FROM students st, grades gr
                        WHERE st.id = gr.student_id
            """)
            return cur.fetchall()
        else:
            cur.execute("""
                        SELECT st.name, st.age, gr.subject, gr.grade
                        FROM students st, grades gr
                        WHERE st.id = gr.student_id
                        AND gr.subject = ?
            """, [subject])
            return cur.fetchall()


u1 = University('Urban')

u1.add_student('Ivan', 26)  # id - 1
u1.add_student('Ilya', 24)  # id - 2
u1.add_student('Dasha', 27)  # id - 3
u1.add_student('Peter', 23)  # id - 4

u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)
u1.add_grade(1, 'С++', 4.8)
u1.add_grade(3, 'PHP', 4.4)
u1.add_grade(3, 'SQL', 4.8)
u1.add_grade(2, 'PHP', 4.9)
u1.add_grade(4, 'Python', 4.5)
u1.add_grade(4, 'SQL', 4.3)

print(u1.get_students())
print(u1.get_students('Python'))
print(u1.get_students('SQL'))

db.close()
