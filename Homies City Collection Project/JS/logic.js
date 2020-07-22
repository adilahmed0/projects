// var apiKey = API_KEY;

var url = "./Resources/city_join.json"
// var proxy_url = "https://cors-anywhere.herokuapp.com/";
// var heroku_url = "https://duong-homies.herokuapp.com/";
// var url = proxy_url + heroku_url

// Fetch the JSON data and console log it
d3.json(url).then((jsonData) => {
  console.log(jsonData)

  var city = jsonData.map(row => row.city)
  var city_sorted = city.sort();
  console.log(city_sorted)

  d3.select("#selDataset")
    .selectAll("option")
    .data(city)
    .enter().append("option")
    .classed("cities", true)
    .text(function(i){return i;})
    .exit().remove()

})

