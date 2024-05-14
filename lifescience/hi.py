from bs4 import BeautifulSoup
import csv

html = '''
<div class="grid-row">

            <!--fwp-loop-->

                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/accessible-bio/"><h3>Accessible Bio</h3></a>                                    </header>
                                    We are building a B2B platform that enables industry biologist to run machine learning workflows at a low cost and without having to be an expert AI.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/acurasset-inc/"><h3>Acurasset, Inc.</h3></a>                                    </header>
                                    Developing a cure for Hepatitis B virus that could rid patients of the virus within months.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/alvus-health/"><h3>Alvus Health</h3></a>                                    </header>
                                    Alvus Health develops target identification and drug discovery platform by AI and high-throughput patient-derived organoids.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/artyx/"><h3>ARTyx</h3></a>                                    </header>
                                    At ARTyx, we are developing an innovative RNA therapeutic platform for cancer treatment, with an initial focus on Breast Cancer.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/believer-pharmaceuticals-inc/"><h3>Believer Pharmaceuticals Inc</h3></a>                                    </header>
                                    We are developing a novel therapy for hard-to-treat cancers.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/clearsky/"><h3>ClearSky</h3></a>                                    </header>
                                    ClearSky serves as a crucial tool in assisting people with vision problem and help improve the quality of safety and efficiency.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/coolr/"><h3>COOLR</h3></a>                                    </header>
                                    COOLR is a cooling device that is wrapped around athlete?s temperature-sensitive spots to lower internal body temperature and thus avoid overheating.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/dart-biosciences/"><h3>Dart Biosciences</h3></a>                                    </header>
                                    Dart Biosciences is developing personalized gene therapies for an array of rare and common diseases.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/dorivac/"><h3>DoriVac</h3></a>                                    </header>
                                    DoriVac (DNA Origami Vaccine) is a biotech startup developing novel cancer treatments using DNA nanotechnology.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/embedx-bio/"><h3>EmbedX Bio</h3></a>                                    </header>
                                    We filed IP on a novel bioprinting method for applications in disease modeling and the scalable generation of human tissues and organs.
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/experiment-researchtodate/"><h3>Experiment: ResearchToDate</h3></a>                                    </header>
                                    Find accurately curated summaries about research in your field and ideas of what could or needs to come next for medical discoveries on Experiment
                                </div>

                            </div>
                        </div>


                    
                    <div class="col-width-large-1-3 col-width-medium-1-2">
                            <div class="jewelbox default venture-team-list  bottom-aligned has-background-img">


                                                                    <div class="inner" style="background-image:url(https://i-lab.harvard.edu/innolabs/wp-content/uploads/sites/5/2017/05/stock-ilab-exterior-1024x633.jpg)">

                                    </div>
                                    



                                <div class="window-shade">
                                    <header>
                                        <a href="https://innovationlabs.harvard.edu/current-team/freyas-gift/"><h3>Freya’s Gift</h3></a>                                    </header>
                                    Our venture develops next-generation microbiome therapeutics that leverages microbial bioactivation of dietary factors to treat infection and disease.
                                </div>

                            </div>
                        </div>


                    

            </div>
'''

soup = BeautifulSoup(html, 'html.parser')

data = []
company_elements = soup.find_all('div', class_='col-width-large-1-3 col-width-medium-1-2')
print(company_elements)
for company_element in company_elements:
    link = company_element.find('a')['href']
    name = company_element.find('h3').text.strip()
    description = company_element.find('div', class_='window-shade').text.strip()
    data.append([name, link, description])

# Save data as CSV
with open('hi.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company Name', 'Link', 'Description'])
    writer.writerows(data)
