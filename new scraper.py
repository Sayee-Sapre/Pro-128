from bs4 import BeautifulSoup
import time
import requests 
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_scraper = []

def scrape_more_data(tables):
    page = requests.get(tables)
    soup = BeautifulSoup(page.content,"html.parser")
    temp_list = []

    for tr_tag in soup.find_all("tr",attrs = {"class","fact_row"}):
        td_tag = tr_tag.find_all("td")
        for td_tag in td_tag:
            temp_list.append(td_tag.find_all("div"),attrs ={"class","value"})[0].contents[0]



