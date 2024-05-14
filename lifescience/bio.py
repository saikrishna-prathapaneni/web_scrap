import csv
from bs4 import BeautifulSoup
import requests

# Send a GET request to the URL and retrieve the HTML content
html_file = "file.html"

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")

# Parse the HTML content with BeautifulSoup

# Find all the session items
session_items = soup.find_all("div", class_="oc-sessionTable__slotItem show")

# Define the CSV file path
csv_file = "session4.csv"

# Open the CSV file in write mode and create a writer object
with open(csv_file, mode="w", newline="",encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name", "Link", "Description"])

    # Iterate over each session item and extract the required information
    for track_item in soup.find_all('div', class_='mc-sessionTrack'):
        company_name = track_item.find('a', class_='af-link').text
        link = track_item.find('a', class_='af-link')['href']
        link = "https://www.bio.org"+link
        description = track_item.find('div', class_='mc-sessionTrack__description').text
        #description = session_item.find("div", class_="af-text").text.strip()

        # Write the extracted information to the CSV file
        writer.writerow([company_name, link, description])

print(f"Data has been successfully extracted and saved to {csv_file}.")
