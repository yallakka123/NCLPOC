import xml.etree.ElementTree as ET

tests = []

package_file = "delta/package/package.xml"

try:
    tree = ET.parse(package_file)
    root = tree.getroot()

    namespace = {"sf": "http://soap.sforce.com/2006/04/metadata"}

    for types in root.findall("sf:types", namespace):
        name = types.find("sf:name", namespace)

        if name is not None and name.text == "ApexClass":
            for member in types.findall("sf:members", namespace):
                class_name = member.text

                if not class_name.endswith("Test"):
                    tests.append(f"{class_name}Test")

    if tests:
        with open("tests.txt", "w") as f:
            f.write(",".join(tests))

except Exception as e:
    print(f"Error: {e}")
