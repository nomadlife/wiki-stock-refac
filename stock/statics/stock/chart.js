$(function drawChart(ticker) {
      var ticker = ticker
      var data1 = []
      var data2 = []
      var labels = []
      console.log('hello!', ticker);
      
      $.ajax({
            type: "GET",
            url: "{% url 'api-chart-data' ticker=${ticker} %}",
            success: function (data) {
                  console.log("success")
                  labels = data.labels
                  data1 = data.value1
                  data2 = data.value2

                  setChart()
            },
            error: function (error_data) {
                  console.log("error")
                  console.log('url:', url)
                  console.log(error_data)
            }
      });

      function setChart() {
            console.log('hello chart!', labels);
            
            var ctx = document.getElementById("myChart");
            var myChart = new Chart(ctx, {
                  type: 'line',
                  data: {
                        labels: labels,
                        datasets: [{
                              label: '종가',
                              data: data1,
                              fill: false,
                              lineTension: 0,
                              borderColor: 'rgba(255,99,132,1)',
                              borderWidth: 1,
                              // showLine: false,
                              pointRadius: 0,
                              // pointBackgroundColor: [],
                              // pointBorderColor: [],
                        },
                        {
                              label: '예측',
                              data: data2,
                              fill: false,
                              lineTension: 0,
                              borderColor: 'rgba(75, 192, 192, 1)',
                              borderWidth: 1,
                              // showLine: false,
                              pointRadius: 1,
                              // pointBackgroundColor: [],
                              // pointBorderColor: [],
                        }]
                  },
                  options: {
                        animation: false,
                        responsive: false,
                        // maintainAspectRatio: true,
                        legend: {
                              display: true,
                              position: 'top',
                        },
                        hover: {
                              mode: 'label'
                        },
                        title: {
                              display: true,
                              text: ticker
                        },
                  }
            })
      }
})