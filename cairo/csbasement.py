import math
import cairo



import json

tx = open("floor3.txt").read()
json.loads(tx)

print tx


#WIDTH, HEIGHT = 600, 600

#surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
# set background image
surface = cairo.ImageSurface.create_from_png ('walker-02.png')
WIDTH = cairo.ImageSurface.get_width(surface)
HEIGHT = cairo.ImageSurface.get_height(surface)
ctx = cairo.Context (surface)

print WIDTH #2550
print HEIGHT #1650

ctx.scale (WIDTH, HEIGHT) # Normalizing the canvas

pat = cairo.LinearGradient (0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba (0.0, 0.0, 0.8, 0, 0.5) # Last stop, 100% opacity
pat.add_color_stop_rgba (0.5 * HEIGHT, 0.0, 0.4, 0.4, 0.5) # Last stop, 100% opacity
pat.add_color_stop_rgba (HEIGHT, 0.9, 0.2, 0.0, 0.5) # First stop, 50% opacity


ctx.rectangle (0, 0, WIDTH, HEIGHT) # Rectangle(x0, y0, x1, y1)
ctx.set_source (pat)
ctx.fill ()

#ctx.translate (0.1, 0.1) # Changing the current transformation matrix

ctx.move_to (0.1, 0.1)
ctx.arc (0.2, 0.1, 0.1, -math.pi/2, 0) # Arc(cx, cy, radius, start_angle, stop_angle)
ctx.line_to (0.5, 0.1) # Line to (x,y)
ctx.curve_to (0.5, 0.2, 0.5, 0.4, 0.2, 0.8) # Curve(x1, y1, x2, y2, x3, y3)
#ctx.close_path ()


ctx.move_to(0.2, 0.1)
ctx.line_to (.9, 0.2)

ctx.set_source_rgb (0.5, 0.0, 0.7) # Solid color
ctx.set_line_width (.02)
ctx.stroke ()

surface.write_to_png ("example6.png") # Output to PNG
