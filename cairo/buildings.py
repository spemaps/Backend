#load some buildings tho
import os
import sys
import re
import json

buildings_filepath = '/Users/Angela/spe/Backend/buildings' #filepath

class Graph(object):
	def __init__(self, image, nodes, edges, scale):
		self.image = image
		self.nodes = nodes
		self.edges = edges
		self.scale = scale


class Building(object):
	floors = {}
	main = None
	entrypoints = None
	directory = None
	def __init__(self, name):
		self.name = name
		old_directory = os.getcwd()
		if (os.path.basename(os.getcwd()) != name): # not in directory change to directory
			os.chdir(os.path.join(buildings_filepath, name))
		#load all the stuff
		self.main = json.loads(open('main.txt').read()) #main.txt
		self.entrypoints = json.loads(open('entrypoints.txt').read())#entrypoints.txt
		self.directory = os.getcwd() #directory
		dirs = os.listdir(self.directory)
		file_names = re.compile("floor(-)?[0-9]+.txt")
		for files in dirs:
			print files
			if file_names.match(files):
				text = json.loads(open(files).read())
				if text['building'] == name and ('floor' + str(text['floor']) +'.txt') == files:
					floors[files] = Graph(text['image'], text['nodes'], text['edges'], text['scale'])
		self.floors = floors
		os.chdir(old_directory)

csbuilding = Building('csbuilding')
