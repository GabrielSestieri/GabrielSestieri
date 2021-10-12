import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from google_play_scraper import app
import pandas as pd
search = input("What would you like to search? ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://play.google.com/store/search?q='+str(search)+'&c=apps')

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
#Finds the URL and puts it in a list
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    if "details?id" in elem.get_attribute("href"):
        links_games.append((elem.get_attribute("href")))
        
links_games = list(dict.fromkeys(links_games))
title = []
emails = []
developer = []
appID = []
#Segments the URL into the AppID only
for iteration in links_games:
    appID.append(iteration[46:])

#Using google-play-store to scrape each parameter that is asked for
for apps in appID:
    result = app(
    apps)
    title.append(result['title'])
    emails.append(result['developerEmail'])
    developer.append(result['developer'])


#Transforms into a DataFrame and outputs as an Excel Sheet
df = pd.DataFrame(list(zip(title, emails, developer)), columns=['Name', "Emails", 'Developer'])
df.to_excel(search+'_playstore_scrape.xlsx', header=True, index=False)


'''message:

Hi NAME,
Nice meeting you.
I'm reaching out as I wish to introduce you to our product VidPush that is designed for monetization and re-engagement of mobile apps.

VidPush offers 100% viewability and the ability to wow your customers with a personalized video push notification. We are the only company to date with the ability to send and play a short video within the push notification (on the device level). Here is a short video made for Playtica that showcases our product.
I'll be happy to schedule a call to discuss a possible test.
https://youtu.be/EJ9442U93c4

Best Regards
Tamar'''