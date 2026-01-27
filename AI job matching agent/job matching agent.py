import re
import warnings
warnings.filterwarnings("ignore")
resumes = {
    "resume_1": "Python, Machine Learning, SQL, Data Analysis",
    "resume_2": "Java, Spring Boot, Microservices",
    "resume_3": "Python, Deep Learning, NLP, SQL",
    "resume_4": "HTML, CSS, JavaScript"
}
job_role = "Python Developer"

required_skills = [
    "python",
    "machine learning",
    "sql"
]
def load_resume(file_name):
    with open(file_name, "r") as file:
        return file.read()
        def clean_text(text):
    text = text.lower()
    text = text.replace(",", "").replace(".", "").replace("!", "")

    return text
    def match_score(resume_text, skills):
    score = 0
    resume_text = clean_text(resume_text)

    for skill in skills:
        if skill in resume_text:
            score += 1

    return score
    def extract_experience(resume_text):
    resume_text = resume_text.lower()

    if "2 years" in resume_text or "3 years" in resume_text:
        return 2
    elif "1 year" in resume_text:
        return 1
    else:
        return 0
        def final_decision(resume_text, skills):
    skill_score = match_score(resume_text, skills)
    experience_score = extract_experience(resume_text)

    total_score = skill_score + experience_score

    if total_score >= 3:
        return "Suitable", skill_score, experience_score
    else:
        return "Not Suitable", skill_score, experience_score

resume_text = load_resume("resume_suitable.txt")

result, skill_score, exp_score = final_decision(
    resume_text, required_skills
)

print("Skill Score:", skill_score)
print("Experience Score:", exp_score)
print("Final Result:", result)
resume_text = load_resume("resume_not_suitable.txt")

result, skill_score, exp_score = final_decision(
    resume_text, required_skills
)

print("Skill Score:", skill_score)
print("Experience Score:", exp_score)
print("Final Result:", result)

        