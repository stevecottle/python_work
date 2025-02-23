import pandas as pd
from geopy.distance import geodesic
import requests

def load_stations(filename):
    """Load Tube station data from CSV."""
    return pd.read_csv(filename)

def find_nearest_station(user_coords, stations):
    """Find the nearest station to user coordinates."""
    nearest_station = None
    min_distance = float('inf')
    
    for _, station in stations.iterrows():
        station_coords = (station['Latitude'], station['Longitude'])
        distance = geodesic(user_coords, station_coords).km
        if distance < min_distance:
            min_distance = distance
            nearest_station = station['Station']
    
    return nearest_station

def get_travel_time(start_station_id, end_station_id, api_key):
    """Get travel time between stations using TfL API."""
    url = f"https://api.tfl.gov.uk/Journey/JourneyResults/{start_station_id}/to/{end_station_id}"
    params = {"app_key": api_key, "mode": "tube"}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'journeys' not in data or not data['journeys']:
            print(f"No journeys: {start_station_id} → {end_station_id}")
            return None
            
        return data['journeys'][0]['duration']
    except Exception as e:
        print(f"Error: {e}")
        return None

def find_equal_time_station(users, stations, api_key):
    """Find destination station with most equal travel times."""
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
    
    # Find station with minimum time variance
    best_station = None
    min_variance = float('inf')
    
    for station, times in travel_times.items():
        mean = sum(times)/len(times)
        variance = sum((t - mean)**2 for t in times)/len(times)
        if variance < min_variance:
            min_variance = variance
            best_station = station
    
    return best_station

if __name__ == "__main__":
    stations = load_stations("tube_stations.csv")
    
    # Example users (lat, lon)
    users = [
        (51.5048, -0.2185),  # Near Shepherd's Bush
        (51.5200, -0.1670)   # Near Edgware Road
    ]
    
    api_key = "YOUR_TFL_API_KEY"  # Replace with your key
    
    result = find_equal_time_station(users, stations, api_key)
    print(f"\nEqual-time destination: {result}")