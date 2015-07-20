import networkx as nx
from matplotlib import pyplot as plt
import sys
import math

class NetworkGraph(object):
	def __init__(self, building):
		self.G = nx.Graph()
		self.buildingToGraph(building)

	def calculateWeight(self, floor, edge):
		nodes = self.building.floors[floor].nodes
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

	def buildingToGraph(self, building):
		self.building = building
		for floor in building.floors:
			for edge in building.floors[floor].edges:
				absCoords = edge['abs_coords']
				self.G.add_edge(absCoords[0], absCoords[1], weight = self.calculateWeight(floor, edge))
				if 'accesibility' in edge:
					self.G.edge[absCoords[0]][absCoords[1]]['accesibility'] = edge['accesibility']
		for connection in building.sConnections:
			self.G.add_edge(connection[0], connection[1], weight = 1)
		for connection in building.eConnections:
			self.G.add_edge(connection[0], connection[1], weight = 2)
		for floor in building.floors:
			for node in building.floors[floor].nodes:
				self.G.add_node(node['abs_id'], node)

	def dijkstra(self, start, end):
		return nx.dijkstra_path(self.G, start, end)

	def removeNodes(self, nodeList):
		removed = {}
		for node in nodeList:
			removed[node] = self.G[node]
			self.G.remove_node(node)
		return removed

	def addNodes(self, removeList):
		for node in removeList:
			for connection in removeList[node]:
				self.G.add_edge(node, connection, removeList[node][connection])


	def removeEdge(self, edge): #[coordA, coordB]
		removed = {'edge':edge, 'properties':self.G[edge[0]][edge[1]]}
		self.G.remove_edge(edge[0], edge[1])
		return removed

	def addEdge(self, edge, properties): #edge is list of nodes, properties is dictionary
		self.G.add_edge(edge[0], edge[1], properties)
