import sqlite3


def initialize_database(db_path = "data/coursepilot.db"):
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS practice_sets (
    id INTEGER PRIMARY KEY,
    course TEXT NOT NULL,
    created_at TEXT NOT NULL
    );
    """
        )

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    practice_set_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    solution TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    type TEXT NOT NULL,
    topic TEXT NOT NULL,
    FOREIGN KEY (practice_set_id) REFERENCES practice_sets(id)
    );
    """
        )

    connection.commit()
    connection.close()




def save_full_practice_set(practice_set, db_path = "data/coursepilot.db"):
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")

    cursor = connection.cursor()

    try:
        course = practice_set["course"]
        created_at = practice_set["created_at"]

        cursor.execute(
        "INSERT INTO practice_sets (course, created_at) VALUES (?, ?)",
        (course, created_at)
        )   

        practice_set_id = cursor.lastrowid

        for question in practice_set["questions"]:
            cursor.execute(
                "INSERT INTO questions (practice_set_id, question, solution, difficulty, type, topic) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    practice_set_id,
                    question["question"],
                    question["solution"],
                    question["difficulty"],
                    question["type"],
                    question["topic"]
                )
            )

        connection.commit()

        return practice_set_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


    


def get_practice_sets():
    connection = sqlite3.connect("data/coursepilot.db")
    
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM practice_sets;")

    rows = cursor.fetchall()

    connection.close()

    return rows




if __name__ == "__main__":
    initialize_database()
    practice_sets = get_practice_sets()
    print(practice_sets)