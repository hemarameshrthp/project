FusionCharts.ready(function () {
    var stockPriceChart = new FusionCharts({
        id: "stockRealTimeChart",
        type: 'realtimeline',
        renderAt: 'chart-container',
        width: '500',
        height: '600',
        dataFormat: 'json',
        dataSource: {
            "chart": {
                "caption": "Macine Run-Time Monitor",
                "xAxisName": "Time",
                "yAxisName": "Deviation",
                "numberSuffix": "mins",
                "refreshinterval": "5",
                "yaxisminvalue": "1",
                "yaxismaxvalue": "10",
                "numdisplaysets": "10",
                "labeldisplay": "rotate",
                "showValues": "0",
                "showRealTimeValue": "0",
                "theme": "fint"
            },
            "categories": [{
                "category": [{
                    "label": "Start"
                }]
            }],
            "dataset": [{
                "data": [{
                    "value": "3"
                }]
            }]
        },
       "events": {
           "initialized": function (evt,args) {
               function addLeadingZero(num){
                   return (num <= 9)? ("0"+num) : num;
               }
                function formatDate()
                {
                    var today=new Date();
                    var dd = today.getDate();
                    var mm = today.getMonth()+1; //January is 0!
                    var yyyy = today.getFullYear();

                   if(dd<10) {
                          dd = '0'+dd
                     }

                    if(mm<10) {
                          mm = '0'+mm
                     }

                    return today = dd + '/' + mm + '/' + yyyy;
                }
                var hema,hema1,hema2;
               var dBRef2= firebase.database().ref('rundiff');
                 dBRef2.on('value',function(snap){ hema=snap.val()});

                 var dBRef4= firebase.database().ref('runstart');
                 dBRef4.on('value',function(snap){ hema1=snap.val()});

                 var dBRef6= firebase.database().ref('runstop');
                 dBRef6.on('value',function(snap){ hema2=snap.val()});

               function updateData() {

                    var chartRef = FusionCharts("stockRealTimeChart"),

                        currDate = new Date(),
                        label = formatDate()+"\n"+hema1+" - "+hema2+"\n"+ addLeadingZero(currDate.getHours()) + ":" +addLeadingZero(currDate.getMinutes()),

                        strData = "&label=" + label
                                    + "&value="
                                    + hema;
                    // Feed it to chart.
                    chartRef.feedData(strData);
                }

               var myVar = setInterval(function () {
                   updateData();
               }, 5000);
           }
       }
    })
    .render();
});