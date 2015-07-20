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
			if 'accesibility' in edge:
				G.edge[absCoords[0]][absCoords[1]]['accesibility'] = edge['accesibility']
	for connection in building.sConnections:
		G.add_edge(connection[0], connection[1], weight = 1)
	for connection in building.eConnections:
		G.add_edge(connection[0], connection[1], weight = 2)
	for floor in building.floors:
		for node in building.floors[floor].nodes:
			G.add_node(node['abs_id'], node)
	return G


def removeNodes(nodeList):
	removed = {}
	for node in nodeList:
		removed[node] = G[node]
		G.remove_node(node)
	return removed

def addNodes(removeList):
	for node in removeList:
		for connection in removeList[node]:
			G.add_edge(node, connection, removeList[node][connection])


def removeEdge(edge): #[coordA, coordB]
	removed = {'edge':edge, 'properties':G[edge[0]][edge[1]]}
	G.remove_edge(edge[0], edge[1])
	return removed

def addEdge(edge, properties): #edge is list of nodes, properties is dictionary
	G.add_edge(edge[0], edge[1], properties)



