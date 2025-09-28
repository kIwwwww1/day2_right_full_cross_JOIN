import psycopg2

config = psycopg2.connect('postgresql://postgres:password<3@localhost:5432/postgres')

def create_db():
    with config as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS employees (
                    emp_id INT PRIMARY KEY,
                    emp_name VARCHAR(50),
                    dept_id INT);""")
        
        c.execute("""CREATE TABLE IF NOT EXISTS departments (
                    dept_id INT PRIMARY KEY,
                    dept_name VARCHAR(50));""")
        conn.commit()
        print('База создана')

def inset_data():
    with config as conn:
        c = conn.cursor()
        c.execute("""INSERT INTO employees (emp_id, emp_name, dept_id) VALUES
                    (1, 'Анна', 10),
                    (2, 'Борис', 20),
                    (3, 'Виктор', 30),
                    (4, 'Галина', NULL),
                    (5, 'Дмитрий', 10);""")
        c.execute("""INSERT INTO departments (dept_id, dept_name) VALUES
                    (10, 'Разработка'),
                    (20, 'Маркетинг'),
                    (40, 'HR'),     
                    (50, 'Финансы');""")
        conn.commit()
        print('Данные добавлены')

# 1 
def one():
    with config as conn:
        c = conn.cursor()
        c.execute("""SELECT e.emp_name, d.dept_name FROM employees e FULL JOIN departments d ON e.dept_id = d.dept_id""")
        for i in c.fetchall():
            print(f'{i[0]} | {i[-1]}')
# 2
def two():
    with config as conn:
        c = conn.cursor()
        c.execute("""SELECT e.emp_name, d.dept_name FROM employees e CROSS JOIN departments d""")
        for i in c.fetchall():
            print(f'{i[0]} | {i[1]}')

