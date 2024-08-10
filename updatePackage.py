import sys
import json
import os
import pyperclip


def get_packages_from_json(filepath):
    package_json_path = os.path.join(filepath, 'package.json')

    if not os.path.exists(package_json_path):
        print(f"Error: package.json not found in {filepath}")
        return None

    with open(package_json_path, 'r') as f:
        package_data = json.load(f)

    dependencies = package_data.get('dependencies', {})

    return list(dependencies.keys())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python updatePackage.py <path_to_project_folder>")
        sys.exit(1)

    project_path = sys.argv[1]
    packages = get_packages_from_json(project_path)

    if packages:
        npm_command = "npm i " + " ".join(packages)
        print(npm_command)
        pyperclip.copy(npm_command)
        print("The npm install command has been copied to your clipboard. \n First delete the package.json dependencies, then run the command to refresh every package version.")
    else:
        print("No packages found or error occurred.")
