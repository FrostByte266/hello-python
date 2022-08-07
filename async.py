"""
This module demonstrates how to use asnyncio to process multiple tasks at the same time
"""
import asyncio
import aiohttp
import json

# Load private API key from file
with open('keys.json') as f:
    data = json.load(f)
    key = data['key']
    
async def get_temperature_at(place: str) -> float:
    """Gets the temperature for a location

    Parameters
    ----------
    place : str
        The location to fetch from

    Returns
    -------
    float
        The temperature in degrees
    """
    async with aiohttp.ClientSession() as session: # Creates an HTTP session
        async with session.get('https://api.openweathermap.org/data/2.5/weather', params={'q': place, 'units': 'imperial', 'appid': key}) as res: # Send a GET request
            data = await res.json() # Parse response into dictionary
            return data['main']['temp']


# This is called an import guard, it prevents this from running
# when the file is imported from another file
if __name__ == '__main__':
    cities = ['Coon Rapids', 'Hesperia', 'Miami', 'Los Angeles', 'Chicago']

    loop = asyncio.get_event_loop() # Event loops are what run asnychronuc functions
    temps = loop.run_until_complete(asyncio.gather(*[get_temperature_at(city) for city in cities])) # Creates many coroutines to all run concurrently

    print(temps) # Prints out the result
