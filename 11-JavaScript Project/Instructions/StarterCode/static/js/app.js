// from data.js
var table_data = data;


// YOUR CODE HERE!
var tbody = d3.select("tbody");


function build_table(data){
    tbody.html("");
    data.forEach(dataRow => {
       
        console.table(dataRow);
        let row = tbody.append("tr");
       console.table(Object.values(dataRow));
       
       
       Object.values(dataRow).forEach((val) => {
          
        let cell = row.append("td");
           cell.text(val);
       });
    });
}

function handle_click(){

    d3.event.preventDefault()
    
    let date = d3.select("#datetime").property("value");
    
    let filter_data = table_data;

    if (date){
        filter_data = filter_data.filter((row) => row.datetime === date);
    }
    build_table(filter_data);
}
d3.selectAll("#filter-btn").on("click", handle_click);
build_table(table_data);