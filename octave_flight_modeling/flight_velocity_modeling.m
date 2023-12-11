% Flight Velocity Modeling Example

% Parameters
acceleration = 2;
initial_velocity = 0;
time_to_takeoff = 10;

% Time vector
t = 0:0.1:time_to_takeoff;

velocity = initial_velocity + acceleration * t + 0.5 * acceleration * t.^2;

% Plotting the results
plot(t, velocity, 'LineWidth', 2);
title('Flight Velocity During Takeoff');
xlabel('Time (seconds)');
ylabel('Velocity (m/s)');
#grid on;

% Save the plot as an image file (e.g., PNG)
saveas(gcf, 'output_plot.png');
