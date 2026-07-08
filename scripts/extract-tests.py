import os

tests = []

for root, dirs, files in os.walk("delta"):
    for file in files:
        if file.endswith(".cls") and not file.endswith("Test.cls"):
            class_name = file.replace(".cls", "")
            tests.append(f"{class_name}Test")

if tests:
    with open("tests.txt", "w") as f:
        f.write(",".join(tests))
