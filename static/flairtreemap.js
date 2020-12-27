
var allflair_frequency = JSON.parse(document.querySelector('#allflair_frequency').value)



var options5 = {
      series: [
      {
        data: allflair_frequency
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
      text: 'Frequent post Flairs',
      align: 'Center',
}


};

var chart5 = new ApexCharts(document.querySelector("#flairtreemap"), options5);
chart5.render();