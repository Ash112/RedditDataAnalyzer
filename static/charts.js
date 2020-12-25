
        // vairables from python throught html

        //common date data
var time_frequency = JSON.parse(document.querySelector('#time_frequency').value)

        //frequencychartoptions
var word_frequency = JSON.parse(document.querySelector('#word_frequency').value)

        //sentimentchartoptions
var sentiment_frequency = JSON.parse(document.querySelector('#sentiment_frequency').value)

        //document.write(time_frequency)
        //document.write(word_frequency)
        //document.write(word_frequency)

         // chart for frequency
 var options = {
          series: [
          {
            name: "Frequency",
            data: sentiment_frequency
          },

        ],
          chart: {
          height: 350,
          type: 'line',

          dropShadow: {
            enabled: true,
            color: '#000',
            top: 18,
            left: 7,
            blur: 10,
            opacity: 0.2
          },
          toolbar: {
            show: false
          }
        },
        colors: ['#77B6EA', '#545454'],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Word Frequency',
          align: 'Center'
        },
        grid: {
          borderColor: '#e7e7e7',
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0
          },
        },
        markers: {
          size: 2
        },
        xaxis: {
          categories: time_frequency,
          title: {
            text: 'Time Frame'
          }
        },
        yaxis: {
          title: {
            text: 'Frequency'
          },
        },

        };

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();