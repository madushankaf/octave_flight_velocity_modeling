from flask import Flask, send_file
import base64
import subprocess
import base64

app = Flask(__name__)

@app.route('/flight-velocity', methods=['GET'])

def get_flight_velocity():
    subprocess.call(['octave',  'flight_velocity_modeling.m'])
    
    # Convert the image to base64
    with open('output_plot.png', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Return the base64 encoded image as a string
    return encoded_string

if __name__ == '__main__':
    app.run(debug=True)
