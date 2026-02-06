import re
import json

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not found"

def extract_name(text):
    lines = text.strip().split('\n')
    return lines[0] if lines else "Not found"

def extract_skills(text, skills_list):
    text = text.lower()
    return [skill for skill in skills_list if skill.lower() in text]


def calculate_match_score(found_skills, required_skills):
    if not required_skills:
        return 0
    return int((len(found_skills) / len(required_skills)) * 100)

def analyze_resume(resume_text, job_requirements):
    name = extract_name(resume_text)
    email = extract_email(resume_text)
    skills = extract_skills(resume_text, job_requirements["skills"])
    score = calculate_match_score(skills, job_requirements["skills"])

    recommendation = (
        "Strong Match" if score >= 70
        else "Average Match" if score >= 40
        else "Weak Match"
    )

    return {
        "name": name,
        "email": email,
        "matched_skills": skills,
        "match_score": score,
        "recommendation": recommendation
    }

def save_report(data, filename="analysis_report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    resume_text = """
    Chamala Venkata Navya
    navyachamala475@gmail.com
    Skills: Python, Machine Learning, Data Analysis, NLP
    Experience: 2 years
    """

    job_requirements = {
        "skills": ["Python", "Machine Learning", "NLP", "SQL"]
    }

    report = analyze_resume(resume_text, job_requirements)
    save_report(report)

    print("Resume Analysis Complete!")
    print(report)