import requests

geodata = requests.get('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson')
geodata.json()


