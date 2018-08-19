// Finding the top and bottom of the Y-axes
Array.min = function( array ){
    return Math.min.apply( Math, array );
};

Array.max = function( array ){
    return Math.max.apply( Math, array );
};

// Set options for Bar Charts
function getTempOptions( Y_max_temp, Y_min_temp ) {
    var options_temp = {
        scales: {
            yAxes: [{
                display: true,
                ticks: {
                    suggestedMin: Y_min_temp,
                    suggestedMax: Y_max_temp
                }
            }]
        },
        responsive:false,
        maintainAspectRatio: false,
        legend: {
            display: false
        },
    };
    return options_temp;
}

function getHumOptions( Y_max_hum, Y_min_hum ) {
    var options_hum = {
        scales: {
        yAxes: [{
            display: true,
            ticks: {
                suggestedMin: Y_min_hum,
                suggestedMax: Y_max_hum
            }
        }]
        },
        responsive:false,
        maintainAspectRatio: false,
        legend: {
            display: false
        },
    };
    return options_hum;
}

// Drawing the chart using chart.js
function drawBarChart(element_name, chartData, options){
  // get temp bar chart canvas
  var chart = document.getElementById(element_name).getContext("2d");
            

  // draw temp bar chart
  var myTempBarChart = new Chart(chart, {
      type: 'bar',
      data: chartData,
      options : options
  });
}

function changeOverTimeData(data_array){
    changeData = []
    for (i = 1; i < data_array.length; i++){
        // if its a decrease
        if (data_array[i-1] > data_array[i]){
            let decrease = data_array[i-1] - data_array[i];
            var change = decrease/data_array[i-1]*100;
        }
        // if its an increase
        if (data_array[i-1] < data_array[i]){
            let increase = data_array[i] - data_array[i-1];
            var change = increase/data_array[i-1]*100;
        }
        changeData[i-1] = change;
    }
    return changeData;
}

function chartChange(humChartData, tempChartData){
    new Chart(document.getElementById("change_chart"), {
        type: 'line',
        data: {
        datasets: [{ 
            data:  tempChartData,
            label: "Temperature Change",
            borderColor: "#3e95cd",
            fill: false
            }, { 
            data: humChartData,
            label: "Humidity Change",
            borderColor: "#8e5ea2",
            fill: false
            }
        ]
        },
        options: {
        title: {
            display: true,
        }
        }
    });
}