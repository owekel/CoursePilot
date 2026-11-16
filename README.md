
# CoursePilot

CoursePilot is a Python application that turns university course PDFs into AI-generated practice questions with step-by-step solutions.

I built it to make studying more targeted: instead of searching through lecture notes for relevant problems, users can select specific pages, choose a difficulty, and generate a practice set based on that material.

## Features

- Upload local PDF course materials and select specific page ranges
- Generate original practice questions using Google's Gemini API
- Choose the number of questions and difficulty level
- Validate generated question data before saving
- Save and retrieve practice sets using SQLite
- Store questions in a relational database linked to their practice sets
- Reveal solutions interactively through a command-line interface
- Export generated practice sets as JSON

## Tech Stack

- **Python** — Application logic and command-line interface
- **Google Gemini API** — AI-powered question generation
- **PyMuPDF** — PDF processing and page rendering
- **SQLite / SQL** — Persistent storage, relational tables, and database transactions
- **pytest** — Automated testing
- **Git / GitHub** — Version control

## Getting Started

Clone the repository:

```bash
git clone https://github.com/owekel/CoursePilot.git
cd CoursePilot
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install google-genai pymupdf pytest
```

Set your Gemini API key:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

Run CoursePilot:

```bash
python main.py
```

Choose whether to generate questions from a PDF or load an existing practice set.

## Testing

Run the automated test suite with:

```bash
python -m pytest -v
```

The tests cover practice-set validation, JSON storage, SQLite persistence, data retrieval, and transaction rollback.

## Project Status

CoursePilot is currently a working command-line application under active development.

Planned improvements include a FastAPI backend and a web interface to make generating and reviewing practice questions more accessible.
