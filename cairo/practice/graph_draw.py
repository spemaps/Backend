
import math
import cairo
import json

filename = raw_input('filename: ')
graph = json.loads(open(filename).read())
image = graph.get('image')
nodes = graph.get('nodes')
edges = graph.get('edges')

colorDict= {"F": [255, 160, 255], "M": [99, 184, 240], "room":[255, 48, 48], "stairs": [24, 116, 205], "elevator": [255, 215, 0], "entry": [0, 128, 0]}

# set background image
surface = cairo.ImageSurface.create_from_png (image)

context = cairo.Context (surface)

WIDTH = cairo.ImageSurface.get_width(surface)
HEIGHT = cairo.ImageSurface.get_height(surface)

#context.scale (WIDTH, HEIGHT)
SCALE = 1000


def x_scale (x):
	return (x + .5) * WIDTH / SCALE

def y_scale (y):
	return (y + .5) * WIDTH / SCALE

def draw_node(cx,cy,r, rgb):
	context.arc(x_scale(cx), y_scale(cy), r, 0, 2 * math.pi)
	context.set_source_rgb(rgb[0]/255.0,rgb[1]/255.0,rgb[2]/255.0)
	context.fill()
	context.stroke()


#function to draw edges
def draw_edge(x0,y0,x1,y1, rgb, width):
	context.move_to(x_scale(x0),y_scale(y0))
	context.line_to(x_scale(x1),y_scale(y1))
	context.set_source_rgb(rgb[0]/255.0,rgb[1]/255.0,rgb[2]/255.0)
	context.set_line_width(width)
	context.stroke()


def draw_graph():
	for edge in edges:
		node_1 = edge.get('coords')[0]
		node_2 = edge.get('coords')[1]
		coords_1 = 0
		coords_2 = 0
		for node in nodes:
			if node.get('id') is node_1:
				coords_1 = node.get('coords')
			if node.get('id') is node_2:
				coords_2 = node.get('coords')
		draw_edge(coords_1[0], coords_1[1], coords_2[0], coords_2[1], [0,0,0], 1)

	for node in nodes:

		if node.get('type') != 'walk':
			draw_node(node.get('coords')[0], node.get('coords')[1], 4, colorFind(node.get('id')))

			
def colorFind(my_id):
	my_type = ""
	for node in nodes:
		if node.get('id') == my_id:
			my_type = node.get('type')
			if my_type == 'bathroom': my_type = node.get('gender')
	return colorDict.get(my_type)
	

def draw_path(path):
	result = {"key": "value"}
	for edge in path:
		node_1 = edge[0]
		node_2 = edge[1]
		coords_1 = 0
		coords_2 = 0
		for node in nodes:
			if node.get('id') is node_1:
				coords_1 = node.get('coords')
			if node.get('id') is node_2:
				coords_2 = node.get('coords')
		draw_edge(coords_1[0], coords_1[1], coords_2[0], coords_2[1], [255, 0, 0], 3)
		#find start and end nodes
		if not node_1 in result:
			result[node_1] = 1 
		else: result[node_1] += 1
		if not node_2 in result:
			result[node_2] = 1
		else: result[node_2] += 1
	endpoints = []
	for key in result:
		if result.get(key) is 1:
			endpoints.append(key)
	for node in nodes: #draw endpoints
		if node['id'] is endpoints[0] or node['id'] is endpoints[1]:
			draw_node(node.get('coords')[0], node.get('coords')[1], 4, [255,0,0])


draw_graph()
draw_path([[3,2],[4,3],[5,4],[5,7],[9,7],[10,9]])

new_image = 'graph' + image
surface.write_to_png (new_image) # Output to PNG
