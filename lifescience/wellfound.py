import csv
import requests
from bs4 import BeautifulSoup
# Read the HTML file


html_file ="file.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")


company_elements = soup.find_all(class_="styles_editorial__uDcY5")

data = []
for element in company_elements:
    name = element.find("div", class_="inline-flex flex-row items-center relative border border-gray-400 bg-gray-100 rounded-md h-18 w-18").find("img")["alt"]
    link_element = element.find("a", class_="styles_component__UCLp3 styles_defaultLink__eZMqw")
    
    link = link_element["href"]
    print(link_element)
    location_element = element.find("dt", text="Locations")
    if location_element:
        locations = [a.text for a in location_element.find_next("dd").find_all("a", class_="styles_component__UCLp3 styles_defaultLink__eZMqw !text-gray-800")]
        location = ", ".join(locations)
    else:
        location = ""
    description = element.find("div", class_="styles_component__481pO").text.strip()
    data.append([name, link, location, description])

# Save data as a CSV file
csv_filename = "wellfound1.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name", "Company Link", "Location", "Description"])
    writer.writerows(data)

print(f"Data saved to {csv_filename}.")
