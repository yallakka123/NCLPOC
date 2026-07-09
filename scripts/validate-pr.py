import os
import sys

pr_body = os.getenv("PR_BODY", "")

required_sections = [
    "Jira",
    "Description",
    "Rollback Plan",
    "Tests"
]

missing = []

for section in required_sections:
    if section.lower() not in pr_body.lower():
        missing.append(section)

if missing:
    print(f"Missing sections: {', '.join(missing)}")
    sys.exit(1)

print("PR validation passed")
