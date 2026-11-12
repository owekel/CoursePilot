from storage import save_practice_set, load_practice_set


def test_save_and_load(tmp_path):
    file_path = tmp_path / "test_practice.json"

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

    save_practice_set(practice_set, file_path)

    result = load_practice_set(file_path)

    assert result == practice_set


def test_creates_missing_directory(tmp_path):
    file_path = tmp_path / "new_folder" / "practice.json"

    practice_set = {"questions": []}

    save_practice_set(practice_set, file_path)

    assert file_path.exists()

    assert file_path.parent.exists()