function velocity_matrix = flight_velocity_modeling(acceleration, initial_velocity, time_to_takeoff)
    acceleration = evalin('base', 'acceleration');
    initial_velocity = evalin('base', 'initial_velocity');
    time_to_takeoff = evalin('base', 'time_to_takeoff');
    % Time vector
    t = 0:0.1:time_to_takeoff;

    % Calculate velocity
    velocity = initial_velocity + acceleration * t + 0.5 * acceleration * t.^2;

    % Store time and velocity values in a matrix
    velocity_matrix = [t' velocity'];
end
