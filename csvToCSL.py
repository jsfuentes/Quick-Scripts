# Open a csv file and parse it to a CSL file
import csv

# The path to your CSV file
csv_file_path = 'mixpanel.csv'

# Initialize an empty list to store the rows of the CSV as dictionaries
data = []

# Open the CSV file for reading
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    # Create a CSV reader object, assuming your CSV has a header row
    reader = csv.DictReader(csvfile)

    # Iterate over the rows in the CSV
    for row in reader:
        # Each row is a dictionary where the keys are the column headers
        # and the values are the data in each cell of the row.
        data.append(row)

userIds = list(map(lambda x: x.get('$distinct_id'), data))
print("\"", "\",\"".join(userIds), "\"", sep='')
