import csv
import requests
from bs4 import BeautifulSoup

url = "https://enterpriseleague.com/blog/biotech-startups/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
startup_elements = soup.select("[class*='et_pb_module et_pb_text']")


print(len(startup_elements))
data = []
for element in startup_elements:
    try:
        name = element.find("a").text.strip()
        link = element.find("a")["href"]
        description = element.find_all("p")[0].text.strip()
    except:
        pass
    data.append([name, link, description])

# Save data as a CSV file
csv_filename = "enterprise.csv"
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Startup Name", "Startup Link", "Description"])
    writer.writerows(data)

print(f"Data saved to {csv_filename}.")
