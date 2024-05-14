import requests
from bs4 import BeautifulSoup
import csv
import re
# List of links
links = [
    "https://www.elabnyc.com/directory/aaron-nesser/",
    "https://www.elabnyc.com/directory/adi-wallach/",
    "https://www.elabnyc.com/directory/alauddin-bhuiyan/",
    "https://www.elabnyc.com/directory/aleksandra-gosiewski/",
    "https://www.elabnyc.com/directory/alexander-efron/",
    "https://www.elabnyc.com/directory/alia-kozlova/",
    "https://www.elabnyc.com/directory/amanda-wang/",
    "https://www.elabnyc.com/directory/ami-shah/",
    "https://www.elabnyc.com/directory/amy-kwan/",
    "https://www.elabnyc.com/directory/anais-rameau/",
    "https://www.elabnyc.com/directory/andrea-westervelt/",
    "https://www.elabnyc.com/directory/andreas-keller/",
    "https://www.elabnyc.com/directory/4941/",
    "https://www.elabnyc.com/directory/aonnicha-burapachaisri/",
    "https://www.elabnyc.com/directory/arijit-bhowmick/",
    "https://www.elabnyc.com/directory/ashley-abid/",
    "https://www.elabnyc.com/directory/assaf-raz/",
    "https://www.elabnyc.com/directory/bahram-marami/",
    "https://www.elabnyc.com/directory/baptiste-aussedat/",
    "https://www.elabnyc.com/directory/ben-young/",
    "https://www.elabnyc.com/directory/bishoy-ghobryal/",
    "https://www.elabnyc.com/directory/brad-thorson/",
    "https://www.elabnyc.com/directory/brendan-walker/",
    "https://www.elabnyc.com/directory/brian-pan/",
    "https://www.elabnyc.com/directory/brian-gillette/",
    "https://www.elabnyc.com/directory/chandrabali-ghose-paul/",
    "https://www.elabnyc.com/directory/4943/",
    "https://www.elabnyc.com/directory/charles-rodenkirch/",
    "https://www.elabnyc.com/directory/charles-platkin/",
    "https://www.elabnyc.com/directory/chichao-chen/",
    "https://www.elabnyc.com/directory/christine-denny/",
    "https://www.elabnyc.com/directory/cira-cardaci/",
    "https://www.elabnyc.com/directory/clark-sullivan/",
    "https://www.elabnyc.com/directory/craig-ramirez/",
    "https://www.elabnyc.com/directory/da-wi-shin/",
    "https://www.elabnyc.com/directory/devansh-sharma/",
    "https://www.elabnyc.com/directory/dominic-ambrosio/",
    "https://www.elabnyc.com/directory/dong-zhang/",
    "https://www.elabnyc.com/directory/dori-thomas-karyat/",
    "https://www.elabnyc.com/directory/douglass-lee/",
    "https://www.elabnyc.com/directory/eleanor-haglund/",
    "https://www.elabnyc.com/directory/elif-alpoge/",
    "https://www.elabnyc.com/directory/evan-noch/",
    "https://www.elabnyc.com/directory/furwa-hussain/",
    "https://www.elabnyc.com/directory/george-georgiev/",
    "https://www.elabnyc.com/directory/gregory-lemberskiy/",
    "https://www.elabnyc.com/directory/heayeon-lee/",
    "https://www.elabnyc.com/directory/hennesys-disla/",
    "https://www.elabnyc.com/directory/jeannette-beasley/",
    "https://www.elabnyc.com/directory/jeetayu-biswas/",
    "https://www.elabnyc.com/directory/jennifer-horonjeff/",
    "https://www.elabnyc.com/directory/john-p-wilson/",
    "https://www.elabnyc.com/directory/jon-zaikowski/",
    "https://www.elabnyc.com/directory/joongheum-park/",
    "https://www.elabnyc.com/directory/jose-bartolomei/",
    "https://www.elabnyc.com/directory/jose-quiroz/",
    "https://www.elabnyc.com/directory/josh-chodosh/",
    "https://www.elabnyc.com/directory/justin-ring/",
    "https://www.elabnyc.com/directory/kaja-wasik/",
    "https://www.elabnyc.com/directory/kelsey-mccarthy/",
    "https://www.elabnyc.com/directory/khatija-ali/",
    "https://www.elabnyc.com/directory/krista-fretes/",
    "https://www.elabnyc.com/directory/kurt-yaeger/",
    "https://www.elabnyc.com/directory/laura-beth-mcintire/",
    "https://www.elabnyc.com/directory/laurence-coman/",
    "https://www.elabnyc.com/directory/lingbo-zhang/",
    "https://www.elabnyc.com/directory/lorena-padro-cortes/",
    "https://www.elabnyc.com/directory/loune-calixte/",
    "https://www.elabnyc.com/directory/4944/",
    "https://www.elabnyc.com/directory/luis-santos/",
    "https://www.elabnyc.com/directory/mamnun-jaigirdar/",
    "https://www.elabnyc.com/directory/manoj-pooleery/",
    "https://www.elabnyc.com/directory/marcelo-cespedes/",
    "https://www.elabnyc.com/directory/mario-castellanos/",
    "https://www.elabnyc.com/directory/mark-stewart/",
    "https://www.elabnyc.com/directory/mark-hase/",
    "https://www.elabnyc.com/directory/maryam-alkhaldi/",
    "https://www.elabnyc.com/directory/matthew-levy/",
    "https://www.elabnyc.com/directory/max-signaevsky/",
    "https://www.elabnyc.com/directory/meshal-alhathal/",
    "https://www.elabnyc.com/directory/mgavi-brathwaite/",
    "https://www.elabnyc.com/directory/mican-meneses/",
    "https://www.elabnyc.com/directory/michelle-roberts/",
    "https://www.elabnyc.com/directory/miriam-boer/",
    "https://www.elabnyc.com/directory/mo-chen/",
    "https://www.elabnyc.com/directory/nan-xiao/",
    "https://www.elabnyc.com/directory/nathan-stevens/",
    "https://www.elabnyc.com/directory/nayoung-yang/",
    "https://www.elabnyc.com/directory/nigel-kelly/",
    "https://www.elabnyc.com/directory/nini-fan/",
    "https://www.elabnyc.com/directory/parth-shah/",
    "https://www.elabnyc.com/directory/paul-booth/",
    "https://www.elabnyc.com/directory/peilin-zhang/",
    "https://www.elabnyc.com/directory/prakrit-jena/",
    "https://www.elabnyc.com/directory/4940/",
    "https://www.elabnyc.com/directory/raymond-alvarez/",
    "https://www.elabnyc.com/directory/rebecca-brachman/",
    "https://www.elabnyc.com/directory/rena-orman/",
    "https://www.elabnyc.com/directory/reza-royaee/",
    "https://www.elabnyc.com/directory/rom-cohen/",
    "https://www.elabnyc.com/directory/rotem-lev-zwickel/",
    "https://www.elabnyc.com/directory/ryan-malonis/",
    "https://www.elabnyc.com/directory/4942/",
    "https://www.elabnyc.com/directory/sam-cho/",
    "https://www.elabnyc.com/directory/selin-kurnaz/",
    "https://www.elabnyc.com/directory/seth-harlem/",
    "https://www.elabnyc.com/directory/seth-goodman/",
    "https://www.elabnyc.com/directory/shin-ying-wu/",
    "https://www.elabnyc.com/directory/sonia-gonzalez/",
    "https://www.elabnyc.com/directory/sunit-jariwala/",
    "https://www.elabnyc.com/directory/sunniekenowsky/",
    "https://www.elabnyc.com/directory/susannah-bailin/",
    "https://www.elabnyc.com/directory/tal-herman/",
    "https://www.elabnyc.com/directory/tessa-callaghan/",
    "https://www.elabnyc.com/directory/thandiwe-kesirobins/",
    "https://www.elabnyc.com/directory/vadim-gordin/",
    "https://www.elabnyc.com/directory/vanessa-siverls/",
    "https://www.elabnyc.com/directory/waleed-abdel-naby/",
    "https://www.elabnyc.com/directory/wesley-alexis/",
    "https://www.elabnyc.com/directory/william-walkowics/",
    "https://www.elabnyc.com/directory/yair-saperstein/",
    "https://www.elabnyc.com/directory/youngtae-seo/"
]
pattern = re.compile(r'Website')
# CSV file path to save the extracted data
csv_file = "output.csv"

# Open CSV file in write mode
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name", "Company Link", "Participant Name", "LinkedIn", "Description"])

    # Iterate over the links
    for link in links:
        # Fetch HTML content from the link
        response = requests.get(link)
        html_content = response.text

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract required information
        company_name = soup.find("div", class_="mc-ats-business-name").text.strip()
        print(company_name)
        try:
            company_link = soup.find("h3",string=pattern).find_next('a')["href"]
        except:
            company_link=None
        participant_name = soup.find('div',class_="fl-col fl-node-5a395ecce96cf fl-col-small mc-ats-participant-details").find('h3',class_='fl-heading').find("span", class_="fl-heading-text").text.strip()
     
        try:
            linkedin = soup.find("a", class_="mc-ats-directory-linkedin-icon")["href"]
        except:
            linkedin=None
        try:
            description = soup.find("div", class_="fl-col fl-node-5a395ecce96ec fl-col-small").find('div',class_='fl-rich-text').find('p').text.strip()
        except:
            description= None
        # Write the extracted data to CSV
        writer.writerow([company_name, company_link, participant_name, linkedin, description])

print("Data extraction and CSV creation completed!")
