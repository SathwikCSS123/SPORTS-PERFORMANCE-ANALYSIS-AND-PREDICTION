from pywebio import start_server
from pywebio.input import input_group, input, NUMBER
from pywebio.output import put_html

# Function to calculate NRR
def calculate_nrr(runs_scored, balls_faced, runs_conceded, balls_bowled):
    runs_per_ball_scored = runs_scored / balls_faced
    runs_per_ball_conceded = runs_conceded / balls_bowled
    nrr = (runs_per_ball_scored - runs_per_ball_conceded) * 6
    return nrr

# Main function to collect inputs and display results
def cricket_nrr_calculator():
    while True:
        put_html("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Cricket Net Run Rate Calculator</title>
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
                <h1>Cricket Net Run Rate Calculator</h1>
                <video controls>
                    <source src="cricket.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <h2 id="result"></h2>
                
                <div id="nrr-result">
                    <h2>NRR Calculation Result:</h2>
                    <p id="net-run-rate"></p>
                </div>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
                <script>
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
                </script>
            </body>
            </html>
        """)
        
        # Collect user input
        form_data = input_group("Cricket Net Run Rate Calculator", [
            input("Enter the rank (1-10):", type=NUMBER, name='rank'),
            input("Enter the number of matches played:", type=NUMBER, name='matches_played'),
            input("Enter the number of wins:", type=NUMBER, name='wins'),
            input("Total Runs Scored:", type=NUMBER, name='runs_scored'),
            input("Total Balls Faced:", type=NUMBER, name='balls_faced'),
            input("Total Runs Conceded:", type=NUMBER, name='runs_conceded'),
            input("Total Balls Bowled:", type=NUMBER, name='balls_bowled')
        ])
        
        # Calculate NRR
        nrr = calculate_nrr(form_data['runs_scored'], form_data['balls_faced'], form_data['runs_conceded'], form_data['balls_bowled'])
        
        # Display the result
        put_html("""
            <script>
                document.getElementById('net-run-rate').innerHTML = 'Net Run Rate (NRR): ' + %s.toFixed(2);
            </script>
        """ % nrr)

if __name__ == '__main__':
    start_server(cricket_nrr_calculator, port=8080, debug=True)