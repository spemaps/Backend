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

	return path


#return in list of dicitonaries [{"floor":"floor#", "path":[nodes in path]}]