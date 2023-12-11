from flask import Flask, send_file
import base64
import subprocess
import base64
import time
import os
from oct2py import octave
from flask import send_file

app = Flask(__name__)

@app.route('/flight-velocity', methods=['GET'])


def get_flight_velocity():
    octave.eval('flight_velocity_modeling')
    
    # Check if the output_plot.png file exists
    if os.path.exists('output_plot.png'):
        # Return the image file
        return send_file('output_plot.png', mimetype='image/png')
    else:
        return 'Error: File not found'
    

if __name__ == '__main__':
    app.run()
