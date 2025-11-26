"""
Test script to verify improved accuracy of skill matching
"""
import requests
import json

# Test Case 1: Python developer with limited skills
resume_1 = """
JOHN DOE
Python Developer

SKILLS:
- Python, Flask, Django
- HTML, CSS
- Git

EXPERIENCE:
- 2 years Python development
- Built web applications with Flask
"""

job_1 = """
Senior Python Developer

REQUIRED SKILLS:
- Python, Django, Flask
- React, JavaScript
- AWS, Docker
- SQL, PostgreSQL
- Kubernetes
"""

print("=" * 60)
print("TEST 1: Python Developer vs Senior Python Role")
print("=" * 60)
print(f"Resume Skills: Python, Flask, Django, HTML, CSS, Git")
print(f"Job Requires: Python, Django, Flask, React, JavaScript, AWS, Docker, SQL, PostgreSQL, Kubernetes")
print(f"Expected Match: ~30-40% (has 3/10 required skills)")

try:
    response = requests.post(
        "http://localhost:8000/analyze/resume-ollama",
        data={"job_description": job_1},
        files={"file": ("resume1.txt", resume_1, "text/plain")}
    )
    if response.status_code == 200:
        result = response.json()
        score = result.get("job_match_score", result.get("analysis", {}).get("skill_match_score", 0))
        print(f"Actual Match Score: {score}%")
        print(f"Analysis: {json.dumps(result.get('analysis', {}), indent=2)}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 60)
print("TEST 2: Full-Stack Developer vs Full-Stack Role")
print("=" * 60)

resume_2 = """
JANE SMITH
Full-Stack Developer

SKILLS:
- JavaScript, TypeScript, React, Vue
- Python, Django
- SQL, PostgreSQL, MongoDB
- Docker, Kubernetes
- AWS S3, Lambda
- Git, GitHub
- HTML5, CSS3, Tailwind
- REST APIs

EXPERIENCE:
- 5 years full-stack development
- Built and deployed microservices
"""

job_2 = """
Full-Stack Engineer

REQUIRED SKILLS:
- JavaScript, React, Vue
- Python
- SQL, PostgreSQL
- Docker
- AWS
- Git
"""

print(f"Resume Skills: JavaScript, TypeScript, React, Vue, Python, SQL, PostgreSQL, MongoDB, Docker, Kubernetes, AWS, Git, HTML5, CSS3, Tailwind, REST APIs")
print(f"Job Requires: JavaScript, React, Vue, Python, SQL, PostgreSQL, Docker, AWS, Git")
print(f"Expected Match: 80-90% (has 9/9 required skills)")

try:
    response = requests.post(
        "http://localhost:8000/analyze/resume-ollama",
        data={"job_description": job_2},
        files={"file": ("resume2.txt", resume_2, "text/plain")}
    )
    if response.status_code == 200:
        result = response.json()
        score = result.get("job_match_score", result.get("analysis", {}).get("skill_match_score", 0))
        print(f"Actual Match Score: {score}%")
        print(f"Analysis: {json.dumps(result.get('analysis', {}), indent=2)}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 60)
print("TEST 3: No job description (baseline)")
print("=" * 60)

resume_3 = """
Basic resume with Python, JavaScript, Git
"""

print(f"Resume Skills: Python, JavaScript, Git")
print(f"No job description provided")
print(f"Expected Match: ~15% (3 skills × 5% = 15%, max 70%)")

try:
    response = requests.post(
        "http://localhost:8000/analyze/resume-ollama",
        data={"job_description": ""},
        files={"file": ("resume3.txt", resume_3, "text/plain")}
    )
    if response.status_code == 200:
        result = response.json()
        score = result.get("job_match_score", result.get("analysis", {}).get("skill_match_score", 0))
        print(f"Actual Match Score: {score}%")
        print(f"Analysis: {json.dumps(result.get('analysis', {}), indent=2)}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("✓ If scores are realistic (not always 90%), the fix is working!")
print("✓ Check that different resumes produce different scores")
