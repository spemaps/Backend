
import math
import cairo
import json
import sys
from PIL import Image

class PictureGraph(object):
	def __init__(self, building, floor):
		self.building = building
		self.floor = floor
		self.image = building.floors[floor].image
		self.nodes = building.floors[floor].nodes
		self.edges = building.floors[floor].edges
		self.surface = cairo.ImageSurface.create_from_png(self.image)
		self.context = cairo.Context(self.surface)
		self.WIDTH = cairo.ImageSurface.get_width(self.surface)
		self.HEIGHT = cairo.ImageSurface.get_height(self.surface)
		self.colorDict= {"F": [255, 160, 255], "M": [99, 184, 240], "room":[255, 48, 48], "stairs": [24, 116, 205], "elevator": [255, 215, 0], "entry": [0, 128, 0]}
		self.SCALE = 1000

	def x_scale (self, x):
		return (x + .5) * self.WIDTH / self.SCALE

	def y_scale (self, y):
		return (y + .5) * self.WIDTH / self.SCALE

	def draw_node(self, cx,cy,r, rgb):
		self.context.arc(self.x_scale(cx), self.y_scale(cy), r, 0, 2 * math.pi)
		self.context.set_source_rgb(rgb[0]/255.0,rgb[1]/255.0,rgb[2]/255.0)
		self.context.fill()
		self.context.stroke()

	#function to draw edges
	def draw_edge(self, x0,y0,x1,y1, rgb, width):
		self.context.move_to(self.x_scale(x0),self.y_scale(y0))
		self.context.line_to(self.x_scale(x1),self.y_scale(y1))
		self.context.set_source_rgb(rgb[0]/255.0,rgb[1]/255.0,rgb[2]/255.0)
		self.context.set_line_width(width)
		self.context.stroke()


	def draw_graph(self):
		for edge in self.edges:
			node_1 = edge.get('coords')[0]
			node_2 = edge.get('coords')[1]
			coords_1 = 0
			coords_2 = 0
			for node in self.nodes:
				if node.get('id') is node_1:
					coords_1 = node.get('coords')
				if node.get('id') is node_2:
					coords_2 = node.get('coords')
			self.draw_edge(coords_1[0], coords_1[1], coords_2[0], coords_2[1], [0,0,0], 1)

		for node in self.nodes:

			if node.get('type') != 'walk':
				self.draw_node(node.get('coords')[0], node.get('coords')[1], 4, self.colorFind(node.get('id')))

				
	def colorFind(self, my_id):
		my_type = ""
		for node in self.nodes:
			if node.get('id') == my_id:
				my_type = node.get('type')
				if my_type == 'bathroom': my_type = node.get('gender')
		return self.colorDict.get(my_type)
		

	def draw_path(self, path):
		first_coords = None
		prev_coords = None
		for node in path:
			for nodeA in self.nodes:
				if nodeA['abs_id'] == node:
					coords = nodeA.get('coords')
			if prev_coords is not None:
				self.draw_edge(prev_coords[0], prev_coords[1], coords[0], coords[1], [255, 0, 0], 3)
			else:
				first_coords = coords
			prev_coords = coords
		#draw endpoints
		self.draw_node(prev_coords[0], prev_coords[1], 4, [255,0,0])
		self.draw_node(first_coords[0], first_coords[1], 4, [255,0,0])

	def show(self):
		self.save()
		new_image = 'graph' + self.image
		Image.open(new_image).show()

	def save(self):
		new_image = 'graph' + self.image
		self.surface.write_to_png(new_image) # Output to PNG

