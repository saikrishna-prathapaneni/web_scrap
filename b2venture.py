from bs4 import BeautifulSoup
import csv

# Read the content of the HTML file
with open("file.html", "r", encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all the div elements with the specified class
div_elements = soup.find_all("div", class_="collection-item-2 w-dyn-item")

# Store the data in a CSV file
csv_filename = "b2v.csv"

with open(csv_filename, mode="w", newline="",encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Company Name", "Link", "Year Founded", "Description"])

    for div_element in div_elements:
        # Extract relevant information for each div element
        company_name = div_element.find("div", class_="headline-05 weight--semibold").text.strip()
        link = div_element.find("a", class_="portfolio-table-grid").get("href")
        year_founded = div_element.find("div", attrs={"fs-cmssort-field": "year"}).text.strip()
        description = div_element.find("div", class_="portfolio-description").text.strip()

        # Write the data to the CSV file
        writer.writerow([company_name, link, year_founded, description])

print(f"Data extracted and saved to {csv_filename}.")
