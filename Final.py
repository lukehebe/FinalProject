import requests
import time

def get_iss_location():
    url = "https://api.wheretheiss.at/v1/satellites/25544"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def print_iss_location(location_data):
    if location_data:
        print("International Space Station (ISS) Current Location:")
        print(f"Latitude: {location_data['latitude']}")
        print(f"Longitude: {location_data['longitude']}")
        print(f"Altitude: {location_data['altitude']} km")
        print(f"Timestamp: {location_data['timestamp']}")
    else:
        print("Failed to retrieve ISS location.")

def main():
    while True:
        iss_location = get_iss_location()
        print_iss_location(iss_location)
        print("\nUpdating every 10 seconds. Press Ctrl+C to exit.\n")
        time.sleep(10)

if __name__ == "__main__":
    main()
