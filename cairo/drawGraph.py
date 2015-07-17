
import math
import cairo
import json
import sys

building = sys.argv[0]
floor = sys.argv[1]
path = sys.argv[2]

image = building.floors[floor].image
nodes = building.floors[floor].nodes
edges = building.floors[floor].edges

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
	first_coords = None
	prev_coords = None
	for node in path:
		for nodeA in nodes:
			if nodeA['abs_id'] == node:
				coords = nodeA.get('coords')
		if prev_coords is not None:
			draw_edge(prev_coords[0], prev_coords[1], coords[0], coords[1], [255, 0, 0], 3)
		else:
			first_coords = coords
		prev_coords = coords
	#draw endpoints
	draw_node(prev_coords[0], prev_coords[1], 4, [255,0,0])
	draw_node(first_coords[0], first_coords[1], 4, [255,0,0])



draw_graph()
draw_path(path)

new_image = 'graph' + image
surface.write_to_png (new_image) # Output to PNG
