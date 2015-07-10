import math
import cairo
<<<<<<< Updated upstream
import json

tx = open("floor3.txt").read()
json.loads(tx)

print tx
=======


>>>>>>> Stashed changes

#WIDTH, HEIGHT = 600, 600

#surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
# set background image
surface = cairo.ImageSurface.create_from_png ('floor2.png')
WIDTH = cairo.ImageSurface.get_width(surface)
HEIGHT = cairo.ImageSurface.get_height(surface)
context = cairo.Context (surface)


context.scale (WIDTH, HEIGHT) # Normalizing the canvas

<<<<<<< Updated upstream
pat = cairo.LinearGradient (0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba (0.0, 0.0, 0.8, 0, 0.5) # Last stop, 100% opacity
pat.add_color_stop_rgba (0.5 * HEIGHT, 0.0, 0.4, 0.4, 0.5) # Last stop, 100% opacity
pat.add_color_stop_rgba (HEIGHT, 0.9, 0.2, 0.0, 0.5) # First stop, 50% opacity


context.rectangle (0, 0, WIDTH, HEIGHT) # Rectangle(x0, y0, x1, y1)
context.set_source (pat)
context.fill ()

#function to draw nodes
def draw_node(cx,cy,r):
	context.arc(cx, cy, r, 0, 2 * math.pi)
	context.set_source_rgb(0,0,0)
	context.stroke()

#function to draw edges
def draw_edge(x0,y0,x1,y1):
	context.move_to(x0,y0)
	context.line_to(x1,y1)
	context.set_source_rgb(0,0,0)
	context.set_line_width(0.02)
	context.stroke()

#context.translate (0.1, 0.1) # Changing the current transformation matrix

context.move_to (0.1, 0.1)
context.arc (0.2, 0.1, 0.1, -math.pi/2, 0) # Arc(cx, cy, radius, start_angle, stop_angle)
context.line_to (0.5, 0.1) # Line to (x,y)
context.curve_to (0.5, 0.2, 0.5, 0.4, 0.2, 0.8) # Curve(x1, y1, x2, y2, x3, y3)
#context.close_path ()


context.move_to(0.2, 0.1)
context.line_to (.9, 0.2)
=======

ctx.move_to (0.1, 0.1)

ctx.line_to (.2, 0.2)
>>>>>>> Stashed changes

context.set_source_rgb (0.5, 0.0, 0.7) # Solid color
context.set_line_width (.02)
context.stroke ()

<<<<<<< Updated upstream
surface.write_to_png ("example6.png") # Output to PNG
=======
surface.write_to_png ("yay.png") # Output to PNG
>>>>>>> Stashed changes
