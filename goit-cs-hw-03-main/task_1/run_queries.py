from db_connection import get_connection

def run_queries():
    conn = get_connection()
    cur = conn.cursor()

    print("\n1. Усі завдання певного користувача (user_id = 1):")
    cur.execute("SELECT * FROM tasks WHERE user_id = 1;")
    print(cur.fetchall())

    print("\n2. Завдання зі статусом 'new':")
    cur.execute("""
        SELECT * FROM tasks 
        WHERE status_id = (SELECT id FROM status WHERE name = 'new');
    """)
    print(cur.fetchall())

    print("\n3. Оновити статус завдання з id = 5 на 'in progress':")
    cur.execute("""
        UPDATE tasks 
        SET status_id = (SELECT id FROM status WHERE name = 'in progress') 
        WHERE id = 5 
        RETURNING *;
    """)
    print(cur.fetchall())

    print("\n4. Користувачі без жодного завдання:")
    cur.execute("""
        SELECT * FROM users 
        WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
    """)
    print(cur.fetchall())

    print("\n5. Додати нове завдання користувачу (user_id = 2):")
    cur.execute("""
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES ('Test Task', 'Inserted from script', 
                (SELECT id FROM status WHERE name = 'new'), 2)
        RETURNING *;
    """)
    print(cur.fetchall())

    print("\n6. Усі незавершені завдання (не 'completed'):")
    cur.execute("""
        SELECT * FROM tasks 
        WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
    """)
    print(cur.fetchall())

    print("\n7. Видалення завдання з id = 10:")
    cur.execute("DELETE FROM tasks WHERE id = 10 RETURNING *;")
    print(cur.fetchall())

    print("\n8. Користувачі з email, що містить '@example.com':")
    cur.execute("SELECT * FROM users WHERE email LIKE '%@example.com';")
    print(cur.fetchall())

    print("\n9. Оновити ім’я користувача з id = 3:")
    cur.execute("UPDATE users SET fullname = 'Updated User' WHERE id = 3 RETURNING *;")
    print(cur.fetchall())

    print("\n10. Кількість завдань для кожного статусу:")
    cur.execute("""
        SELECT s.name AS status, COUNT(t.id) AS task_count
        FROM status s
        LEFT JOIN tasks t ON s.id = t.status_id
        GROUP BY s.name;
    """)
    print(cur.fetchall())

    print("\n11. Завдання користувачів з email, що містить '@example.com':")
    cur.execute("""
        SELECT t.* FROM tasks t
        JOIN users u ON t.user_id = u.id
        WHERE u.email LIKE '%@example.com';
    """)
    print(cur.fetchall())

    print("\n12. Завдання без опису:")
    cur.execute("""
        SELECT * FROM tasks 
        WHERE description IS NULL OR description = '';
    """)
    print(cur.fetchall())

    print("\n13. Користувачі та їхні завдання у статусі 'in progress':")
    cur.execute("""
        SELECT u.fullname, t.title FROM users u
        JOIN tasks t ON u.id = t.user_id
        WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');
    """)
    print(cur.fetchall())

    print("\n14. Користувачі та кількість їхніх завдань:")
    cur.execute("""
        SELECT u.fullname, COUNT(t.id) AS task_count
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.id;
    """)
    print(cur.fetchall())

    cur.close()
    conn.close()

if __name__ == "__main__":
    run_queries()
