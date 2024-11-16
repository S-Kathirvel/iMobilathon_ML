import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(69)

# Define the number of samples
n_samples = 2000

# Define car types and their respective limits for car height, spoiler size, speed, and wing angle
car_types = {
    'Compact': {'car_height': (140, 160), 'spoiler_size': (3, 10), 'speed': (120, 180), 'wing_angle': (0, 10)},
    'Hatchbacks': {'car_height': (140, 155), 'spoiler_size': (3, 10), 'speed': (120, 170), 'wing_angle': (0, 12)},
    'Sedans': {'car_height': (140, 160), 'spoiler_size': (5, 15), 'speed': (140, 200), 'wing_angle': (0, 15)},
    'Luxury_Sedans': {'car_height': (140, 160), 'spoiler_size': (5, 12), 'speed': (150, 250), 'wing_angle': (0, 10)},
    'SUVs': {'car_height': (160, 185), 'spoiler_size': (5, 20), 'speed': (140, 210), 'wing_angle': (0, 20)},
    'Crossovers': {'car_height': (155, 175), 'spoiler_size': (5, 15), 'speed': (130, 190), 'wing_angle': (0, 15)},
    'Sports_Cars': {'car_height': (120, 140), 'spoiler_size': (10, 25), 'speed': (200, 350), 'wing_angle': (5, 30)},
    'Muscle_Cars': {'car_height': (130, 145), 'spoiler_size': (15, 25), 'speed': (180, 300), 'wing_angle': (10, 25)},
    'Supercars': {'car_height': (110, 130), 'spoiler_size': (20, 30), 'speed': (250, 400), 'wing_angle': (15, 30)},
    'Pickup_Trucks': {'car_height': (170, 200), 'spoiler_size': (5, 20), 'speed': (120, 180), 'wing_angle': (0, 15)},
    'Utility': {'car_height': (140, 160), 'spoiler_size': (5, 15), 'speed': (120, 180), 'wing_angle': (0, 12)},
    'Kei_Cars': {'car_height': (130, 150), 'spoiler_size': (1, 5), 'speed': (100, 140), 'wing_angle': (0, 8)}
}

# Generate synthetic data
car_type_choices = np.random.choice(list(car_types.keys()), size=n_samples)
data = {'car_type': car_type_choices}

# Populate data based on car type limits
car_heights = []
spoiler_sizes = []
speeds = []
wing_angles = []

for car_type in data['car_type']:
    height_min, height_max = car_types[car_type]['car_height']
    spoiler_min, spoiler_max = car_types[car_type]['spoiler_size']
    speed_min, speed_max = car_types[car_type]['speed']
    wing_angle_min, wing_angle_max = car_types[car_type]['wing_angle']
    
    car_heights.append(np.random.uniform(height_min, height_max+1))
    spoiler_sizes.append(np.random.uniform(spoiler_min, spoiler_max))
    speeds.append(np.random.uniform(speed_min, speed_max))
    wing_angles.append(np.random.uniform(wing_angle_min, wing_angle_max))

# Create remaining attributes
data['car_height'] = np.array(car_heights).astype(int) 
data['spoiler_size'] = np.array(spoiler_sizes).astype(int)
data['speed'] = np.array(speeds).astype(int)  # Speed in km/h
data['wing_angle'] = np.array(wing_angles).round(2)  # Wing angle in degrees

# Generate synthetic downforce values (in Newtons)
data['downforce'] = (
    0.5 * data['speed']**1.5 * np.sin(np.radians(data['wing_angle'])) / (data['car_height']) + 
    10 * data['spoiler_size']
).round(2)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('Data/downforce_data.csv', index=False)
print("CSV file 'downforce_data' created successfully.")
