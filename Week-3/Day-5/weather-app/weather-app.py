from pyowm import OWM

owm = OWM('93ff977522c7e59d4a64221479d96b55')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('Tel Aviv,IL')
w = observation.weather

temp = w.temperature('celsius')['temp']
wind_speed = w.wind()['speed']
sunrise = w.sunrise_time(timeformat='iso')
sunset = w.sunset_time(timeformat='date')

print(f"The temperature in Tel Aviv is {temp} degrees Celsius. With a wind speed of {wind_speed} meters per second.")
print(f"The sunrise is at {sunrise} and the sunset at {sunset}")