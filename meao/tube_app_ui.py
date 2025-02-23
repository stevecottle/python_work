import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from geopy.distance import geodesic
import requests
import time

# Load station data
def load_stations(filename):
    return pd.read_csv(filename)

# Find the nearest station
def find_nearest_station(user_coords, stations):
    nearest_station = None
    min_distance = float('inf')
    
    for _, station in stations.iterrows():
        station_coords = (station['Latitude'], station['Longitude'])
        distance = geodesic(user_coords, station_coords).km
        if distance < min_distance:
            min_distance = distance
            nearest_station = station['Station']
    
    return nearest_station

# Get travel time between stations
def get_travel_time(start_station_id, end_station_id, api_key, retries=3):
    if start_station_id == end_station_id:
        return None
    
    url = f"https://api.tfl.gov.uk/Journey/JourneyResults/{start_station_id}/to/{end_station_id}"
    params = {"app_key": api_key, "mode": "tube"}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'journeys' not in data or not data['journeys']:
            return None
            
        return data['journeys'][0]['duration']
    except requests.exceptions.HTTPError as e:
        if response.status_code == 500 and retries > 0:
            time.sleep(1)
            return get_travel_time(start_station_id, end_station_id, api_key, retries - 1)
        else:
            return None
    except Exception as e:
        return None

# Find the equal-time destination
def find_equal_time_station(users, stations, api_key):
    user_stations = [find_nearest_station(user, stations) for user in users]
    
    travel_times = {}
    for _, destination in stations.iterrows():
        dest_id = destination['StationID']
        times = []
        valid = True
        
        for start_station in user_stations:
            start_id = stations[stations['Station'] == start_station]['StationID'].values[0]
            time = get_travel_time(start_id, dest_id, api_key)
            if not time:
                valid = False
                break
            times.append(time)
        
        if valid:
            travel_times[destination['Station']] = times
    
    best_station = None
    min_variance = float('inf')
    
    for station, times in travel_times.items():
        mean = sum(times) / len(times)
        variance = sum((t - mean) ** 2 for t in times) / len(times)
        if variance < min_variance:
            min_variance = variance
            best_station = station
    
    return best_station

# UI Code
def toggle_input_mode():
    if toggle_button.cget("text") == "Use Dropdown":
        # Show dropdowns and hide manual input fields
        label_user1_station.grid()
        combo_user1_station.grid()
        label_user2_station.grid()
        combo_user2_station.grid()
        
        label_user1_lat.grid_remove()
        entry_user1_lat.grid_remove()
        label_user1_lon.grid_remove()
        entry_user1_lon.grid_remove()
        label_user2_lat.grid_remove()
        entry_user2_lat.grid_remove()
        label_user2_lon.grid_remove()
        entry_user2_lon.grid_remove()
        
        toggle_button.config(text="Use Manual Input")
    else:
        # Show manual input fields and hide dropdowns
        label_user1_lat.grid()
        entry_user1_lat.grid()
        label_user1_lon.grid()
        entry_user1_lon.grid()
        label_user2_lat.grid()
        entry_user2_lat.grid()
        label_user2_lon.grid()
        entry_user2_lon.grid()
        
        label_user1_station.grid_remove()
        combo_user1_station.grid_remove()
        label_user2_station.grid_remove()
        combo_user2_station.grid_remove()
        
        toggle_button.config(text="Use Dropdown")

def on_submit():
    try:
        if toggle_button.cget("text") == "Use Dropdown":
            # Get selected stations from the dropdowns
            user1_station = combo_user1_station.get()
            user2_station = combo_user2_station.get()
            
            # Get the coordinates of the selected stations
            user1_coords = (
                stations[stations['Station'] == user1_station]['Latitude'].values[0],
                stations[stations['Station'] == user1_station]['Longitude'].values[0]
            )
            user2_coords = (
                stations[stations['Station'] == user2_station]['Latitude'].values[0],
                stations[stations['Station'] == user2_station]['Longitude'].values[0]
            )
        else:
            # Get coordinates from the manual input fields
            user1_lat = float(entry_user1_lat.get())
            user1_lon = float(entry_user1_lon.get())
            user2_lat = float(entry_user2_lat.get())
            user2_lon = float(entry_user2_lon.get())
            
            user1_coords = (user1_lat, user1_lon)
            user2_coords = (user2_lat, user2_lon)
        
        users = [user1_coords, user2_coords]
        
        # Find the equal-time destination
        result = find_equal_time_station(users, stations, api_key)
        
        # Show the result in a message box
        if result:
            messagebox.showinfo("Result", f"Equal-time destination: {result}")
        else:
            messagebox.showinfo("Result", "Unable to find an equal-time destination.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the main window
root = tk.Tk()
root.title("Tube App")

# Load station data and API key
stations = load_stations("tube_stations.csv")
api_key = "f234cac01ae545d2991cc51681a2f820"  # Replace with your key

# Create input fields for manual coordinates
label_user1_lat = tk.Label(root, text="User 1 Latitude:")
label_user1_lat.grid(row=0, column=0)
entry_user1_lat = tk.Entry(root)
entry_user1_lat.grid(row=0, column=1)

label_user1_lon = tk.Label(root, text="User 1 Longitude:")
label_user1_lon.grid(row=1, column=0)
entry_user1_lon = tk.Entry(root)
entry_user1_lon.grid(row=1, column=1)

label_user2_lat = tk.Label(root, text="User 2 Latitude:")
label_user2_lat.grid(row=2, column=0)
entry_user2_lat = tk.Entry(root)
entry_user2_lat.grid(row=2, column=1)

label_user2_lon = tk.Label(root, text="User 2 Longitude:")
label_user2_lon.grid(row=3, column=0)
entry_user2_lon = tk.Entry(root)
entry_user2_lon.grid(row=3, column=1)

# Create dropdown menus for station selection
label_user1_station = tk.Label(root, text="User 1 Station:")
label_user1_station.grid(row=0, column=0)
combo_user1_station = ttk.Combobox(root, values=stations['Station'].tolist())
combo_user1_station.grid(row=0, column=1)

label_user2_station = tk.Label(root, text="User 2 Station:")
label_user2_station.grid(row=1, column=0)
combo_user2_station = ttk.Combobox(root, values=stations['Station'].tolist())
combo_user2_station.grid(row=1, column=1)

# Hide dropdowns initially
label_user1_station.grid_remove()
combo_user1_station.grid_remove()
label_user2_station.grid_remove()
combo_user2_station.grid_remove()

# Create a toggle button to switch between input modes
toggle_button = tk.Button(root, text="Use Dropdown", command=toggle_input_mode)
toggle_button.grid(row=4, column=0, columnspan=2)

# Create a submit button
submit_button = tk.Button(root, text="Find Equal-Time Destination", command=on_submit)
submit_button.grid(row=5, column=0, columnspan=2)

# Run the main loop
root.mainloop()