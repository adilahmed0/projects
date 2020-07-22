// Link to Json file
var url = "./Resources/city_join.json"
// var proxy_url = "https://cors-anywhere.herokuapp.com/";
// var heroku_url = "https://duong-homies.herokuapp.com/";
// var url = proxy_url + heroku_url

// Creating map object
var myMap = L.map("map-id", {
    center: [39.833333, -98.583333],
    zoom: 4
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
}).addTo(myMap);

// Grabbing Json data
d3.json(url).then((jsonData) => {
// d3.json(url, function(jsonData) {
//     console.log(jsonData)
    var city = jsonData.map(row => row.city)
    var lat = jsonData.map(row => row.lat)
    var long = jsonData.map(row => row.long)
    var state = jsonData.map(row => row.state)
    var crime = jsonData.map(row => row.crime_index)
    var living = jsonData.map(row => row.cost_of_living_index)

    // Adding pop-up marker for each city
    for (var d=0; d<city.length; d++) {
        var newMarker = L.marker([lat[d], long[d]], {
            fillOpacity: 0.75,
            color: "blue"
        })
    
    // Popup message
    newMarker.bindPopup(city[d] + ", " + state[d] + "<hr>" + "Crime Index: " + crime[d] + "<br>" + "Cost of Living: " + living[d])
    // When hovering mouse icon over the marker, display popup message
    newMarker.on('mouseover', function (e) {
        this.openPopup()
    })
    // When no longer hovering over the icon, close the popup
    newMarker.on('mouseout', function (e) {
        this.closePopup()
    })
    
    // Add click to zoom and center functionality
    newMarker.on('click', function (clickZoom){
        myMap.setView(clickZoom.target.getLatLng(),12);
    })

    // Add to map
    newMarker.addTo(myMap)
    }


});

d3.selectAll("#selDataset").on("change", optionChanged)

function optionChanged() {
    d3.json(url).then((jsonData) => {
        var dropdownMenu = d3.select("#selDataset")
        var dataset = dropdownMenu.property("value")

        var city = jsonData.map(row => row.city)
        var lat = jsonData.map(row => row.lat)
        var long = jsonData.map(row => row.long)

        for(var i = 0; i < city.length; i++) {
            if(dataset == city[i]) {
                myMap.setView(new L.LatLng(lat[i], long[i]), 12)
            }
        }
    })
}