
        var word_frequency = JSON.parse(document.querySelector('#word_frequency').value)

        //document.write(word_frequency)

        var time_frequency = JSON.parse(document.querySelector('#time_frequency').value)

        //document.write(time_frequency)

        var options = {
          series: [{
            name: "Frequency",
            data: word_frequency

        }],
          chart: {
          height: 300,
          type: 'line',

          zoom: {
            enabled: true
          }
        },

        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight',
          width: 3
        },
        title: {
          text: 'Word mention Frequency',
          align: 'center'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0
          },
        },
        xaxis: {
          categories: time_frequency,
        }
        };

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();
