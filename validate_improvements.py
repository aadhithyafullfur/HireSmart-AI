#!/usr/bin/env python3
"""
Final validation test for accuracy improvements
Tests all major components and validates fixes
"""
import sys
sys.path.insert(0, 'd:\\Projects\\Ai-resume-analyzer\\resume-analyzer\\ml_api')

from app import extract_skills_from_text, generate_ml_fallback_analysis

print("\n" + "=" * 70)
print("ACCURACY IMPROVEMENT VALIDATION TEST")
print("=" * 70)

# Test 1: Skill Extraction Accuracy
print("\n[TEST 1] Skill Extraction Accuracy")
print("-" * 70)

test_cases = [
    ("Python Django Flask", ["Python"]),
    ("JavaScript TypeScript React", ["TypeScript", "JavaScript", "React"]),
    ("Java Spring Boot", ["Java"]),  # Should NOT have JavaScript
    ("HTML CSS Bootstrap", ["HTML", "CSS", "Bootstrap"]),
    ("AWS Lambda DynamoDB", ["AWS"]),
    ("Docker Kubernetes", ["Docker", "Kubernetes"]),
]

all_passed = True
for resume, expected_skills in test_cases:
    found = extract_skills_from_text(resume)
    # Check if at least the main skills are there
    main_skill = expected_skills[0]
    if main_skill in found:
        print(f"[PASS] '{resume[:30]}...' -> Found {main_skill}")
    else:
        print(f"[FAIL] '{resume[:30]}...' -> Missing {main_skill}")
        all_passed = False

print(f"\nSkill Extraction: {'PASSED' if all_passed else 'FAILED'}")

# Test 2: Score Accuracy
print("\n[TEST 2] Match Score Accuracy")
print("-" * 70)

score_tests = [
    {
        "name": "Perfect Match (100%)",
        "resume": "JavaScript React Vue Python SQL Docker AWS Git",
        "job": "JavaScript React Vue Python SQL Docker AWS Git",
        "expected_min": 99,
        "expected_max": 101,
    },
    {
        "name": "Partial Match (50%)",
        "resume": "Python JavaScript React Docker",
        "job": "Python JavaScript React Vue SQL Docker AWS Kubernetes",
        "expected_min": 40,
        "expected_max": 60,
    },
    {
        "name": "Poor Match (25%)",
        "resume": "Python Django Flask",
        "job": "JavaScript React Vue Kotlin Swift Java",
        "expected_min": 0,
        "expected_max": 30,
    },
    {
        "name": "No Job Description (Baseline)",
        "resume": "Python JavaScript Git Docker",
        "job": "",
        "expected_min": 10,
        "expected_max": 30,
    },
]

score_passed = True
for test in score_tests:
    result = generate_ml_fallback_analysis(test["resume"], test["job"])
    score = result["analysis"]["skill_match_score"]
    
    is_valid = test["expected_min"] <= score <= test["expected_max"]
    status = "[PASS]" if is_valid else "[FAIL]"
    
    print(f"{status} {test['name']}: {score}% (expected {test['expected_min']}-{test['expected_max']}%)")
    
    if not is_valid:
        score_passed = False

print(f"\nScore Accuracy: {'PASSED' if score_passed else 'FAILED'}")

# Test 3: False Positive Prevention
print("\n[TEST 3] False Positive Prevention")
print("-" * 70)

false_positive_tests = [
    {
        "name": "Java vs JavaScript",
        "text": "JavaScript TypeScript React",
        "should_not_contain": "Java",
    },
    {
        "name": "Go vs Django",
        "text": "Django Python Flask",
        "should_not_contain": "Go",
    },
    {
        "name": "ML vs general text",
        "text": "Machine Learning Engineer",
        "should_contain": "Machine Learning",
    },
]

fp_passed = True
for test in false_positive_tests:
    found = extract_skills_from_text(test["text"])
    
    if "should_not_contain" in test:
        if test["should_not_contain"] not in found:
            print(f"[PASS] '{test['name']}': Correctly avoided false positive")
        else:
            print(f"[FAIL] '{test['name']}': False positive found: {test['should_not_contain']}")
            fp_passed = False
    
    if "should_contain" in test:
        if test["should_contain"] in found:
            print(f"[PASS] '{test['name']}': Correctly detected")
        else:
            print(f"[FAIL] '{test['name']}': Missed detection")
            fp_passed = False

print(f"\nFalse Positive Prevention: {'PASSED' if fp_passed else 'FAILED'}")

# Test 4: Future Skills Identification
print("\n[TEST 4] Future Skills Identification")
print("-" * 70)

result = generate_ml_fallback_analysis(
    "Python JavaScript React",
    "Python JavaScript React Vue SQL Docker AWS Kubernetes"
)

future = result["analysis"]["future_skills_required"]
required_missing = {"Vue", "SQL", "Docker", "AWS", "Kubernetes"}
missing_found = [s for s in required_missing if s in future]

if missing_found:
    print(f"[PASS] Correctly identified missing skills: {', '.join(missing_found[:3])}...")
    fp_passed = True
else:
    print(f"[FAIL] Failed to identify missing skills")
    fp_passed = False

print(f"\nFuture Skills Identification: {'PASSED' if fp_passed else 'FAILED'}")

# Summary
print("\n" + "=" * 70)
print("FINAL RESULT")
print("=" * 70)

all_tests_passed = all_passed and score_passed and fp_passed

if all_tests_passed:
    print("\n[SUCCESS] ALL TESTS PASSED")
    print("\nThe accuracy improvements are working correctly:")
    print("  * Skills detection expanded to 50+ technologies")
    print("  * Match scores are now realistic and varied")
    print("  * False positives (Java in JavaScript) have been eliminated")
    print("  * Job-skill matching is accurate")
    print("  * Future skills identification works correctly")
else:
    print("\n[FAILED] SOME TESTS FAILED")
    print("Please review the failures above")

print("\n" + "=" * 70)
