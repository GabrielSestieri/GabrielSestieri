import time
import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, LEFT, TOP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



#The whole box of the GUI
root = tk.Tk()
root.title("LinkedIn Bot")
root.geometry("500x500")
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
    file = open('credentials.txt')
    lines = file.readlines()
    email = lines[0]
    passwd = lines[1]
    username = driver.find_element_by_id("session_key")
    username.send_keys(email)
    time.sleep(2)
    password = driver.find_element_by_id("password")
    time.sleep(2)
    password.send_keys(passwd)
    time.sleep(30)


def searchkeyword():
    '''DESCRIPTION: As soon as your're logged in, the searchleyword() function will open the search bar and based on what you have given it in the GUI 
    it will search that up through the 'People' filter.'''
    
    searchbar = driver.find_element_by_id('global-nav-typeahead').click()
    search = driver.find_element_by_class_name('search-global-typeahead__input')
    keyword = key_wrd.get() #NOTICE that the keyword variable is defined here after using the get() function that gets whatever the user inputted into the GUI.
    search.send_keys(keyword) 
    search.send_keys(Keys.RETURN)
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
    i = 0
    try:
        text = profiles[num].text
        fullname = (text.split("\n"))[0]
        firstname = (text.split("\n")[0].split(" ")[0])
        if "LinkedIn Member" not in text and "Follow" not in text:
            if profiles[num]:
                profiles[num+i].click()
                time.sleep(3)
                connect = driver.find_element_by_xpath("//button[contains(@aria-label,'Connect with')]").send_keys(Keys.RETURN)
                time.sleep(3)
                addnote = driver.find_element_by_xpath("//button[contains(@aria-label,'Add a note')]").send_keys(Keys.RETURN)
                msg = open("message.txt").read()
                writemsg = message1 = driver.find_element_by_id("custom-message").send_keys(msg)
                #send = driver.find_element_by_xpath("//button[contains(@aria-label, 'Send now')]").send_keys(Keys.RETURN)
                listofnames = open("names.txt", "a")
                listofnames.write(fullname+"\n")
                listofnames.close()
                time.sleep(3)
                driver.back()
        elif "Message" in text:
            more = driver.find_element_by_xpath("//button[contains(@aria-label,'More actions')]").send_keys(Keys.RETURN)
            connect = driver.find_element_by_xpath("//li[contains(@data-control-name,'connect')]").send_keys(Keys.RETURN)
            addnote = driver.find_element_by_xpath("//button[contains(@aria-label,'Add a note')]").send_keys(Keys.RETURN)
            msg = open("note.txt").read()
            writemsg = message1 = driver.find_element_by_id("custom-message").send_keys(msg)
            #send = driver.find_element_by_xpath("//button[contains(@aria-label, 'Send now')]").send_keys(Keys.RETURN)
            listofnames = open("names.txt", "a")
            listofnames.write(fullname+"\n")
            listofnames.close()
            time.sleep(3)
            driver.back()
        else:
            i+=1
    except:
        pass

def sendmessage():
    pass
#The search bar in the GUI along with the prompt asking what you'd like to search 
searchword = tk.Label(frame, justify=LEFT, padx=(5), pady=(5))
searchword.config(text="Who would you like to search for on LinkedIn:", font=("Helvetica", 15))
searchword.pack()
key_wrd = tk.Entry(frame, bg="white")
key_wrd.pack()

#Send a customize message (less than 300 characters)
messagebox = tk.Label(frame, justify=LEFT, padx=(5), pady=(5))
messagebox.config(text="What message would you like to send?", font=("Helvetica", 15))
messagebox.place(x = 65, y=100)
message = tk.Text(frame, bg="white")
message.place(width=350, height=200, x=25,y=150)

#The function that runs all other functions
def main():
    num = 0
    login()
    searchkeyword()
    while True:
        connect(num)
        num += 1
        if num > 9:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_xpath("//button[contains(@aria-label,'Next')]").send_keys(Keys.RETURN)
            num = 0
    
    
    

#The 'run' button on the GUI which tells the program to initiate main()
runapp = tk.Button(frame, text="Run", padx=10, pady=5, fg="black", bg="#263D42", command=main)
runapp.pack(side=BOTTOM)

#Creates the GUI
root.mainloop()

main()