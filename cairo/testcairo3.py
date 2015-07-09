import math
import cairo

#Load a few images from files
surf1 = cairo_image_surface_create_from_png("example.png");
surf2 = cairo_image_surface_create_from_png("example4.png");

#Create the background image
img = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 100, 100);

#Create the cairo context
cr = cairo_create(img);

#Initialize the image to black transparent
cairo_set_source_rgba(cr, 0,0,0, 1);
cairo_paint(cr);

surface.write_to_png ("example5.png") # Output to PNG
