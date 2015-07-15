#building to graph
#create a graph from a building
from graph.py import Vertex
from graph.py import Graph
from buildings.py import floorGraph
from buildings.py import Building

#load some buildings tho
#import os
#import sys
#import re
#import json




def calculateWeight(floor, edge):
	nodes = building.floors[floor].nodes
	coordsA = []
	coordsB = []
	weight = 0
	for node in nodes:
		if edge.coords[0] is node.id:
			coordsA = node.coords
		if edge.coords[1] is node.id:
			coordsB = node.coords
	weight = Math.sqrt((coordsB[0] - coordsA[0]) * (coordsB[0] - coordsA[0]) + (coordsB[1] - coordsA[1])*(coordsB[1] - coordsA[1]))
	return weight



buildingName = raw_input("building: ")
building = Building(buildingName) #whichever building to import

graph = Graph()

for floorid in building.floors:
	floor = building.floors[floorid]
	edges = floor.edges
	for edge in edges: #assuming every node is connected to an edge
		weight = calculateWeight(floorid, edge)
		graph.addEdge(edge.coords[0], edge.coords[1], weight)
		graph.addEdge(edge.coords[1], edge.coords[0], weight)













