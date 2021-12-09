# Gabriel Sestieri
This is where I will be adding and working on projects and scripts in my free time to build a portfolio. 

## Python

	1. Connect4
		A simple Connect 4 game.

	2. Drug Interaction
		Uses requests to access the NIH interaction API, cross references
		interactions of specified drug, and outputs all interactions into a
		new text file.

	3. Hangman
		A simple hangman game that generates a random word from a text file
		and gives the user three tries to guess it.
	
	4. Basketball Predictor
		Allows the user to input two NBA teams and will output several bar
		graphs comparing team stats and a pie char predicting who would win
		between the two. teams based on stats.

	5. Robot Fight
		A rudimentary robot fight simulation containing two classes. 
		
	6. Server/Client
		A basic client and server chat network.
	
	7. Data Challenge '21
		Refer to the Data Challenge Section.
	8. Keylogger
		A keylogged built using pynput. Also cleans the file from its raw format. 
		Will add email capabilities in the future and more slickness.
		
	9. Google Play Store Scraper
		A scraper built using Selenium and the 'google-play-scraper' pyp package. 
		The program will use Selenium to scrape each app ID and then using
		a for-loop will feed each ID to the google-play-scraper package which will 
		scrape each Title, Developer Email, and Company Name for each 
		app found on the Google Play Store. Outputs the results into an Excel sheet.
		
	10. LinkedIn Bot
		Using Selenium this bot will log in to a LinkedIn account using the provided 
		credenials from 'linkedin.txt'. Then, based on the search entry from the Tkinter 
		GUI will search a job role through the 'People' filter of LinkedIn.
		It will then automatically connect with all possible people fitting that criteria 
		and send them a custom note. For example, typing 'Senior Java Developer' will 
		search for every person you can connect to that has that description in their profile
		and automatically send them a message and connect with them. 
		
## C
A collection of labs and projects I completed in my CMSC106 course.

## JavaScript
This is where all my worthy JavaScript projects are showcased. They are subject to constant updates.

	1. CrimeTracker
		A webapp that uses Google Maps' API and Prince George's county
		crime data to pinpoint crime around a given address. Can be
		filtered based on crimes. Has bugs.

## DataChallenge '21
Data Challenge is an annual week-long data exploration event at the University of Maryland hosted by The College of Information Studies.

During the week, UMD students will gain analytical experience by solving challenging problems exploring novel datasets, build technical aptitude integrating datasets to create multidisciplinary knowledge, and obtain real-world team-building experience. This week long distributed format allows for sufficient time to evaluate, formulate a question about the dataset, and conduct dataset integration, analysis, and results preparation.

More information can be found at: https://datachallenge.ischool.umd.edu

Our group of four undergraduates won the award for "Best Expression of Results" out of more than 80 teams varied between masters and PhD students.

	1. Countries
		This folder contains CSV files of all the provided countries given by the API after being run through our data scraping program "get_all_country_data.py"

	2. DataScraping
		In order to analyze the data we first had to scrape it from the
		API. Using a series of loops we called the API the necessary amount
		to collect the data on each indicator related to the survey and
		each country that participated 

	3. Graphing
		Once we had all the necessary information cleaned up and ready to
		manipulate, we created several programs that could graph the data
		in certain ways we deemed necessary for analysis.
	
	4. Indicators
		This folder contains CSV files of all the provided indicators given
		by the API after being run through our data scraping program
		"get_all_country_data.py"
