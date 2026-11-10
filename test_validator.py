from validator import validate_practice_set

practice_set = {
    "questions": [
        {
            "question": "what is 2+2",
            "solution": "4",
            "difficulty": "easy",
            "type": "computational",
            "topic": "Arithmetic"
        }
    ]
}

result = validate_practice_set(practice_set, 1)

print(result)



