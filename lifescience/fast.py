from bs4 import BeautifulSoup

html_content = '''
<article class="post__article">
  <div>
    <p><em>Explore the full 2022 list of </em><em><a href="https://www.fastcompany.com/most-innovative-companies/list" target="_blank" rel="noopener noreferrer">Fast Company’s Most Innovative Companies</a>, 528 organizations whose efforts are reshaping their businesses, industries, and the broader culture. We’ve selected the firms making the biggest impact with their initiatives across 52 categories, including the most innovative <a href="https://www.fastcompany.com/90724444/most-innovative-companies-medical-devices-2022" target="_blank" rel="noopener noreferrer">medical device</a>, <a href="https://www.fastcompany.com/90724447/most-innovative-companies-medicines-therapeutics-2022" target="_blank" rel="noopener noreferrer">medicines and therapeutics</a>, and <a href="https://www.fastcompany.com/90717458/most-innovative-companies-consumer-goods-2022" target="_blank" rel="noopener noreferrer">consumer goods</a>&nbsp;companies.</em></p>
  </div>
  <div></div>
  <div class="adInserts_0">
    <div class="ad-unit-wrap-native">
      <div class="ad-wrapper ad-wrapper--native_mid_article">
        <div id="native_mid_article_5962230946" class="adElement camp-native_mid_article" data-ad_slot_type="native_mid_article" data-page="1" data-instance="1" data-slot_base_id="native_mid_article_1_1" data-refresh_count="1"></div>
      </div>
    </div>
  </div>
  <div>
    <p>The most innovative companies in biotech this year expand R&amp;D capabilities for researchers in the lab and online, enable more precise and inclusive diagnostic tests, and offer new paradigms for everything from drug development to the maintenance of healthy soils for agriculture. Emulate, for example, added to its arsenal of organs-on-a-chip with in vitro models of the colon and the brain, permitting new ways of studying intestinal inflammation and testing drug candidates that can pierce the blood-brain barrier. DNA Script employs a new process called enzymatic DNA synthesis (EDS) in its benchtop DNA printers, allowing scientists to create longer strands of DNA than traditional DNA synthesis on demand. TMRW Life Sciences is modernizing the IVF clinic with an automated, robotic platform for safe storage and efficient retrieval of frozen eggs and embryos. Notable advances in diagnosing cancer and guiding treatments come from Strata Oncology, which launched a new assay for solid tumors that requires significantly smaller tissue samples for genomic profiling, and Myriad, which updated its genetic test for breast cancer risk to include risk assessments for more diverse populations. LightDeck and SafeTraces developed new ways of quickly detecting COVID-19 and other pathogens in patient samples or circulating through large buildings. Bringing a portfolio model to its diverse drug-development program, BridgeBio Pharma attained two FDA approvals for new drugs last year, making it the smallest drugmaker to earn more than one nod from the agency. Benchling’s launch of a cloud R&amp;D platform for life sciences helped accelerate research in mRNA underlying new COVID-19 treatments. And Biome Makers applied genomic sequencing to soil, analyzing the microbiomes of farmland to help farmers measure the impact of fertilizers, biological inputs, and other management practices on crop health, soil fertility, and crop productivity. These companies, selected by Fast Company editors, represent the vanguard of biotechnology today, and in the coming decade.</p>
  </div>
  <div></div>
  <div></div>
</article>
'''

soup = BeautifulSoup(html_content, 'html.parser')

company_list = []

# Find the <p> tag containing the company descriptions
description_p = soup.find('p')

if description_p:
    company_descriptions = description_p.find_all_next('p')
    
    for description in company_descriptions:
        # Extract the company name, description, and link
        company_name = description.find('a')
        if company_name:
            company_name = company_name.text.strip()
            company_link = company_name['href']
        
        company_description = description.text.strip()
        
        if company_name and company_description and company_link:
            company_list.append({
                'name': company_name,
                'description': company_description,
                'link': company_link
            })

# Print the extracted company names, descriptions, and links
for company in company_list:
    print('Company Name:', company['name'])
    print('Description:', company['description'])
    print('Link:', company['link'])
    print('---')
