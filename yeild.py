import requests
from bs4 import BeautifulSoup
import csv
url = "https://upwest.vc/portfolio/"
html_file = "file.html"

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")


# Find all the desired HTML elements
elements = soup.find_all("div", class_="info-element-text")

# Define the CSV file path
csv_file = "yeild.csv"

# Write the data to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name", "Description"])

    # Iterate over the elements and extract the data
    for element in elements:
        print(element)
        
        company_name = element.find("div", class_="info-member info-element-title").text.strip()
        try:
            company_description = element.find("div", class_="info-member info-element-description").text.strip()
        except:
            company_description =None
        
        writer.writerow([company_name, company_description])

print("Data saved to", csv_file)
