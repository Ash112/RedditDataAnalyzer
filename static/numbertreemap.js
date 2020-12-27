

var allnumber_frequency = JSON.parse(document.querySelector('#allnumber_frequency').value)


var options5 = {
      series: [
      {
        data: allnumber_frequency
      }
    ],
      legend: {
      show: false
    },
    chart: {
      height: 250,
      type: 'treemap'

    },
    title: {
      text: 'Frequent Numbers',
      align: 'Center',
}


};

var chart5 = new ApexCharts(document.querySelector("#numbertreemap"), options5);
chart5.render();