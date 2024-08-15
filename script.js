document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById('resultChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March'],
            datasets: [{
                label: 'Fraud Detection',
                data: [10, 20, 30],
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        }
    });
});

function downloadReport() {
    window.location.href = '/download/report';
}

function submitAnalysis() {
    const method = document.getElementById('method').value;
    fetch('/run_analysis', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ method: method })
    })
    .then(response => response.json())
    .then(data => {
        // Update the chart with new data
        chart.data.datasets[0].data = data.results;
        chart.update();
    })
    .catch(error => console.error('Error:', error));
}
