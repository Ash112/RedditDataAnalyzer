
        // vairables from python throught html

        //common date data
var time_frequency = JSON.parse(document.querySelector('#time_frequency').value)

        //polarity chart data
var polarity_frequency = JSON.parse(document.querySelector('#polarity_frequency').value)

        //chart 2
         var options3 = {
          series: [
          {
            name: "Polarity",
            data: polarity_frequency
          },
                ],

          chart: {
          height: 300,
          type: 'line',

              dropShadow: {
                enabled: true,
                color: '#000',
                top: 18,
                left: 10,
                blur: 10,
                opacity: 0.3
                        },
              toolbar: {
                show: true
                        }
                },

        colors: ['#0099cc'],
        dataLabels: {
          enabled: false,
                    },

        stroke: {
          lineCap: 'butt',
          curve: 'straight',
          width: 2,
                },

        title: {
          text: 'Content Polarity',
          align: 'Center'
                },

        grid:   {
          borderColor: '#e7e7e7',
          strokeDashArray: 2,
              row: {
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                opacity: 0
                   },
                     xaxis: {
                        lines: {
                            show: false
                                },
                            },
                            yaxis: {
                        lines: {
                            show: false
                                },
                            },


                },

        markers: {
          size: 2.5,
                },

        xaxis: {
          categories: time_frequency,

          title: {
            text: 'Time(DD.MM.YY-HH)'
          }
        },
        yaxis: {
          title: {
            text: 'Polarity'
          },
        },

        };

        var chart3 = new ApexCharts(document.querySelector("#chartpolarity"), options3);
        chart3.render();
