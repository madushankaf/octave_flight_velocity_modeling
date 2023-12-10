from flask import Flask, send_file
import base64
import subprocess

app = Flask(__name__)

@app.route('/flight-velocity', methods=['GET'])
def get_flight_velocity():
    subprocess.call(['octave',  'flight_velocity_modeling.m'])
    
    # Return the saved image file
    return send_file('output_plot.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
