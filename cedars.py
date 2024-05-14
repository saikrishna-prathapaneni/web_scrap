import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = "https://csaccelerator.com/current-companies"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the div elements with class "summary-item"
companies = soup.find_all("div", class_="row sqs-row")

# Initialize a list to store the extracted data
data = []

# Iterate over each company element
for company in companies:
    # Extract the CEO name
    try:
        ceo = company.find("div", class_="summary-title").text.strip()
    except:
        ceo = None

    # Extract the company description
    try:
        description = company.find("p", class_="white-space:pre-wrap;").text.strip()
    except:
        description =None

    # Extract the company name and website
    try:
        name_element = company.find("a")
        name = name_element.text.strip()

        website = name_element["href"]
    except:
        None

    # Append the extracted data as a dictionary to the list
    data.append({
        "Company Name": name,
        "CEO Name": ceo,
        "Description": description,
        "Website": website
    })

# Define the CSV file path
csv_file = "company_data.csv"

# Write the data to the CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Company Name", "CEO Name", "Description", "Website"])
    writer.writeheader()
    writer.writerows(data)

print("Data extracted and saved as", csv_file)
