from buildings import Building
from networkGraph import NetworkGraph
from drawGraph import PictureGraph
import re
import sys


def pathSort(pathList): #pathlist = list of nodes in path
	pathSort = {} #floor:[nodes in path on floor]
	path = []
	#determine which nodes belong to each floor, sort
	for node in pathList:
		floor = re.search(re.compile("PU\.[0-9]+\.([A-F]*[0-9]*)\.[0-9]+"), node).group(1)
		if floor in pathSort:
			floorlist = pathSort[floor]
			floorlist.append(node)
			pathSort[floor] = floorlist
		else:
			pathSort[floor] = [node]

	for floor in pathSort:
		nodelist = pathSort[floor]
		floorname = "floor" + str(floor)
		if len(nodelist) > 1:
			path.append({"floor":floorname, "path":nodelist})
	return path   #return in list of dicitonaries [{"floor":"floor#", "path":[nodes in path]}]

csbuilding = Building('csbuilding')
networkGraph = NetworkGraph(csbuilding)
start = 'PU.1.1.29'
end = 'PU.1.4.66'
path = networkGraph.dijkstra(start, end)

floorPaths = pathSort(path)

for floorPath in floorPaths:
	floor = floorPath['floor']
	path = floorPath['path']
	pictureGraph = PictureGraph(csbuilding, floor)
	pictureGraph.draw_graph()
	pictureGraph.draw_path(path)
	pictureGraph.show()
