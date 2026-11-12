from validator import validate_practice_set

def test_valid_practice_set():
    practice_set = {
        "questions": [
            {
                "question": "What is 2 + 2?",
                "solution": "4",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            }
        ]
    }

    result = validate_practice_set(practice_set, 1)

    assert result is True


def test_missing_solution():
    practice_set = {
        "questions": [
            {
                "question": "What is 2 + 2?",
                "solution": "",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            }
        ]
    }



    result = validate_practice_set(practice_set, 1)

    assert result is False


def test_wrong_question_count():
    practice_set = {
        "questions": [
            {
                "question": "What is 2 + 2?",
                "solution": "4",
                "difficulty": "easy",
                "type": "computational",
                "topic": "Arithmetic"
            }
        ]
    }

    result = validate_practice_set(practice_set, 3)

    assert result is False

