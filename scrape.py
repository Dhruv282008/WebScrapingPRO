from selenium import webdriver
from bs4 import BeautifulSoup

import time
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('C:/DHRUV Whitehat PROJECTS/WebScraping1/chromedriver')
browser.get(start_url)

time.sleep(10)

def scraper():
    headers = ["Name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 1):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul"):
            li_tags = ul_tag.find_all("li")
            temp_list = []

        for index, li_tag in enumerate(li_tags):
            if(index == 0):
                temp_list.append(li_tag.find_all("a")[0].contents[0])

            else:
                try:
                    temp_list.append(li_tag.contents[0])

                except:
                    temp_list.append("")

        star_data.append(temp_list)


    with open("WebScraper1.csv", "w")as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(star_data)

scraper()
