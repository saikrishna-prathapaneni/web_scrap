import csv
import requests
from bs4 import BeautifulSoup

url = "https://evonexus.org/portfolio-companies/"

# Send a GET request to the URL
html_file = "file.html"

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")

print(soup)
# Find all the article elements
articles = soup.find_all("article", {"id": "caf-post-layout9"})

# Create a list to store the extracted data
data = []

# Extract the company name, link, and description from each article
for article in articles:
    
    company_link = article.find("a", {"class": "caf-f-link"})["href"]
    company_name = article.find("h2").text.strip()
    company_description = article.find("div", {"id": "manage-post-area"}).text.strip()

    data.append([company_name, company_link, company_description])

# Save the data as a CSV file
csv_filename = "nexus.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Company Name", "Link", "Description"])
    writer.writerows(data)

print(f"Data saved successfully as '{csv_filename}'")
