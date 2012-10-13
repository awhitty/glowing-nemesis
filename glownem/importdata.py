import xml.dom.minidom
import os
import re

def getText(nodelist):
	rc = []
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc.append(node.data)
	return ''.join(rc)

def getByName(node, key):
	return getText(node.getElementsByTagName(key)[0].childNodes)

def handleMovieList(dictionary, list):
	movies = list.getElementsByTagName("movie")
	for movie in movies:
		handleMovie(dictionary, movie)

def handleMovie(dictionary, movie):
	title = getByName(movie, "title").encode("utf8", "ignore")
	
	try:
		locationList = dictionary[title]
	except KeyError:
		locationList = []
		dictionary[title] = locationList
	
	locations = movie.getElementsByTagName("location")
	handleLocations(locationList, locations)

def handleLocations(movie, locations):
	for location in locations:
		handleLocation(movie, location)

def handleLocation(movie, location):
	coords = getByName(location, "coordinates")
	movie.append(coords.encode("utf8", "ignore"))

def makePretty(name):
	return name

movies = {}

path = "/Users/Max/Desktop/glowing-nemesis/data/"
output = open("/Users/Max/Desktop/movielist.txt", "w")
for line in os.listdir(path):
	if re.match(".+\.xml", line):
		fullpath = (path + line)
		dom = xml.dom.minidom.parse(fullpath)
		handleMovieList(movies, dom)

def outputMovie(key, name, file):
	file.write("  {\n")
	file.write("    \"model\": \"movies.movie\",\n")
	file.write("    \"pk\": %i,\n" % key)
	file.write("    \"fields\": {\n")
	file.write("      \"name\": \"" + name + "\"\n")
	file.write("    }\n")
	file.write("  },\n")

def outputLocation(movie, key, coordinates, file):
	file.write("  {\n")
	file.write("    \"model\": \"movies.location\",\n")
	file.write("    \"pk\": %i,\n" % key)
	file.write("    \"fields\": {\n")
	file.write("      \"movie\": %i,\n" % movie)
	file.write("      \"longitude\": " + coordinates[coordinates.find(",")+1:] + ",\n")
	file.write("      \"latitude\": " + coordinates[:coordinates.find(",")] + "\n")
	file.write("    }\n")
	file.write("  },\n")

movie_key = 1
location_key = 1
for key in movies:
	if len(key) > 0:
		outputMovie(movie_key, makePretty(key), output)
		for location in movies[key]:
			outputLocation(movie_key, location_key, location, output)
			location_key += 1
		movie_key += 1

output.close()
