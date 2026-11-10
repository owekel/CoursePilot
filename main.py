from practice_generator import generate_practice_questions
from pdf_reader import render_pdf_pages, get_page_count
from storage import save_practice_set, load_practice_set, list_practice_sets
from datetime import datetime
from validator import validate_practice_set
from pathlib import Path

practice_set = None


while True:

    print("Welcome to CoursePilot!")
    print("1. Generate new practice questions")
    print("2. Load saved practice questions")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice in ("1", "2", "3"):
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if choice == "1":

    while True:
        pdf_path = Path(input("Enter a PDF path: ").strip())

        if not pdf_path.is_file():
            print("Your PDF path is not a file!")
            continue

        if pdf_path.suffix.lower() != ".pdf":
            print("Please enter a PDF file.")
            continue

        try:
            total_pages = get_page_count(pdf_path)

            if total_pages == 0:
                print("This PDF contains no pages.")
                continue

            print(f"Valid PDF! Found {total_pages} pages.")
            break

        except Exception as error:
            print(f"Unable to open PDF: {error}")

    while True:
        try:
            start_page = int(input(f"Enter the start page number (1-{total_pages}): "))
            end_page = int(input(f"Enter the end page number (1-{total_pages}): "))

            if start_page < 1 or start_page > total_pages:
                print(f"Invalid start page number. Please enter a number between 1 and {total_pages}.")
            elif end_page < 1 or end_page > total_pages:
                print(f"Invalid end page number. Please enter a number between 1 and {total_pages}.")
            elif start_page > end_page:
                print("Start page must be before or equal to end page.")
            elif end_page - start_page + 1 > 10:
                print("Please select a maximum of 10 pages.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            num_questions = int(input("Enter the number of questions (1-10): "))

            if 1<= num_questions <= 10:
                break
            else:
                print("Invalid number of questions")

        except ValueError:
            print("Please enter a valid integer.")


    while True:
        difficulty = input("Choose difficulty (easy/medium/hard/mixed): ").strip().lower()

        if difficulty in ("easy", "medium", "hard", "mixed"):
            break
        else:
            print("Invalid Difficulty Entered")


    print(f"Pages: {start_page}-{end_page}")
    print(f"Questions: {num_questions}")
    print(f"Difficulty: {difficulty}")

    image_paths = render_pdf_pages(pdf_path, start_page, end_page)



    practice_set = generate_practice_questions(image_paths, num_questions, difficulty)

    is_valid = validate_practice_set(practice_set, num_questions)

    if is_valid:
        print("Practice set is valid!")

        practice_set["course"] = pdf_path.stem
        practice_set["start_page"] = start_page
        practice_set["end_page"] = end_page
        practice_set["created_at"] = datetime.now().isoformat(timespec="seconds")
        practice_set["requested_difficulty"] = difficulty
        practice_set["requested_count"] = num_questions

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        file_path = f"data/practice_sets/{pdf_path.stem}_{timestamp}.json"

        save_practice_set(practice_set, file_path)

        print(f"Practice set saved to {file_path}")
        print(f"Generated {len(practice_set['questions'])} questions!")

    else:
        print("Practice set is invalid.")
        practice_set = None


elif choice == "2":
    saved_sets = list_practice_sets()

    for number, file in enumerate(saved_sets, start=1):
        saved_set = load_practice_set(file)

        course = saved_set.get("course", "Unknown course")
        start = saved_set.get("start_page", "?")
        end = saved_set.get("end_page", "?")
        created_at = saved_set.get("created_at", "Unknown date")

        print(f"{number}. {course} | Pages {start}-{end} | {created_at}")

    if len(saved_sets) == 0:
        print("You have no saved sets")
    else:
        while True:
            try:
                selection = int(input("Select a practice set: "))

                if 1 <= selection <= len(saved_sets):
                    selected_file = saved_sets[selection - 1]
                    practice_set = load_practice_set(selected_file)
                    break
                else:
                    print(f"Please enter a number between 1 and {len(saved_sets)}.")

            except ValueError:
                print("Invalid input. Please enter an integer.")

elif choice == "3":
    # Exit the program
    print("See ya")




if practice_set is not None:
    for number, question in enumerate(practice_set["questions"], start=1):
        print(f"\nQuestion {number}")
        print(f"Topic: {question['topic']}")
        print(f"Difficulty: {question['difficulty']}")
        print(question["question"])

        input("\nPress Enter to reveal the solution...")
        print(question["solution"])



