import numpy as np

def match_skills(user_skills, course_skills):
    common = len(set(user_skills) & set(course_skills))
    total = len(set(user_skills) | set(course_skills))
    return common / total if total != 0 else 0

def recommend_courses(user_id, courses, users, top_n=5):
    user_data = users.get(user_id, None)
    if not user_data:
        return []
    
    user_hobbies = set(user_data['hobbies'])
    user_skills = set(user_data['expertise'])
    
    recommendations = []
    for course in courses:
        skill_score = match_skills(user_skills, course['requirements'])
        hobby_match = len(user_hobbies & set(course['domain']))
        score = 0.7 * skill_score + 0.3 * hobby_match  
        recommendations.append((course['id'], course['title'], score))
    
    recommendations.sort(key=lambda x: x[2], reverse=True)
    return recommendations[:top_n]

courses = [
    {"id": 1, "title": "Cybersecurity Fundamentals", "requirements": ["Networking", "Security"], "domain": ["Cybersecurity"]},
    {"id": 2, "title": "Data Science", "requirements": ["Python", "Statistics", "Data Analysis"], "domain": ["Data Science"]},
    {"id": 3, "title": "Web Development", "requirements": ["HTML", "CSS", "JavaScript"], "domain": ["Software Development"]}
]


users = {
    "user_1": {"hobbies": ["Cybersecurity"], "expertise": ["Networking"], "learning_preference": "Security"},
    "user_2": {"hobbies": ["Software Development"], "expertise": ["HTML", "CSS"], "learning_preference": "Frontend"}
}

print(recommend_courses("user_1", courses, users))
