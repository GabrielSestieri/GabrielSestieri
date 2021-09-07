import time
import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, LEFT, TOP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



#The whole box of the GUI
root = tk.Tk()
root.title("LinkedIn Bot")
root.geometry("350x350")
root.resizable(False, False)

#The title bar of the GUI
title = tk.Label(root, fg="White", bg="#0077b5")
title.config(text="LinkedIn Employee Search", font=("Helvetica", 20))
title.pack(side=TOP)

#The center box of the GUI
frame = tk.Frame(root, bg="#0077b5")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

#'driver' is Google Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
def login():
    '''DESCRIPTION:The login() function takes the url and passes it to the driver (gets you to linked in). 
    It then reads your email/password from the linkedin.txt file and provides that to the driver.'''
    
    url = 'http://linkedin.com'   
    driver.get(url)
    file = open('linkedin.txt')
    lines = file.readlines()
    email = lines[0]
    passwd = lines[1]
    username = driver.find_element_by_id("session_key")
    username.send_keys(email)
    password = driver.find_element_by_id("session_password")
    time.sleep(2)
    password.send_keys(passwd)
    #driver.find_element_by_class_name('sign-in-form__submit-button').click()

def searchkeyword():
    '''DESCRIPTION: As soon as your're logged in, the searchleyword() function will open the search bar and based on what you have given it in the GUI 
    it will search that up through the 'People' filter.'''
    
    searchbar = driver.find_element_by_id('global-nav-typeahead').click()
    search = driver.find_element_by_class_name('search-global-typeahead__input')
    keyword = key_wrd.get() #NOTICE that the keyword variable is defined here after using the get() function that literally gets whatever the user inputted into the GUI.
    search.send_keys(keyword) 
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    time.sleep(2)
    peoplefilter = driver.find_element_by_xpath("//button[contains(@aria-label, 'People')]").click()
    
def connect(num):
    '''DESCRIPTION: When you have reached the People page based on what you searched, 
    the connect() function will (if it isn't an unaccessable "LinkedIn Member") click the profile at the top of the list.
    It will then go back a page and add +1 to the variale 'num' each time, indicating the program to go down the list and connect. 
    Each connection will be sent a message along with it's connection'''
    
    time.sleep(3)
    profiles = driver.find_elements_by_class_name('reusable-search__result-container')
    time.sleep(3)
    text = profiles[num].text
    i = 1
    try:
        if "LinkedIn Member" not in text:
            profiles[num].click()
            time.sleep(3)
            connect = driver.find_element_by_class_name('pvs-profile-actions__action').send_keys(Keys.RETURN)
            time.sleep(3)
            addnote = driver.find_element_by_xpath("//button[contains(@aria-label,'Add a note')]").send_keys(Keys.RETURN)
            message1 = driver.find_element_by_id("custom-message").send_keys(".הי, נעים להכיר\n")
            message2 = driver.find_element_by_id("custom-message").send_keys(".במערך אבטחת המידע והגנת הסייבר בחטיבת הטכנולוגיה בבנק הפועלים נפתחו מס משרות שאולי יכולים לעניין אותך\n")
            message3 = driver.find_element_by_id("custom-message").send_keys(".להלן קישור לאתר שמסביר קצת עלינו ועל המשרות הפתוחות במערך\n")
            message4 = driver.find_element_by_id("custom-message").send_keys("https://wearestuff.co/cyber-poalim/\n")
            message5 = driver.find_element_by_id("custom-message").send_keys(",בברכה")
            message6 = driver.find_element_by_id("custom-message").send_keys("\nדוד\n")
            time.sleep(3)
            send = driver.find_element_by_xpath("//button[contains(@aria-label, 'Send now')]").send_keys(Keys.RETURN)
        else:
            profiles[num+i].click() #NOTICE that +i tells the program to skip this profile and go down to the next listing
            time.sleep(3)
            connect = driver.find_element_by_class_name('pvs-profile-actions__action').send_keys(Keys.RETURN)
            time.sleep(3)
            addnote = driver.find_element_by_xpath("//button[contains(@aria-label,'Add a note')]").send_keys(Keys.RETURN)
            message1 = driver.find_element_by_id("custom-message").send_keys(".הי, נעים להכיר\n")
            message2 = driver.find_element_by_id("custom-message").send_keys(".במערך אבטחת המידע והגנת הסייבר בחטיבת הטכנולוגיה בבנק הפועלים נפתחו מס משרות שאולי יכולים לעניין אותך\n")
            message3 = driver.find_element_by_id("custom-message").send_keys(".להלן קישור לאתר שמסביר קצת עלינו ועל המשרות הפתוחות במערך\n")
            message4 = driver.find_element_by_id("custom-message").send_keys("https://wearestuff.co/cyber-poalim/\n")
            message5 = driver.find_element_by_id("custom-message").send_keys(",בברכה")
            message6 = driver.find_element_by_id("custom-message").send_keys("\nדוד\n")
            send = driver.find_element_by_xpath("//button[contains(@aria-label, 'Send now')]").send_keys(Keys.RETURN)
            time.sleep(5)
    except:
        pass
    i += 1
    driver.back()
    
#The search bar in the GUI along with the prompt asking what you'd like to search 
searchword = tk.Label(frame, justify=LEFT, padx=(10), pady=(10))
searchword.config(text="What would you like to search on LinkedIn:", font=("Helvetica", 15))
searchword.pack()
key_wrd = tk.Entry(frame, bg="white")
key_wrd.pack()


#The function that runs all other functions
def main():
    count = 0
    login()
    searchkeyword()
    while True:
        connect(count)
        count += 1

#The 'run' button on the GUI which tells the program to initiate main()
runapp = tk.Button(frame, text="Run", padx=10, pady=5, fg="black", bg="#263D42", command=main)
runapp.pack(side=BOTTOM)

#Creates the GUI
root.mainloop()

main()