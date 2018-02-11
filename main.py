from display import *
from draw import *

#500 x500
screen = new_screen()

color1 = [0, 0, 255]
draw_line(0,0, 250, 500, screen, color1)
color2 = [0, 255, 255]
draw_line(0,0, 500, 250, screen, color2)
color3 = [120,250,90]
draw_line(0,500, 500, 250, screen, color3)
color4 = [0, 255, 0]
draw_line(0,500, 250, 0, screen, color4)
color5 = [0,255,0]
draw_line(0,0,500,500, screen, color5)
color6 = [255,0,0]
draw_line(0,500,500,0, screen, color6)
color7 = [255,0,0]
draw_line(0,250,500,250, screen,color7)
color8= [0,0,255]
draw_line(0,0,0,500, screen, color8)
color9= [255,0	,120]
draw_line(499, 499, 499,0, screen, color9)
display(screen)
save_extension(screen, 'pic.ppm')