import json
import sys

with open("coverage.json", "r") as f:
    data = json.load(f)

coverage = data.get("result", {}).get("coverage", 0)

print(f"Coverage: {coverage}%")

if coverage < 75:
    print("Minimum coverage not met")
    sys.exit(1)

print("Coverage validation passed")
