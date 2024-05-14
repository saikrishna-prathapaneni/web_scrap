import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

html_file = "file.html"

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")



# Find all list item elements
list_items = soup.find_all("li")

# Open the CSV file in append mode
with open("nih4.csv", "a", newline="") as file:
    writer = csv.writer(file)

    # Iterate over the list items
    for list_item in list_items:
        # Extract company name
        company_name = list_item.find("a").text

        # Extract relative link
        anchor_tags = list_item.find_all("a")

        # Check if there are at least two anchor tags
        if len(anchor_tags) >= 2:
            # Extract the second anchor tag and its link
            second_anchor = anchor_tags[1]
            link = second_anchor.get("href")

        # Create the full link by joining the base URL and the relative link
        #full_link = urljoin(url, relative_link)

        # Extract description
        description = list_item.find("p").text

        # Write the extracted information to the CSV file
        writer.writerow([company_name, link, description])

