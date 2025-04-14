import requests
api_key ="8759aaaf48cf1d557bbee84cf63cba24"
city = input("Enter the city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
if response.status_code ==200:
    data = response.json()
    temp= data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    wind_direction = data['wind']['deg']
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Wind Direction: {wind_direction}°")
else: print("City not found. Please check the name and try again.")