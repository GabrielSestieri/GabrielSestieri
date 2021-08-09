import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from google_play_scraper import app
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://play.google.com/store/search?q=games&c=apps')

time.sleep(10)

SCROLL_PAUSE_TIME = 5
 
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
time.sleep(SCROLL_PAUSE_TIME)
 
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
 
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

links_games = []
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    if "details?id" in elem.get_attribute("href"):
        links_games.append((elem.get_attribute("href")))
        
links_games = list(dict.fromkeys(links_games))
title = []
emails = []
installs = []
ratings = []
appID = []
for iteration in links_games:
    appID.append(iteration[46:])

for apps in appID:
    result = app(
    apps)
    title.append(result['title'])
    emails.append(result['developerEmail'])
    installs.append(result['installs'])
    ratings.append(result['ratings'])


df = pd.DataFrame(list(zip(title, emails, installs, ratings)), columns=['Name', "Emails", "Installs", "Ratings"])
df.to_excel('playstore_scrape.xlsx', header=True, index=False)
