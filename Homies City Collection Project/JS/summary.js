// Link to Json file
var sumurl = "./Resources/city_join.json"
// var proxy_url = "https://cors-anywhere.herokuapp.com/";
// var heroku_url = "https://duong-homies.herokuapp.com/";
// var url = proxy_url + heroku_url





var summary = []



d3.select("#selDataset").on("change", function(summaryd) {
    Weather()
    
    selectedOption = d3.select(this).node().value

    d3.json(sumurl).then((jsonData) => {
        console.log(jsonData);
        var cityData = jsonData;
        
    
        summary = cityData.filter(d => d.city == selectedOption);
        console.log("summary", summary);
        var affordability = summary.map(row => row.affordability_index)
        var costOfLiving = summary.map(row => row.cost_of_living_index)
        var crimeIndex = summary.map(row => row.crime_index)
        var healthCareIndex = summary.map(row => row.health_care_index)
        var pollutionIndex = summary.map(row => row.pollution_index)
        var priceToIncome = summary.map(row => row.price_to_income_ratio)
        var purchasingPower = summary.map(row => row.purchasing_power_index)
        var qolIndex = summary.map(row => row.quality_of_life_index)
        var safetyIndex = summary.map(row => row.safety_index)
        var trafficIndex = summary.map(row => row.traffic_commute_time_index)
        var cityName = summary.map(row => row.city)
        console.log(cityName)
        document.getElementById("Anchor").innerHTML = `City: ${cityName}`
        document.getElementById("Anchor_Affordability").innerHTML = `Affordability Index: ${affordability}`
        document.getElementById("Anchor_COL").innerHTML = `Cost of Living Index: ${costOfLiving}`
        document.getElementById("Anchor_Crime").innerHTML = `Crime Index: ${crimeIndex}`
        document.getElementById("Anchor_Healthcare").innerHTML = `Health Care Index: ${healthCareIndex}`
        document.getElementById("Anchor_Pollution").innerHTML = `Pollution Index: ${pollutionIndex}`
        document.getElementById("Anchor_PTI").innerHTML = `Price to Income Ratio: ${priceToIncome}`
        document.getElementById("Anchor_Purchasing").innerHTML = `Purchasing Power Index: ${purchasingPower}`
        document.getElementById("Anchor_QOL").innerHTML = `Quality Of Life Index: ${qolIndex}`
        document.getElementById("Anchor_Safety").innerHTML = `Safety Index: ${safetyIndex}`
        document.getElementById("Anchor_Traffic").innerHTML = `Traffic Index: ${trafficIndex}`
        
    });
    
    
});
