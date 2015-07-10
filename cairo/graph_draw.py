import math
import cairo
import json

filename = raw_input('filename: ')
graph = json.loads(open(filename).read())
print graph
image = graph.get('image')
print image
nodes = graph.get('nodes')
edges = graph.get('edges')



# set background image
surface = cairo.ImageSurface.create_from_png (image)

context = cairo.Context (surface)

WIDTH = cairo.ImageSurface.get_width(surface)
HEIGHT = cairo.ImageSurface.get_height(surface)

context.scale (WIDTH, HEIGHT)


def x_scale (x):
	width = 1000.0
	return (x + .5) / width

def y_scale (y):
	height = 1000.0 * HEIGHT / WIDTH
	return (y + .5) / height

def draw_node(cx,cy,r):
	context.arc(x_scale(cx), y_scale(cy), r, 0, 2 * math.pi)
	context.set_source_rgb(0,0,0)
	context.stroke()

#function to draw edges
def draw_edge(x0,y0,x1,y1):
	context.move_to(x_scale(x0),y_scale(y0))
	context.line_to(x_scale(x1),y_scale(y1))
	context.set_source_rgb(0,0,0)
	context.set_line_width(0.005)
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
		draw_edge(coords_1[0], coords_1[0], coords_2[0], coords_2[1])

	for node in nodes:
		draw_node(node.get('coords')[0], node.get('coords')[1], .01)

draw_graph()

new_image = 'graph' + image
surface.write_to_png (new_image) # Output to PNG
