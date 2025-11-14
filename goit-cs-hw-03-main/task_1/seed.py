from faker import Faker
import random
from db_connection import get_connection

fake = Faker()
conn = get_connection()
cur = conn.cursor()

statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", (status,))

user_ids = []
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id;", (fullname, email))
    user_ids.append(cur.fetchone()[0])

for _ in range(30):
    title = fake.sentence(nb_words=6)
    description = fake.text() if random.random() > 0.2 else None
    status_id = random.randint(1, 3)
    user_id = random.choice(user_ids)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
                (title, description, status_id, user_id))

conn.commit()
cur.close()
conn.close()
