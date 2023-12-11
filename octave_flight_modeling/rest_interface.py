from flask import Flask, jsonify
import base64
import subprocess
import base64
import time
import os
from oct2py import octave
from flask import request

app = Flask(__name__)


@app.route('/flight-velocity', methods=['GET'])
def get_flight_velocity():
    # Get acceleration, initial_velocity, and time_to_takeoff from query parameters
    acceleration = float(request.args.get('acceleration'))
    initial_velocity = float(request.args.get('initial_velocity'))
    time_to_takeoff = float(request.args.get('time_to_takeoff'))

    octave.eval(f'acceleration = {acceleration};')
    octave.eval(f'initial_velocity = {initial_velocity};')
    octave.eval(f'time_to_takeoff = {time_to_takeoff};')

    # Load the Octave script
    octave.eval('source("flight_velocity_modeling.m")')

    # Call the MATLAB function and store the result in a variable
    octave.eval('result = flight_velocity_modeling(acceleration, initial_velocity, time_to_takeoff);')

    # Retrieve the result from the Octave workspace
    velocity_matrix = octave.pull('result');
    velocity_matrix_list = velocity_matrix.tolist()

    # Print the results
    print("Time and Velocity Matrix:")
    print(velocity_matrix)
    return jsonify({'time_and_velocity_matrix': velocity_matrix_list})

    
    

if __name__ == '__main__':
    app.run()
