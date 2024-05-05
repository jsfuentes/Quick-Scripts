packages_list = """
    "axios": "^0.19.0",
    "debug": "^4.1.1",
    "react": "^16.8.6",
    "react-dom": "^16.8.6"
"""
packages = []
for line in packages_list.split("\n"):
    parts = line.split("\"")
    if len(parts) > 1:
        packages.append(parts[1])
print("npm i " + " ".join(packages))
