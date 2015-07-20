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

building = Building('csbuilding')
networkGraph = NetworkGraph(building)
begin = raw_input('start: ').lower()
dest = raw_input('destination: ').lower()

#make lowercase
beginNumber = re.search(re.compile("([0-9]+[a-z]?)"), begin).group(1)
destNumber = re.search(re.compile("([0-9]+[a-z]?)"), dest).group(1)
start = ''
end = ''
for floor in building.floors:
	for node in building.floors[floor].nodes:
		if node['type'] == 'room':
			if node['room'] == beginNumber:
				start = node['abs_id']
			if node['room'] == destNumber:
				end = node['abs_id']

if start != '' and end != '':
	path = networkGraph.dijkstra(start, end)

	floorPaths = pathSort(path)

	for floorPath in floorPaths:
		floor = floorPath['floor']
		path = floorPath['path']
		pictureGraph = PictureGraph(building, floor)
		#pictureGraph.draw_graph()
		pictureGraph.draw_path(path)
		pictureGraph.show()
elif start == '':
	print 'Invalid start'
else:
	print 'Invalid destination'
