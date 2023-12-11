from flask import Flask, send_file
import base64
import subprocess
import base64
import time
import os
from oct2py import octave

app = Flask(__name__)

@app.route('/flight-velocity', methods=['GET'])

def get_flight_velocity():
    octave.eval('flight_velocity_modeling')
    
    # Check if the output_plot.png file exists
    
    if os.path.exists('output_plot.png'):
        # Convert the image to base64
        with open('output_plot.png', 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        # Return the base64 encoded image as a string
        return encoded_string
    else:
        return 'Error: File not found'
    

if __name__ == '__main__':
    app.run()
