import re
import gmplot
import numpy as np

''' Import of the coordinate file '''
coordinates = open('./geoloc_gendarmerie.csv', 'r')

''' World map centered on France '''
gmap = gmplot.GoogleMapPlotter(47, 2.4, 3)

''' Empty lists of latitudes and longitudes '''
lat = []
lon = []

''' For every line in the file '''
for line in coordinates:
	
	''' Extract columns with lat and lon '''
	latitude = re.sub('"', '', line.split(';')[11])
	longitude = re.sub('"', '', line.split(';')[12]).rstrip()
	
	if (longitude != '') and (latitude != '') and (re.findall('[0-9]', longitude)):
		''' And add converted to float value to lists '''
		lon.append(float(longitude))
		lat.append(float(latitude))

''' Path from A to B to C ... '''
#gmap.plot(lon, lat, 'cornflowerblue', edge_width=5)

''' And point map '''
gmap.scatter(lon, lat, '#d041e0', size=5000, marker=False)

''' Google symbol '''
#gmap.scatter(lon, lat, 'k', marker=True)

''' Heatmap '''
gmap.heatmap(lon, lat)

''' Final plot '''
gmap.draw("mymap.html")
