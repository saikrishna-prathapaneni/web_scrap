import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://upwest.vc/portfolio/"
html_file = "file.html"

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")



company_elements = soup.find_all("div", class_="portfolio--modal-slide")
company_data = []

for element in company_elements:
    company_name = element.get("data-name")
    company_description = element.find("div", class_="content").find("p").text
    try:
        company_link = element.find("a", class_="btn").get("href")
    except:
        None
    company_data.append([company_name, company_description, company_link])

df = pd.DataFrame(company_data, columns=["Company Name", "Description", "Link"])
df.to_csv("upwest.csv", index=False)
