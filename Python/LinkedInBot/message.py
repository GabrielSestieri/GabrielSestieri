import time
import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, LEFT, TOP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
def login():
    '''DESCRIPTION:The login() function takes the url and passes it to the driver (gets you to linked in). 
    It then reads your email/password from the linkedin.txt file and provides that to the driver.'''
    
    url = 'http://linkedin.com'   
    driver.get(url)
    file = open('credentials.txt')
    lines = file.readlines()
    email = lines[0]
    passwd = lines[1]
    username = driver.find_element_by_id("session_key")
    username.send_keys(email)
    time.sleep(2)
    password = driver.find_element_by_id("session_password")
    time.sleep(2)
    password.send_keys(passwd)
    password.send_keys(Keys.RETURN)
    time.sleep(3)
    
def network():
    mynetwork = driver.find_element_by_xpath("//a[contains(@data-control-name,'nav_mynetwork')]").click()
    connections = driver.find_element_by_css_selector('href./mynetwork/import-contacts/saved-contacts/').click()
    profiles = driver.find_elements_by_class_name('reusable-search__result-container')
    profilestxt = profiles.text
    print(profilestxt)
    
    

login()
network()