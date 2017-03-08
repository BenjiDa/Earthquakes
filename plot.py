#import matplotlib.pyplot as plt
#import numpy as np
import requests
import json

#print(geodata.json())

#for item in geodata.json()['features']:
#	print item

# quit
url = 'http://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2016-01-01&endtime=2016-01-02&minmagnitude=2.5&latitude=38.9582&longitude=-122.6264&maxradius=10'
def retrieve_usgs_earthquak_data(url):
	geodata = requests.get(url) 
	return json.dumps(geodata.json(), sort_keys = True, indent=4)

url = 'http://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2016-01-01&endtime=2016-01-02&minmagnitude=2.5&latitude=38.9582&longitude=-122.6264&maxradius=10'
geodata = requests.get(url) 
map_data = geodata.json()['features']






# Plotting up data.
#x = []
#y = []

#x, y = np.loadtxt('plot/eqLocation.txt', delimiter='	', unpack=True)

#plt.plot(y,x, 'b.')
		
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Interesting Graph\nCheck it out')
#plt.legend()
#plt.show()

