#load some buildings tho
import os
import sys
import re
import json

buildings_filepath = '/Users/Angela/spe/Backend/buildings' #filepath

class FloorGraph(object):
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
	id = 1
	connections = []
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
		file_names = re.compile("floor[A-F]*[0-9]*.txt")
		floors = {}
		for files in dirs:
			if file_names.match(files):
				text = json.loads(open(files).read())
				if text['building'] == name and ('floor' + str(text['floor']) +'.txt') == files:
					floors[files[:-4]] = FloorGraph(text['image'], text['nodes'], text['edges'], text['scale'])
		self.floors = floors

		stairs = {}
		elevator = {}
		##set abosolute ID for nodes
		for floor_id in self.floors:
			floor_val = floor_id[5:] #get floor number
			floor = self.floors[floor_id]
			for node in floor.nodes:
				node['abs_id'] = "PU." + str(self.id) + "." + str(floor_val) + "." + str(node['id'])
				if node['type'] == 'stairs':
					stairset = node['stairset']
					if stairset in stairs:
						stairs[stairset].append(node)
					else:
						stairs[stairset] = [node]
				if node['type'] == 'elevator':
					stairset = node['stairset']
					if stairset in elevator:
						elevator[stairset].append(node)
					else:
						elevator[stairset] = [node]
				#if node['type'] == 'entry'
			for edge in floor.edges:
				abs_coords = ["PU." + str(self.id) + "." + str(floor_val) + "." + str(edge['coords'][0]), "PU." + str(self.id) + "." + str(floor_val) + "." + str(edge['coords'][1])]
				edge['abs_coords'] = abs_coords

		eConnections = []
		sConnections = []
		for stairsets in stairs:
			stairset = stairs[stairsets] #set of nodes in stairset
			for nodeA in stairset:
				up = ''
				down = ''
				upNode = ''
				downNode = ''
				if nodeA['up'] != "":
					up = nodeA['up']
				if nodeA['down'] != "":
					down = nodeA['down']
				for node in stairset:
					index = re.search(re.compile("PU\.[0-9]+\.([A-F]*[0-9]*)\.[0-9]+"), node['abs_id']).group(1)
					if index == up:
						upNode = node
					if index == down:
						downNode = node
				if upNode != "":
					coords = [nodeA['abs_id'], upNode['abs_id']]
					if not [upNode['abs_id'], nodeA['abs_id']] in sConnections:
						sConnections.append(coords)
				if downNode != "":
					coords = [nodeA['abs_id'], downNode['abs_id']]
					if not [downNode['abs_id'], nodeA['abs_id']] in sConnections:
						sConnections.append(coords)

		for stairset in elevator:
			stairset = elevator[stairsets] #set of nodes in stairset
			for nodeA in stairset:
				for nodeB in stairset:
					coords = [nodeA['abs_id'], nodeB['abs_id']]
					if coords[0] is not coords[1]:
						eConnections.append(coords)
		#remove duplicates
		for connection in eConnections:
			for connectionB in eConnections:
				if connectionB[0] == connection[1] and connectionB[1] == connection[0]:
					eConnections.remove(connectionB)
		self.eConnections = eConnections
		self.sConnections = sConnections
		os.chdir(old_directory)
