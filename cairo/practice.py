import networkx as nx
from matplotlib import pyplot as plt
import sys
import math

def calculateWeight(building, floor, edge):
	nodes = building.floors[floor].nodes
	coordsA = []
	coordsB = []
	weight = 0
	for node in nodes:
		if edge['coords'][0] is node['id']:
			coordsA = node['coords']
		if edge['coords'][1] is node['id']:
			coordsB = node['coords']
	weight = math.sqrt((coordsB[0] - coordsA[0]) * (coordsB[0] - coordsA[0]) + (coordsB[1] - coordsA[1])*(coordsB[1] - coordsA[1]))
	return weight

def buildingToGraph(building):
	G = nx.Graph()
	for floor in building.floors:
		for edge in building.floors[floor].edges:
			absCoords = edge['abs_coords']
			G.add_edge(absCoords[0], absCoords[1], weight = calculateWeight(building, floor, edge))
	for connection in building.sConnections:
		G.add_edge(connection[0], connection[1], weight = 1)
	for connection in building.eConnections:
		G.add_edge(connection[0], connection[1], weight = 2)
	return G


G = buildingToGraph(sys.argv[0])

path = nx.dijkstra_path(G, 'PU.1.1.29', 'PU.1.4.66')
print path

nx.draw(G)
plt.show()


