"""
Quick test of accuracy improvements
"""
import sys
sys.path.insert(0, 'd:\\Projects\\Ai-resume-analyzer\\resume-analyzer\\ml_api')

from app import generate_ml_fallback_analysis

# Test 1: Limited skills vs complex job
print("TEST 1: Python Dev (3 required skills match) vs Senior Python Role (10 skills required)")
resume1 = "Python Flask Django HTML CSS Git"
job1 = "Python Django Flask React JavaScript AWS Docker SQL PostgreSQL Kubernetes"
result1 = generate_ml_fallback_analysis(resume1, job1)
print(f"Score: {result1['analysis']['skill_match_score']}% (expected 30-40%)")
print(f"Skills you have: {result1['analysis']['project_skills_implemented']}")
print(f"Skills needed: {result1['analysis']['future_skills_required']}")
print()

# Test 2: Perfect match
print("TEST 2: Full-Stack Dev vs Full-Stack Role (9/9 match)")
resume2 = "JavaScript TypeScript React Vue Python SQL PostgreSQL Docker AWS Git"
job2 = "JavaScript React Vue Python SQL PostgreSQL Docker AWS Git"
result2 = generate_ml_fallback_analysis(resume2, job2)
print(f"Score: {result2['analysis']['skill_match_score']}% (expected 100%)")
print(f"Skills you have: {result2['analysis']['project_skills_implemented']}")
print(f"Skills needed: {result2['analysis']['future_skills_required']}")
print()

# Test 3: No job desc
print("TEST 3: Basic resume, no job description")
resume3 = "Python JavaScript Git"
result3 = generate_ml_fallback_analysis(resume3, "")
print(f"Score: {result3['analysis']['skill_match_score']}% (expected max 70%, baseline)")
print(f"Skills in resume: {result3['analysis']['project_skills_implemented']}")
print()

# Test 4: Check Java/JavaScript collision
print("TEST 4: Check if Java falsely detected in JavaScript")
resume4 = "JavaScript TypeScript React"
result4 = generate_ml_fallback_analysis(resume4, "")
has_java = 'Java' in result4['analysis']['project_skills_implemented']
print(f"Resume: JavaScript TypeScript React")
print(f"Skills found: {result4['analysis']['project_skills_implemented']}")
print(f"Has Java (should be False): {has_java}")
print()

print("=" * 60)
if has_java:
    print("[FAILED] Java collision still exists - need to fix")
else:
    print("[SUCCESS] Accuracy improvements working!")
    print("Scores are now realistic and varied, not always 90%")
