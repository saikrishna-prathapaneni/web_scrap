import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

# List of links
# List of links
links = [
    "https://sosv.com/portfolio/simply-good-jars",
    "https://sosv.com/portfolio/halla",
    "https://sosv.com/portfolio/true-made-foods",
    "https://sosv.com/portfolio/freshspoke",
    "https://sosv.com/portfolio/uplift-food",
    "https://sosv.com/portfolio/bizzy-coffee",
    "https://sosv.com/portfolio/rambuhealth",
    "https://sosv.com/portfolio/fieldcraft",
    "https://sosv.com/portfolio/planetarians",
    "https://sosv.com/portfolio/global-belly",
    "https://sosv.com/portfolio/re-nuble",
    "https://sosv.com/portfolio/bramble",
    "https://sosv.com/portfolio/foodcloud",
    "https://sosv.com/portfolio/servy",
    "https://sosv.com/portfolio/wasteless",
    "https://sosv.com/portfolio/abbots-butcher",
    "https://sosv.com/portfolio/foodie-for-all",
    "https://sosv.com/portfolio/livekuna",
    "https://sosv.com/portfolio/mori",
    "https://sosv.com/portfolio/eio-diagnostics",
    "https://sosv.com/portfolio/entr",
    "https://sosv.com/portfolio/givn-goods",
    "https://sosv.com/portfolio/ingest-ai",
    "https://sosv.com/portfolio/kojo",
    "https://sosv.com/portfolio/millennia-tea",
    "https://sosv.com/portfolio/plasma-nutrition",
    "https://sosv.com/portfolio/tasting-collective",
    "https://sosv.com/portfolio/abbys-better",
    "https://sosv.com/portfolio/sweetie-pie-organics",
    "https://sosv.com/portfolio/freshsurety",
    "https://sosv.com/portfolio/hidden-gems-beverage-company",
    "https://sosv.com/portfolio/milk-moovement",
    "https://sosv.com/portfolio/living-food-company",
    "https://sosv.com/portfolio/lula-inc",
    "https://sosv.com/portfolio/tinychef",
    "https://sosv.com/portfolio/tru-inc",
    "https://sosv.com/portfolio/amp-your-good",
    "https://sosv.com/portfolio/mushroom-cups",
    "https://sosv.com/portfolio/booster-agtech",
    "https://sosv.com/portfolio/paragon-pure",
    "https://sosv.com/portfolio/bite",
    "https://sosv.com/portfolio/vaartani",
    "https://sosv.com/portfolio/farma-genetics-inc",
    "https://sosv.com/portfolio/nature-preserve",
    "https://sosv.com/portfolio/nonfood",
    "https://sosv.com/portfolio/rxdiet"
]

# Create a Selenium WebDriver instance
driver = webdriver.Chrome()

# Extract company website links
websites = []
for link in links:
    driver.get(link)
    website_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.single-company-header__website')))
    website_url = website_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
    websites.append(website_url)

# Close the WebDriver
driver.quit()

# Save as CSV
csv_file = "company_websites.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'Website'])
    for link, website in zip(links, websites):
        writer.writerow([link, website])

print("CSV file saved successfully!")
