import json
from google import genai
from google.genai import types
from google.genai.errors import ServerError


client = genai.Client()

schema = {
    "type": "OBJECT",
    "properties": {
        "questions": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "question": {"type": "STRING"},
                    "solution": {"type": "STRING"},
                    "difficulty": {"type": "STRING", "enum": ["easy", "medium", "hard"]},
                    "type": {"type": "STRING", "enum": ["computational", "conceptual", "proof"]},
                    "topic": {"type": "STRING"}
                },
                "required": [
                    "question",
                    "solution",
                    "difficulty",
                    "type",
                    "topic"
                ]
            }
        }
    },
    "required": ["questions"]
}

def generate_practice_questions(image_paths, num_questions, difficulty):
    # 1. Open the image file
    
    images = []


    for image_path in image_paths:
        with open(image_path, "rb") as file:
            image_data = file.read()

        image_part = types.Part.from_bytes(
            data = image_data,
            mime_type = "image/png"
        )

        images.append(image_part)


    # 2. Send the image to Gemini with a prompt

    prompt = f"""
    You are a university-level educator.

    Analyze the provided course material.
    Identify the main concepts taught on these pages.

    Generate {num_questions} original practice questions based on
    those concepts.

    The requested difficulty is {difficulty}

    Requirements:
    1. Test the same concepts as the textbook.
    2. Do not copy the textbook's example.
    3. Match the requested difficulty level. If the difficulty is mixed, include a range of easy, medium, and hard questions.
    4. Provide a detailed step-by-step solution.
    5. Check that your solution satisfies the problem.

    Additional requirements:
    - Every question must be self-contained.
    - Do not reference textbook exercises or figures.
    - Ensure that every question has a valid solution.
    - Independently verify calculations before responding.
    - Generate a mix of computational and conceptual questions.
    - Do not generate questions that are nearly identical.
    
    """

    try:
        response = client.models.generate_content(
        model = "gemini-3.1-flash-lite",
        contents = images + [prompt],
        config = types.GenerateContentConfig(
            response_mime_type = "application/json",
            response_schema = schema
            )
        )

        return json.loads(response.text)
    except ServerError:
        print("Gemini is temporarily unavailable. Please try again.")
        return None