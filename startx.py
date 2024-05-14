from bs4 import BeautifulSoup
import csv

# Assume 'html' variable contains the HTML content
# Open the HTML file and read its contents
with open('file.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html,"html.parser")



# Find all <li> elements
li_elements = soup.find_all('li')

# Create a list to store the extracted data
data = []

# Iterate over each <li> element
for li in li_elements:
    # Find the <a> element within the <li> element
    a_element = li.find('a')
    
    # Extract the company name from the website link
    try:
        company_name = a_element.get('href').split('//')[-1]
        print(company_name)
        if company_name.split('.')[0] == "www":
            company_name= company_name.split('.')[1]
        else:
            company_name = company_name.split('.')[0]

    except:
        company_name =""
    # Extract the company link
    company_link = a_element.get('href')
    
    # Add the data to the list
    data.append([company_name, company_link])

# Specify the CSV file path
csv_file = 'startx.csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Company Link'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f"Data saved to {csv_file} successfully.")
