// Get location form
var locationForm = document.getElementById('location-form');
// Listen for submit
locationForm.addEventListener('submit', geocode);

var infoWindow;

function geocode(e){
  e.preventDefault();

  var location = document.getElementById('location-input').value;
  
  axios.get('https://maps.googleapis.com/maps/api/geocode/json',{
    params:{
      address:location,
      key:'AIzaSyBSs1yDD-gBeLwJhZptud-Iga12Ytw27Uk'
    }
  })
  .then(function (response) {
    loc = []
    var latit= response.data.results[0].geometry.location.lat;
    var longit = response.data.results[0].geometry.location.lng;
    loc.push(latit, longit)
    return loc;
  })
  .then(loc => loc = loc)
  .then(() => {
    var latit = loc[0]
    var longit = loc[1]

    // Map options
    var options = {
      zoom:13,
      center:{lat: latit,lng: longit}
    }
    // New map
    var map = new google.maps.Map(document.getElementById('map'), options);

    // Marker on user location
    var marker = new google.maps.Marker({
      position:{lat: latit,lng: longit},
      map:map
  });
    const contentString = '<h4> Your Location: </h4>' + location;
    
    const infoWindow = new google.maps.InfoWindow({
      content: contentString
    });

    marker.addListener('click', () =>{
      infoWindow.open(map, marker);
    });

    const form = $(e.target).serializeArray(); // here we're using jQuery to serialize the form
      fetch('/api', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    })
      .then((fromServer) => fromServer.json())
      .then((fromServer) => {

        for (let prop in fromServer) {

          if (document.getElementById('select-all').checked) {
                const latit = Number(fromServer[prop].latitude)
                const longit = Number(fromServer[prop].longitude)
                const dates = fromServer[prop].date
                const street = fromServer[prop].street_number 
                const addy = fromServer[prop].street_address
                const crime = fromServer[prop].clearance_code_inc_type
                const service = new google.maps.DistanceMatrixService();
                var origin = [location];
                var destination = {lat: latit, lng: longit};
                service.getDistanceMatrix(
                  {
                    origins: [String(origin)], 
                    destinations: [destination],
                    travelMode: 'DRIVING',
                    unitSystem: google.maps.UnitSystem.IMPERIAL
                  },
                  (response, status) => {
                    if (status == 'OK') {
                      var origins = response.originAddresses;
                      var destinations = response.destinationAddresses;
                  
                      for (var i = 0; i < origins.length; i++) {
                        var results = response.rows[i].elements;
                        for (var j = 0; j < results.length; j++) {
                          const distArr = []
                          var element = results[j];
                          distance = element.distance.text;
                          }
                      }
                    }
                    const contentString =
                      '<h4>' + street + " " + addy + '</h4>' +
                      "<p><b>Crime: </b>" + crime + "</br>" + 
                      "<b>Date: </b>" + dates + "</br>" +
                      "<p id=distance><b>Distance from your location: </b></p>" + distance
                      "</p>" ;
                    const marker  = new google.maps.Marker({
                      position:{lat: latit, lng: longit},
                      map:map,
                      icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
              
                    const infoWindow = new google.maps.InfoWindow({
                      content: contentString
                    });
          
                    marker.addListener('click', () =>{
                      infoWindow.open(map, marker);
                    });

                    map.addListener('click', function() {
                      if (infoWindow) infoWindow.close();
                    });
                  })
            };
              
          if (document.getElementById('homocide').checked) {
            if (fromServer[prop].clearance_code_inc_type == "HOMOCIDE") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
  
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
  
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

                })
              }
            };

          if (document.getElementById('sex').checked) {
            if (fromServer[prop].clearance_code_inc_type == "SEX OFFENSE") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

                })
              }
            };

          if (document.getElementById('vandalism').checked) {
            if (fromServer[prop].clearance_code_inc_type == "VANDALISM") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

                })
              }
            };
          
          if (document.getElementById('assault').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ASSAULT") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

                })
              }
            };
          
          if (document.getElementById('assaultW').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ASSAULT, WEAPON") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('assaultS').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ASSAULT, SHOOTING") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

  
                })
              }
            };
    
          if (document.getElementById('accident').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ACCIDENT") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

        
                })
              }
            };
    
          if (document.getElementById('accidentI').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ACCIDENT WITH IMPOUND") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

                })
              }
            };
    
          if (document.getElementById('autoT').checked) {
            if (fromServer[prop].clearance_code_inc_type == "THEFT FROM AUTO") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });

                })
              }
            };
    
          if (document.getElementById('autoS').checked) {
            if (fromServer[prop].clearance_code_inc_type == "AUTO, STOLEN") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('autoSR').checked) {
            if (fromServer[prop].clearance_code_inc_type == "AUTO, STOLEN & RECOVERED") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('theft').checked) {
            if (fromServer[prop].clearance_code_inc_type == "THEFT") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('robberyC').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ROBBERY, COMMERCIAL") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('robberyO').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ROBBERY, OTHER") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('robberyV').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ROBBERY, VEHICLE") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('robberyR').checked) {
            if (fromServer[prop].clearance_code_inc_type == "ROBBERY, RESIDENTIAL") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('BnER').checked) {
            if (fromServer[prop].clearance_code_inc_type == "B & E, RESIDENTIAL") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('BnEC').checked) {
            if (fromServer[prop].clearance_code_inc_type == "B & E, COMMERCIAL") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('BnEV').checked) {
            if (fromServer[prop].clearance_code_inc_type == "B & E, VACANT") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('BnERV').checked) {
            if (fromServer[prop].clearance_code_inc_type == "B & E, RESIDENTIAL (VACANT)") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('BnES').checked) {
            if (fromServer[prop].clearance_code_inc_type == "B & E, SCHOOL") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };
    
          if (document.getElementById('BnEO').checked) {
            if (fromServer[prop].clearance_code_inc_type == "B & E, OTHER") {
              const latit = Number(fromServer[prop].latitude)
              const longit = Number(fromServer[prop].longitude)
              const dates = fromServer[prop].date
              const street = fromServer[prop].street_number 
              const addy = fromServer[prop].street_address
              const crime = fromServer[prop].clearance_code_inc_type
              const service = new google.maps.DistanceMatrixService();
              var origin = [location];
              var destination = {lat: latit, lng: longit};
              service.getDistanceMatrix(
                {
                  origins: [String(origin)], 
                  destinations: [destination],
                  travelMode: 'DRIVING',
                  unitSystem: google.maps.UnitSystem.IMPERIAL
                },
                (response, status) => {
                  if (status == 'OK') {
                    var origins = response.originAddresses;
                    var destinations = response.destinationAddresses;
                
                    for (var i = 0; i < origins.length; i++) {
                      var results = response.rows[i].elements;
                      for (var j = 0; j < results.length; j++) {
                        const distArr = []
                        var element = results[j];
                        distance = element.distance.text;
                      }
                    }
                  }
    
                  const contentString =
                    '<h4>' + street + " " + addy + '</h4>' +
                    "<p><b>Crime: </b>" + crime + "</br>" + 
                    "<b>Date: </b>" + dates + "</br>" +
                    "<p id=distance><b>Distance from your location: </b></p>" + distance +
                    "</p>" ;
    
                  const marker  = new google.maps.Marker({
                    position:{lat: latit, lng: longit},
                    map:map,
                    icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
                  });
            
                  const infoWindow = new google.maps.InfoWindow({
                    content: contentString
                  });
        
                  marker.addListener('click', () =>{
                    infoWindow.open(map, marker);
                  });

                  map.addListener('click', function() {
                    if (infoWindow) infoWindow.close();
                  });
                })
              }
            };

          };

        })
      });
    };