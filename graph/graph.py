#Graph data structure

class Vertex:
	def __init__(self, key):
		self.id = key
		self.edges = {}

	def addEdge(self, neighbor, weight):
		self.edges[neighbor] = weight

class Graph:
	def __init__(self):
		self.list = {}
		self.size = 0

	def addVertex(self, key):
		vertex = Vertex(key)
		self.list[key] = vertex
		self.size = self.size + 1

	def addEdge(self, vert, neighbor, weight): ##should we make it be double sided?
		if vert not in self.list:
			vertex = self.addVertex(vert)
		if neighbor not in self.list:
			vertex = self.addVertex(neighbor)
		self.list[vert].addEdge(self.list[neighbor], weight)
		# self.list[neighbor].addEdge(self.list[vert], weight) #will add edge to both sides

	def __contains__(self, key):
		return key in self.list

	def __iter__(self):
		return iter(self.list.values())
