import requests
import csv
from bs4 import BeautifulSoup
import re
links = [
    "https://xrcventures.com/123-baby-box",
    "https://xrcventures.com/adrich",
    "https://xrcventures.com/ash-wellness",
    "https://xrcventures.com/avi-health",
    "https://xrcventures.com/avec",
    "https://xrcventures.com/axius",
    "https://xrcventures.com/barb",
    "https://xrcventures.com/billie",
    "https://xrcventures.com/bluue",
    "https://xrcventures.com/bobblehaus",
    "https://xrcventures.com/reveal",
    "https://xrcventures.com/caraa",
    "https://xrcventures.com/cartogram",
    "https://xrcventures.com/cherry-pick",
    "https://xrcventures.com/clear-health",
    "https://xrcventures.com/cluey",
    "https://xrcventures.com/creator-nova",
    "https://xrcventures.com/curie",
    "https://xrcventures.com/dappback",
    "https://xrcventures.com/endear",
    "https://xrcventures.com/facenote",
    "https://xrcventures.com/feather-bone",
    "https://xrcventures.com/ffora",
    "https://xrcventures.com/fillogic",
    "https://xrcventures.com/findmine",
    "https://xrcventures.com/fitted",
    "https://xrcventures.com/frenzy",
    "https://xrcventures.com/furnishr",
    "https://xrcventures.com/gather-ai",
    "https://xrcventures.com/globe-thrivers",
    "https://xrcventures.com/charlieai",
    "https://xrcventures.com/hemster",
    "https://xrcventures.com/hilos",
    "https://xrcventures.com/holi-chow",
    "https://xrcventures.com/homefield",
    "https://xrcventures.com/joymode",
    "https://xrcventures.com/juniver",
    "https://xrcventures.com/kanduai",
    "https://xrcventures.com/kashew",
    "https://xrcventures.com/lexset",
    "https://xrcventures.com/loomia",
    "https://xrcventures.com/thelobby",
    "https://xrcventures.com/macondo-vision",
    "https://xrcventures.com/mademebuyit",
    "https://xrcventures.com/mayawell",
    "https://xrcventures.com/md-integrations",
    "https://xrcventures.com/medsnow",
    "https://xrcventures.com/melibio",
    "https://xrcventures.com/minu",
    "https://xrcventures.com/mystore",
    "https://xrcventures.com/naked-sundays",
    "https://xrcventures.com/naniderm",
    "https://xrcventures.com/nimbly",
    "https://xrcventures.com/nuudii",
    "https://xrcventures.com/orthofx",
    "https://xrcventures.com/outlines",
    "https://xrcventures.com/pathr-ai",
    "https://xrcventures.com/pockyt",
    "https://xrcventures.com/pod-foods",
    "https://xrcventures.com/proper-good",
    "https://xrcventures.com/qatch",
    "https://xrcventures.com/radbutter",
    "https://xrcventures.com/radd",
    "https://xrcventures.com/raydiant",
    "https://xrcventures.com/recurate",
    "https://xrcventures.com/reflektme",
    "https://xrcventures.com/resist",
    "https://xrcventures.com/returnity",
    "https://xrcventures.com/sanguina",
    "https://xrcventures.com/sapyen",
    "https://xrcventures.com/scent-lab",
    "https://xrcventures.com/sequencing",
    "https://xrcventures.com/share-club",
    "https://xrcventures.com/shopshops",
    "https://xrcventures.com/simplista",
    "https://xrcventures.com/snappy",
    "https://xrcventures.com/socalytix",
    "https://xrcventures.com/solawave",
    "https://xrcventures.com/sowell-health",
    "https://xrcventures.com/stabl",
    "https://xrcventures.com/storedna",
    "https://xrcventures.com/stryde",
    "https://xrcventures.com/suggestic",
    "https://xrcventures.com/sweet-chameleon",
    "https://xrcventures.com/swivel-beauty",
    "https://xrcventures.com/tags-commerce",
    "https://xrcventures.com/teleperson",
    "https://xrcventures.com/terra-kaffe",
    "https://xrcventures.com/thesis",
    "https://xrcventures.com/trade-monday",
    "https://xrcventures.com/veeve",
    "https://xrcventures.com/viewlabs",
    "https://xrcventures.com/villie",
    "https://xrcventures.com/viveat",
    "https://xrcventures.com/wear",
    "https://xrcventures.com/youmecare"
]

pattern = re.compile(r'Website')
company_data = []

for link in links:
    response = requests.get(link)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    company_name = soup.find('strong').text.strip()
    
    try:
        company_link = soup.find('a', href=True,text=pattern).get('href')
    except:
        company_link= None
    description = soup.find('h3').text.strip()
    try:
        ceo_name = soup.find('div', class_='summary-title').text.strip()
    except:
        ceo_name=None
    company_data.append({
        'company_name': company_name,
        'company_link': company_link,
        'description': description,
        'ceo_name': ceo_name
    })

# Save data as CSV
filename = 'xrc.csv'
fieldnames = ['company_name', 'company_link', 'description', 'ceo_name']

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(company_data)

print(f"Data saved successfully to {filename}.")
