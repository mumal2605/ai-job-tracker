import spacy
import fitz
import docx
nlp = spacy.load("en_core_web_sm")
SKILLS_LIST = [
    'python', 'django', 'flask', 'fastapi', 'java', 'c++', 'c#', 'javascript',
    'typescript', 'react', 'angular', 'vue', 'html', 'css', 'sql', 'mysql',
    'postgresql', 'mongodb', 'nosql', 'aws', 'azure', 'gcp', 'docker',
    'kubernetes', 'git', 'github', 'rest', 'api', 'nlp', 'spaCy',
    'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn',
    'pandas', 'numpy', 'data analysis', 'data science', 'agile', 'scrum'
]
def extract_skills_from_jd(text : str) -> list[str]:
    doc = nlp(text.lower())
    extracted_skills = set()
    for token in doc:
        if token.text in SKILLS_LIST:
            extracted_skills.add(token.text)

    for chunk in doc.noun_chunks:
        if chunk.text in SKILLS_LIST:
            extracted_skills.add(chunk.text)

    return list(extracted_skills)

def extract_text_from_file(file_path: str) -> str:
    text = ""
    if file_path.endswith('.pdf'):
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

def extract_skills_from_resume(file_path: str) -> list[str]:
    resume_text = extract_text_from_file(file_path)
    return extract_skills_from_jd(resume_text)
 
