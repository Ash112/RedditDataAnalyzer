
var allword_frequency = JSON.parse(document.querySelector('#allword_frequency').value)


var options5 = {
      series: [
      {
        data: allword_frequency
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
      text: 'Frequent Words',
      align: 'Center',
}


};

var chart5 = new ApexCharts(document.querySelector("#wordtreemap"), options5);
chart5.render();