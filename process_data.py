import pandas as pd
import csv

# Load the scraped data
df = pd.read_csv('restaurants-dubai-yellowpages-scraped-data.csv')

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)

# Handle missing values
# For example, fill missing values in the 'website' column with 'Not Available'
df.loc[df['website'].isnull(), 'website'] = 'Not Available'

# Create a list to store dictionaries
output_list = []

# Iterate over rows in DataFrame
for index, row in df.iterrows():
    # Create a dictionary for each row
    row_dict = {
        "rank": row["rank"],
        "business_name": row["business_name"],
        "telephone": row["telephone"],
        "business_page": row["business_page"],
        "street_address": row["category"],
        "locality": row["website"],
        "zipcode": row["zipcode"]
    }
    # Append the dictionary to the list
    output_list.append(row_dict)

# Specify the output CSV file path
output_csv_file = 'results.csv'

# Write the list of dictionaries to the output CSV file
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["rank", "business_name", "telephone", "business_page", "street_address", "locality", "zipcode"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in output_list:
        writer.writerow(entry)

print(f"Output data has been saved to {output_csv_file}")
