
## PG County Crime Tracker

[Heroku Link](https://warm-brushlands-70019.herokuapp.com/)

  

This project gives users an interactive Google Map that allows them to input their location and see various crimes around their location.

  

### Target browsers

* Chrome

  

### User manual

* Input your current location in the search bar to pinpoint yourself on the map. Check the checkboxes with the crimes you want included on the map. Click Submit

* Click on flags to display info on the specific crime
* To add more crimes to the map check them off and click submit again.

* Use the Crimes page to display a list of crimes based on crime type.

  

## Developer Manual

### Installation

clone the repository here and run:

  

npm install

npm start

  

Once the server is running you will be able to visit http://localhost:3000/ and see the application running

### The API for our server application - all GET, POST, PUT, etc endpoints, and what they each do

    Data of crimes gathered from Prince George's County's API
    [https://data.princegeorgescountymd.gov/resource/wb4e-w4nf.json]

    Relating user input to an actual address and coordinates used Google Maps Geocode API
	[https://maps.googleapis.com/maps/api/geocode/json]
	

    Generating a map, markers, infoWindows, and various services like distance from crime used the Google Maps Map API and its following services
	[https://maps.googleapis.com/maps/api/js?key=MYKEY&callback=geocode]
	*Services
		google.maps.Map: Creates a Google Maps
		google.maps.Marker: Creates markers
		google.maps.InfoWinfow: Assigns InfoWindows to markers
		google.maps.DistanceMatrixService: Calculates the distance from user location to crime entry

	Google Maps API documentation:
		https://developers.google.com/maps/documentation/javascript/overview
	

### Bugs and future development

* Searching for a new address without refreshing can lead some of the information to be incorrect

