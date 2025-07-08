# 🤖 AI-Powered Internship Application Tracker

This is a full-stack web application built in 4 hours to help job seekers quickly analyze how well their resume matches a job description. The tool extracts key skills from a job post, compares them against a user's resume, and provides an instant match score and a list of matching/missing skills.

## ✨ Features

-   **Job Description Analysis:** Paste any job description to get started.
-   **Resume Parsing:** Upload your resume in PDF or DOCX format.
-   **AI Skill Extraction:** Uses spaCy for Natural Language Processing (NLP) to identify technical skills.
-   **Match Scoring:** Calculates a percentage score based on how many required skills are present in the resume.
-   **Skill Gap Analysis:** Clearly displays which skills you have and which you're missing.

## 🛠️ Tech Stack

-   **Backend:** Django
-   **Frontend:** HTML, CSS, Vanilla JavaScript
-   **NLP:** spaCy
-   **File Parsing:** PyMuPDF (for PDFs), python-docx (for Word docs)
-   **Database:** SQLite

## 🚀 Getting Started

1.  Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt 
    ```
    *(Note: We need to create this file)*
    
4.  Download the spaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```
5.  Run database migrations:
    ```bash
    python manage.py migrate
    ```
6.  Start the development server:
    ```bash
    python manage.py runserver
    ```

## 💡 Bonus: `requirements.txt`

Create a `requirements.txt` file so others can easily install the dependencies.

```bash
pip freeze > requirements.txt
