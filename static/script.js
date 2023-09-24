
function updateChart() {
    $.ajax({
        type: "GET",
        url: "/get-data"
    })
    .done(function(response){
        $('#myCharts').empty()
        $('#myCharts').append(response.data)
        //$('#myCharts').replaceWith(response.data)
    })
}


setInterval(updateChart, 2000);
