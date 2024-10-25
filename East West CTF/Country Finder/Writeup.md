# Country Finder Challenge Writeup

## Challenge Summary

In this challenge, we connected to a netcat (`nc`) server that provided multiple rounds, each consisting of latitude and longitude coordinates. For each round, we were required to:
1. Retrieve the country name for each set of coordinates.
2. Sort the country names alphabetically.
3. Send the sorted list back to the server within a specified time limit.

## Solution Strategy

To efficiently solve this, we used the **geopy** library, which allowed for straightforward access to country names from latitude and longitude coordinates. Here's the approach in detail:

1. **Establish Connection**: Connect to the server and start receiving coordinates.
2. **Extract Coordinates**: For each round, parse the data to extract latitude and longitude pairs.
3. **Reverse Geocode**: Use `Nominatim` from the geopy library to convert each set of coordinates into a country name.
4. **Sort and Send**: Sort the list of country names alphabetically, format it as required, and send it back to the server.
5. **Repeat**: Continue the above steps for each round until completion.

---

## Solution Code

Below is the Python code used to implement the solution:

```python
from pwn import remote
from geopy.geocoders import Nominatim

def reverse_geocode(latitude, longitude):
    try:
        geolocator = Nominatim(user_agent="geopy_example")
        location = geolocator.reverse((latitude, longitude), exactly_one=True, language='en')
        if location:
            return location.raw['address'].get('country')
    except Exception as e:
        print(f"Error during geocoding: {e}")
    return None

def connect_and_solve():
    server_address = ('chall.cbctf.xyz', 34163)
    conn = remote(*server_address)
    response = ''
    for round in range(100):
        if round == 0:
            data = conn.recv(4096).decode()
        else:
            data = response
        print(f"{data}")

        coordinates = extract_coordinates(data)
        if not coordinates:
            print("No coordinates found, exiting...")
            break

        countries = []
        for latitude, longitude in coordinates:
            country = reverse_geocode(latitude, longitude)
            if country:
                countries.append(country)
            else:
                print(f"Error: No country found for {latitude}, {longitude}")

        sorted_countries = sorted(countries)
        print(f"Sorted countries: {sorted_countries}")

        answer = ', '.join(sorted_countries)
        print(f"Sending answer: {answer}")

        conn.sendline(answer.encode())

        response = conn.recv(4096).decode()
        print(f"Server response:\n{response}")

def extract_coordinates(data):
    lines = data.split('\n')
    coordinates = []

    for line in lines:
        if "Latitude" in line and "Longitude" in line:
            try:
                lat_long = line.replace("Latitude: ", "").replace("Longitude: ", "").strip()
                lat, long = map(float, lat_long.split(","))
                coordinates.append((lat, long))
            except ValueError as e:
                print(f"Error parsing coordinates in line: '{line}' -> {e}")

    return coordinates if coordinates else None

if __name__ == "__main__":
    connect_and_solve()
