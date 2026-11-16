import sqlite3, pytest
from database import initialize_database, save_full_practice_set, get_questions_for_set, load_full_practice_set


def test_save_full_practice_set(tmp_path):
    db_path = tmp_path / "test.db"

    initialize_database(db_path)

    practice_set = {
        "course": "MATH 115",
        "created_at": "2026-11-13",
        "questions": [
            {
                "question": "What is 2 + 2?",
                "solution": "4",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            },
            {
                "question": "What is 3 + 3?",
                "solution": "6",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            }
        ]
    }

    save_full_practice_set(practice_set, db_path)

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions")
    question_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM practice_sets")
    practice_set_count = cursor.fetchone()[0]

    connection.close()

    assert question_count == 2
    assert practice_set_count == 1



def test_rollback_on_failure(tmp_path):
    db_path = tmp_path / "rollback_test.db"

    initialize_database(db_path)

    practice_set = {
        "course": "MATH 115",
        "created_at": "2026-11-13",
        "questions": [
            {
                "question": "What is 2 + 2?",
                "solution": "4",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            },
            {
                "question": "What is 3 + 3?",

                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            }
        ]
    }

    with pytest.raises(KeyError):
        save_full_practice_set(practice_set, db_path)

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions")
    question_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM practice_sets")
    practice_set_count = cursor.fetchone()[0]

    assert question_count == 0
    assert practice_set_count == 0

def test_get_questions_for_set(tmp_path):
    db_path = tmp_path / "get_questions_test.db"

    initialize_database(db_path)

    practice_set = {
        "course": "MATH 115",
        "created_at": "2026-11-13",
        "questions": [
            {
                "question": "What is 2 + 2?",
                "solution": "4",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            },
            {
                "question": "What is 3 + 3?",
                "solution": "6",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            }
        ]
    }

    practice_set_id = save_full_practice_set(practice_set, db_path)

    assert len(get_questions_for_set(practice_set_id, db_path)) == 2



def test_load_full_practice_set(tmp_path):
    db_path = tmp_path / "load_test.db"

    initialize_database(db_path)

    practice_set = {
        "course": "MATH 115",
        "created_at": "2026-11-14",
        "questions": [
            {
                "question": "What is 2 + 2?",
                "solution": "4",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            },
            {
                "question": "What is 5 + 2?",
                "solution": "7",
                "difficulty": "hard",
                "type": "computational",
                "topic": "Arithmetic"
            }            
        ]
    }

    practice_set_id = save_full_practice_set(practice_set, db_path)

    loaded_pset = load_full_practice_set(practice_set_id, db_path)

    assert loaded_pset == practice_set

