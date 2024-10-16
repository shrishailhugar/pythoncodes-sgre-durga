html_content='''<!DOCTYPE html>
<html>
<head>
    <title>Test Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        .passed {
            background-color: lightgreen;
        }
        .failed {
            background-color: lightcoral;
        }
        .skipped {
            background-color: lightyellow;
        }
        .chart-container {
            width: 400px;
            height: 400px;
            margin: auto;
            margin-top: 20px;
        }
        .blue {
            color: blue;
        }
        .green{
        color: green;
        }
        .red{
        color: red;
        }
        .yellow{
        color:yellow;
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
<h2>Test Report</h2>
<p>Total Testcases: <span id="total" class="blue"></span></p>
<p>Passed: <span id="passed" class="green"></span></p>
<p>Failed: <span id="failed" class="red"></span></p>
<p>Skipped: <span id="skipped" class="yellow"></span></p>
<table id="reportTable">
    <tr>
        <th>Test Name</th>
        <th>Status</th>
    </tr>
</table>
<div class="chart-container">
    <canvas id="testChart"></canvas>
</div>

<script>
    // Function to generate table rows based on test cases
    function generateRows(testCases) {
        var table = document.getElementById('reportTable');
        var total = testCases.length;
        var passedCount = testCases.filter(tc => tc.status === 'Passed').length;
        var failedCount = testCases.filter(tc => tc.status === 'Failed').length;
        var skippedCount = testCases.filter(tc => tc.status === 'Skipped').length;
        document.getElementById('total').innerText = total;
        document.getElementById('passed').innerText = passedCount;
        document.getElementById('failed').innerText = failedCount;
        document.getElementById('skipped').innerText = skippedCount;
        for (var i = 0; i < testCases.length; i++) {
            var row = table.insertRow();
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerText = testCases[i].name;
            cell2.innerText = testCases[i].status;
            cell2.className = testCases[i].status.toLowerCase();
        }
    }

    // Generate pie chart
    function generateChart(testCases) {
        var passedCount = testCases.filter(tc => tc.status === 'Passed').length;
        var failedCount = testCases.filter(tc => tc.status === 'Failed').length;
        var skippedCount = testCases.filter(tc => tc.status === 'Skipped').length;

        var ctx = document.getElementById('testChart').getContext('2d');
        var testChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Passed', 'Failed', 'Skipped'],
                datasets: [{
                    data: [passedCount, failedCount, skippedCount],
                    backgroundColor: [
                        'lightgreen',
                        'lightcoral',
                        'lightyellow'
                    ]
                }]
            },
            options: {
                title: {
                    display: true,
                    text: 'Test Case Distribution'
                }
            }
        });
    }

    // Fetch test cases from JSON file
    fetch('testCases.json')
        .then(response => response.json())
        .then(testCases => {
            generateRows(testCases);
            generateChart(testCases);
        })
        .catch(error => console.error('Error fetching test cases:', error));
</script>
</body>
</html>
'''
with open('html_report.html','w')as f:
    f.write(html_content)
