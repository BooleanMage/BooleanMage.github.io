// HistogramData.js

function generateHistogramData(answers) {
    // Count the number of times each option was selected
    var counts = {};
    for(var i=0; i<answers.length; i++) {
        if(answers[i] in counts) {
            counts[answers[i]]++;
        } else {
            counts[answers[i]] = 1;
        }
    }

    // Create the data for the histogram
    var histogramData = {
        labels: Object.keys(counts),
        datasets: [{
            data: Object.values(counts),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    return histogramData;
}

function drawHistogram(elementId, histogramData) {
    // Draw the histogram
    var ctx = document.getElementById(elementId).getContext('2d');
    var histogram = new Chart(ctx, {
        type: 'bar',
        data: histogramData,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
