<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Realy Time Calculator</title>
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 40px;
            color: red;
        }
        h2 {
            font-size: 30px;
            color: blue;
        }
        form {
            margin-top: 20px;
        }
        input {
            margin: 10px;
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
        }
        video {
            margin-top: 20px;
            width: 600px;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>Realy Time Calculator</h1>
    <video controls>
        <source src="relay.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>

    <h2 id="result"></h2>
    <form id="nrr-form">
        <label for="runs_scored">Total Runs Scored:</label><br>
        <input type="number" id="runs_scored" name="runs_scored" step="1" required><br>
        <label for="balls_faced">Total Balls Faced:</label><br>
        <input type="number" id="balls_faced" name="balls_faced" step="1" required><br>
        <label for="runs_conceded">Total Runs Conceded:</label><br>
        <input type="number" id="runs_conceded" name="runs_conceded" step="1" required><br>
        <label for="balls_bowled">Total Balls Bowled:</label><br>
        <input type="number" id="balls_bowled" name="balls_bowled" step="1" required><br>
        <button type="submit">Calculate</button>
    </form>

    <div id="nrr-result">
        <h2>NRR Calculation Result:</h2>
        <p id="net-run-rate"></p>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script>
        $(document).ready(function () {
            $('#nrr-form').submit(function (event) {
                event.preventDefault();
                var formData = $(this).serialize();
                $.ajax({
                    type: 'POST',
                    url: '/calculate_nrr',
                    data: formData,
                    success: function (response) {
                        $('#net-run-rate').text('Net Run Rate (NRR): ' + response.net_run_rate.toFixed(2));
                    },
                    error: function (error) {
                        console.log(error);
                    }
                });
            });
        });
    </script>
</body>
</html>
