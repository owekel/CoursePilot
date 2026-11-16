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


def get_questions_for_set(practice_set_id, db_path = "data/coursepilot.db"):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM questions WHERE practice_set_id = ?",
        (practice_set_id,)
    )

    rows = cursor.fetchall()

    connection.close()

    return rows



def load_full_practice_set(practice_set_id, db_path="data/coursepilot.db"):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
            "SELECT * FROM practice_sets WHERE id = ?",
            (practice_set_id,)
        )

    row = cursor.fetchone()

    if row is None:
        connection.close()
        return None

    course = row[1]
    created_at = row[2]

    cursor.execute(
        "SELECT * FROM questions WHERE practice_set_id = ?",
        (practice_set_id,)
    )

    question_rows = cursor.fetchall()

    questions = []

    for row in question_rows:
        question = {
            "question": row[2],
            "solution": row[3],
            "difficulty": row[4],
            "type": row[5],
            "topic": row[6]
        }

        questions.append(question)

    practice_set = {
    "course": course,
    "created_at": created_at,
    "questions": questions
    }

    connection.close()

    return practice_set





if __name__ == "__main__":
    initialize_database()
    practice_sets = get_practice_sets()
    print(practice_sets)