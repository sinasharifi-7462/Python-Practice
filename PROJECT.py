import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Project: Car Suspension Simulation (Quarter Car Model)
# Physics: Mass-Spring-Damper System
# Method: Euler Integration
# ==========================================

# --- 1. Define Physical Parameters ---
m = 250.0      # Mass (kg) - Quarter of the car's weight
k = 16000.0    # Spring Stiffness (N/m) - How hard the spring is
c = 1000.0     # Damping Coefficient (N.s/m) - Shock absorber strength

# --- 2. Simulation Time Setup ---
dt = 0.01                  # Time step (s) - Smaller is more accurate
total_time = 5.0           # Total duration of simulation (s)
t = np.arange(0, total_time, dt) # Time array from 0 to 5

# --- 3. Define Road Profile ( The Input ) ---
# Create an array of zeros representing a flat road
road_height = np.zeros(len(t))

# Create a "Bump" in the road
# The bump is 10cm high (0.1m) and lasts from t=1s to t=1.5s
for i in range(len(t)):
    if 1.0 <= t[i] <= 1.5:
        road_height[i] = 0.1

# --- 4. Initialize Variables ---
y_car = np.zeros(len(t))   # Car vertical position (Output)
v_car = np.zeros(len(t))   # Car vertical velocity

# Initial conditions (Car starts at rest)
y_car[0] = 0.0
v_car[0] = 0.0

# --- 5. Main Solver Loop (Euler Method) ---
# Loop through each time step to calculate physics
for i in range(len(t) - 1):
    
    # A) Calculate Spring Deflection
    # Displacement = Road Height - Car Height
    displacement = road_height[i] - y_car[i]
    
    # B) Calculate Forces
    # Force from Spring = k * x
    force_spring = k * displacement
    
    # Force from Damper = -c * v (Opposes motion)
    force_damper = -c * v_car[i]
    
    # Total Force on the mass
    total_force = force_spring + force_damper
    
    # C) Newton's Second Law: a = F / m
    acceleration = total_force / m
    
    # D) Update State for the next time step (i+1)
    # New Velocity = Old Velocity + (Acceleration * Time)
    v_car[i+1] = v_car[i] + (acceleration * dt)
    
    # New Position = Old Position + (Velocity * Time)
    y_car[i+1] = y_car[i] + (v_car[i] * dt)

# --- 6. Visualization (Plotting) ---
plt.figure(figsize=(10, 6))

# Plot the Road (Input)
plt.plot(t, road_height, label="Road Profile (Input)", color='black', linestyle='--', linewidth=1.5)

# Plot the Car Response (Output)
plt.plot(t, y_car, label="Car Body Response (Output)", color='red', linewidth=2.5)

# Graph styling
plt.title(f"Suspension Response (m={m}kg, k={k}, c={c})")
plt.xlabel("Time (s)")
plt.ylabel("Vertical Displacement (m)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Show the final result
plt.show()