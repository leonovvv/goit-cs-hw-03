from faker import Faker
import psycopg2

fake = Faker()

def seed_data():
    try:
        connection = psycopg2.connect(dbname="hw02", user="postgres", password="567234", host="localhost")
        cursor = connection.cursor()

        # Insert statuses
        statuses = ['new', 'in progress', 'completed']
        for status in statuses:
            cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (status,))

        # Insert users and tasks
        for _ in range(10):
            fullname = fake.name()
            email = fake.unique.email()
            cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id", (fullname, email))
            user_id = cursor.fetchone()[0]

            # Insert tasks for user
            for _ in range(fake.random.randint(1, 5)):
                title = fake.sentence(nb_words=6)
                description = fake.text() if fake.random.randint(0, 1) else None
                status_id = fake.random.randint(1, 3)
                cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))

        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    seed_data()