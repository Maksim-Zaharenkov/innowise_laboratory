CREATE TABLE IF NOT EXISTS students
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name TEXT NOT NULL,
birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS grades
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER,
subject TEXT NOT NULL,
grade INTEGER, 
CONSTRAINT student_check_grade CHECK(grade >= 0 AND grade <= 100),
CONSTRAINT students_grades_fk
FOREIGN KEY (student_id) REFERENCES students (id)
);

INSERT INTO students (full_name, birth_year) VALUES 
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

CREATE INDEX IF NOT EXISTS index_grades_students_student_id ON grades (student_id);
CREATE INDEX IF NOT EXISTS index_subject ON grades (subject);

SELECT grade 
FROM grades AS g 
JOIN students AS s ON g.student_id  = s.id
WHERE s.full_name = 'Alice Johnson';

SELECT s.full_name, AVG(g.grade) AS average_grade 
FROM students AS s
JOIN grades AS g ON s.id  = g.student_id 
GROUP BY s.full_name;

SELECT full_name FROM students WHERE birth_year > 2004;

SELECT subject, AVG(grade) AS average_grade FROM grades GROUP BY subject;

SELECT s.full_name, AVG(g.grade) AS average_grade 
FROM students AS s 
JOIN grades AS g ON s.id  = g.student_id 
GROUP BY s.full_name
ORDER BY average_grade DESC
LIMIT 3;

SELECT DISTINCT s.id, s.full_name
FROM students as s
JOIN grades as g ON s.id = g.student_id
WHERE g.grade < 80;