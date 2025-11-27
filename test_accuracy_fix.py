#!/usr/bin/env python3
"""
Quick test to verify the accuracy fix works correctly.
Tests skill extraction and match score calculation.
"""

import re
from typing import List

# Copy the fixed functions here
SKILL_KEYWORDS = [
    # Programming Languages
    'python', 'javascript', 'typescript', 'java', 'csharp', 'cpp', 'php', 'go', 'rust', 'ruby', 'kotlin', 'swift',
    # Frontend
    'react', 'vue', 'angular', 'html', 'css', 'bootstrap', 'tailwind', 'webpack', 'nextjs', 'svelte',
    # Backend
    'nodejs', 'node', 'express', 'django', 'flask', 'fastapi', 'spring', 'laravel', 'aspnet',
    # Databases
    'sql', 'postgresql', 'mysql', 'mongodb', 'firebase', 'redis', 'elasticsearch', 'oracle', 'cassandra',
    # Cloud & DevOps
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'k8s', 'git', 'cicd', 'jenkins', 'terraform', 'ansible', 'linux',
    # Data Science & ML
    'machinelearning', 'tensorflow', 'pytorch', 'keras', 'scikitlearn', 'pandas', 'numpy', 'opencv', 'jupyter', 'nlp',
    # APIs & Tools
    'restapi', 'graphql', 'websocket', 'soap', 'agile', 'scrum', 'jira', 'slack', 'github', 'gitlab',
    # Soft Skills
    'communication', 'teamwork', 'leadership', 'management', 'problemsolving', 'analytical', 'creative', 'collaboration'
]

def extract_skills_from_text(cleaned_text: str) -> List[str]:
    """Extract skills from text with proper word boundary matching"""
    found = []
    text_lower = cleaned_text.lower()
    
    # Skill patterns with word boundaries to avoid false matches
    skill_patterns = {
        'python': r'\bpython\b',
        'javascript': r'\bjavascript\b|\bjs\b',
        'typescript': r'\btypescript\b|\bts\b',
        'java': r'\bjava\b(?!script)',  # Java but not JavaScript
        'csharp': r'\bc#\b|\bcsharp\b',
        'cpp': r'\bc\+\+\b',
        'php': r'\bphp\b',
        'go': r'\bgo\b(?:lang)?\b',
        'rust': r'\brust\b',
        'ruby': r'\bruby\b',
        'kotlin': r'\bkotlin\b',
        'swift': r'\bswift\b',
        'react': r'\breact\b',
        'vue': r'\bvue\.?js\b|\bvue\b',
        'angular': r'\bangular\b',
        'html': r'\bhtml\b',
        'css': r'\bcss\b',
        'bootstrap': r'\bbootstrap\b',
        'tailwind': r'\btailwind\b',
        'webpack': r'\bwebpack\b',
        'nextjs': r'\bnext\.?js\b',
        'svelte': r'\bsvelte\b',
        'nodejs': r'\bnode\.?js\b',
        'node': r'\bnode\b(?!\.js)',
        'express': r'\bexpress\b',
        'django': r'\bdjango\b',
        'flask': r'\bflask\b',
        'fastapi': r'\bfastapi\b',
        'spring': r'\bspring\b',
        'laravel': r'\blaravel\b',
        'aspnet': r'\basp\.net\b',
        'sql': r'\bsql\b',
        'postgresql': r'\bpostgres(?:ql)?\b',
        'mysql': r'\bmysql\b',
        'mongodb': r'\bmongo(?:db)?\b',
        'firebase': r'\bfirebase\b',
        'redis': r'\bredis\b',
        'elasticsearch': r'\belasticsearch\b',
        'oracle': r'\boracle\b',
        'cassandra': r'\bcassandra\b',
        'aws': r'\baws\b',
        'azure': r'\bazure\b',
        'gcp': r'\bgcp\b|\bgoogle\s+cloud\b',
        'docker': r'\bdocker\b',
        'kubernetes': r'\bkubernetes\b|\bk8s\b',
        'k8s': r'\bk8s\b',
        'git': r'\bgit\b',
        'cicd': r'\bci\s*/?cd\b',
        'jenkins': r'\bjenkins\b',
        'terraform': r'\bterraform\b',
        'ansible': r'\bansible\b',
        'linux': r'\blinux\b',
        'machinelearning': r'\bmachine\s+learning\b|\bml\b',
        'tensorflow': r'\btensorflow\b',
        'pytorch': r'\bpytorch\b',
        'keras': r'\bkeras\b',
        'scikitlearn': r'\bscikit[\s-]?learn\b',
        'pandas': r'\bpandas\b',
        'numpy': r'\bnumpy\b',
        'opencv': r'\bopencv\b',
        'jupyter': r'\bjupyter\b',
        'nlp': r'\bnlp\b',
        'restapi': r'\brest\s+api\b|\brestful\b',
        'graphql': r'\bgraphql\b',
        'websocket': r'\bwebsocket\b',
        'soap': r'\bsoap\b',
        'agile': r'\bagile\b',
        'scrum': r'\bscrum\b',
        'jira': r'\bjira\b',
        'slack': r'\bslack\b',
        'github': r'\bgithub\b',
        'gitlab': r'\bgitlab\b',
        'communication': r'\bcommunication\b',
        'teamwork': r'\bteamwork\b',
        'leadership': r'\bleadership\b',
        'management': r'\bmanagement\b',
        'problemsolving': r'\bproblem\s+solving\b',
        'analytical': r'\banalytical\b',
        'creative': r'\bcreative\b',
        'collaboration': r'\bcollaboration\b'
    }
    
    for skill, pattern in skill_patterns.items():
        if re.search(pattern, text_lower):
            if skill not in found:
                found.append(skill)
    
    return found

def calculate_match_score(resume_skills: List[str], job_skills: List[str]) -> int:
    """Calculate accurate match score"""
    if not job_skills:
        # No job description
        return min(len(resume_skills) * 5, 70)
    
    matched = [s for s in job_skills if s in resume_skills]
    score = int((len(matched) / len(job_skills)) * 100)
    return max(0, min(100, score))

# Test cases
print("=" * 60)
print("TESTING ACCURACY FIX")
print("=" * 60)

# Test 1: Perfect match
print("\n✓ TEST 1: Perfect Match (100%)")
resume1 = "python javascript react django mongodb"
job1 = "python javascript react django mongodb"
resume_skills1 = extract_skills_from_text(resume1)
job_skills1 = extract_skills_from_text(job1)
score1 = calculate_match_score(resume_skills1, job_skills1)
print(f"  Resume: {resume1}")
print(f"  Job: {job1}")
print(f"  Resume skills: {resume_skills1}")
print(f"  Job skills: {job_skills1}")
print(f"  Match score: {score1}% (expected: 100%)")
assert score1 == 100, f"Expected 100%, got {score1}%"

# Test 2: Partial match
print("\n✓ TEST 2: Partial Match (66%)")
resume2 = "python javascript react django"
job2 = "python javascript react django node express"
resume_skills2 = extract_skills_from_text(resume2)
job_skills2 = extract_skills_from_text(job2)
score2 = calculate_match_score(resume_skills2, job_skills2)
print(f"  Resume: {resume2}")
print(f"  Job: {job2}")
print(f"  Resume skills: {resume_skills2}")
print(f"  Job skills: {job_skills2}")
print(f"  Match score: {score2}% (expected: ~66%)")
assert 60 <= score2 <= 75, f"Expected ~66%, got {score2}%"

# Test 3: No match
print("\n✓ TEST 3: No Match (0%)")
resume3 = "python"
job3 = "java c++ kubernetes docker"
resume_skills3 = extract_skills_from_text(resume3)
job_skills3 = extract_skills_from_text(job3)
score3 = calculate_match_score(resume_skills3, job_skills3)
print(f"  Resume: {resume3}")
print(f"  Job: {job3}")
print(f"  Resume skills: {resume_skills3}")
print(f"  Job skills: {job_skills3}")
print(f"  Match score: {score3}% (expected: 0%)")
assert score3 == 0, f"Expected 0%, got {score3}%"

# Test 4: Java vs JavaScript (false positive prevention)
print("\n✓ TEST 4: Java vs JavaScript (False Positive Prevention)")
resume4 = "javascript nodejs react"
job4 = "java spring"
resume_skills4 = extract_skills_from_text(resume4)
job_skills4 = extract_skills_from_text(job4)
print(f"  Resume: {resume4}")
print(f"  Job: {job4}")
print(f"  Resume skills: {resume_skills4}")
print(f"  Job skills: {job_skills4}")
assert 'javascript' in resume_skills4 and 'java' not in resume_skills4, "JavaScript should be detected, not Java"
print(f"  ✓ Correctly detected JavaScript (not Java)")

# Test 5: No job description
print("\n✓ TEST 5: No Job Description Baseline")
resume5 = "python javascript react django mongo"
score5 = calculate_match_score(extract_skills_from_text(resume5), [])
print(f"  Resume skills: {len(extract_skills_from_text(resume5))}")
print(f"  Match score: {score5}% (should be capped at 70%)")
assert score5 <= 70, f"Expected <=70%, got {score5}%"

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED - ACCURACY FIX IS WORKING!")
print("=" * 60)
print("\n📊 Key Improvements:")
print("  1. 60+ skills detected (was 19)")
print("  2. Accurate formula: (matched / required) * 100")
print("  3. Java vs JavaScript collision fixed")
print("  4. Without job description: capped at 70%")
print("  5. With job description: realistic percentages")
