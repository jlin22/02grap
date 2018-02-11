from display import *

#def plot( screen, color, x, y ):
#0=(dy)x-(dx)y+(dx)b
#0=Ax+By+C
def draw_line( x0, y0, x1, y1, screen, color ):
	dy = y1-y0
	dx = x1-x0
	A = dy
	B = -dx
	# 0 < dy/dx < 1 
	# Octant 1
	if 0 < dy < dx : 
		x=x0, y=y0
		d=2*A+B
		while x <= x1:
    		plot(screen, color, x, y)	
    		if d>0:
   	    		y++
   	    		d+=2*B
   			x++
   			d+=2*A

	
	# 1 < dy/dx 
	# Octant 2
	elif dx < dy :

	}
	# -1 < dy/dx < 0
	# Octant 8
	elif -dx < dy < 0:

	# dy/dx < -1
	# Octant 7
	elif dy < -dx:	

	# dy/dx = 1
	elif dy = dx:	
	# dy/dx = -1
	elif dy = -dx :
	# dy/dx = 0
	elif dy = 0 :
	# dy/dx = infinity
	elif dx = 0 and dy > 0:
	# dy/dx = -infinity	
	elif dx = 0 and dy < 0:
    pass