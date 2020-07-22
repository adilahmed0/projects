var apiKey = weather_key
var qurl = ''

const fetchWeather = () => {
    axios.get(qurl)
        .then(function (response){
            //const cityWeather = response;
            console.log(response.data.main.temp);
            document.getElementById("Anchor_Weather").innerHTML = `Current Temperature ${response.data.main.temp}`
        })
        .catch(error => console.log(error));
};

function Weather() {
    // recover the option that has been chosen
    var selectedOption = d3.select(this).node().value

    qurl = 'http://api.openweathermap.org/data/2.5/weather?q=' + selectedOption + ',US&units=imperial&appid=' + apiKey;
    
    fetchWeather();
    
};





