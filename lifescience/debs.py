import requests
from bs4 import BeautifulSoup

url = "https://deerfield.com/?q=portfolio%20companies&sort_field%5Bposts%5D=sortable_title&sort_direction%5Bposts%5D=asc&view=list&archive=companies"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

print(soup)
# Find all the buttons containing the company information
buttons = soup.find_all("button", class_="st-result openModalItem active aos-init aos-animate")

print(len(buttons))
# Iterate over each button and extract the company details
for button in buttons:
    # Extract the company name
    company_name = button.find("div", class_="st-result__title").text.strip()
    
    # Extract the company link
    company_link = "https://deerfield.com" + button["data-url"]
    
    # Click the button to open the side window pop-up and get the description
    popup_url = "https://deerfield.com" + button["data-url"]
    popup_response = requests.get(popup_url)
    popup_soup = BeautifulSoup(popup_response.content, "html.parser")
    description = popup_soup.find("div", class_="entry-content").p.text.strip()
    
    # Print the extracted information
    print("Company Name:", company_name)
    print("Company Link:", company_link)
    print("Description:", description)
    print("--------------------")
