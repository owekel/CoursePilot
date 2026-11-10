def validate_practice_set(practice_set, num_questions):
    is_valid = True
    
    if not isinstance(practice_set, dict):
        print("Invalid response: expected a dictionary.")
        return False

    questions = practice_set.get("questions")

    if not isinstance(questions, list):
        print("Invalid response: excpected a list")
        return False


    actual_count = len(practice_set["questions"])

    if num_questions == actual_count:
        print("Correct number of questions generated!")
    else:
        print(f"Asked for {num_questions} questions but got {actual_count}.")
        is_valid = False



    required_fields = ["question", "solution", "difficulty", "type", "topic"]

    for number, question in enumerate(questions, start=1):
        if not isinstance(question, dict):
            print(f"Question {number} is not a dictionary!")
            is_valid = False
            continue

        for field in required_fields:
            if not question.get(field):
                print(f"Question {number} has a missing or empty {field}!")
                is_valid = False

    return is_valid