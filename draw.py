from display import *

#def plot( screen, color, x, y ):
#0=(dy)x-(dx)y+(dx)b
#0=Ax+By+C
def draw_line( x0, y0, x1, y1, screen, color ):
	dy = y1-y0
	dx = x1-x0
	A = dy
	B = -dx
	x = x0
	y = y0

	# 0 < dy/dx < 1 
	# Octant 1
	if (0 < dy < dx): 
		d= 2*A+B
		while (x <= x1):
			plot(screen, color, x, y)
			if (d>0):
				y+=1	
				d+=2*B
			x+=1
			d+=2*A


	# 1 < dy/dx 
	# Octant 2
	elif (dx < dy):
		d = A+2*B
		while (y <= y1):
			plot(screen, color, x, y)
			if (d<0):
				x+=1	
				d+=2*A
			y+=1
			d+=2*B



	# -1 < dy/dx < 0
	# Octant 8
	elif (-dx < dy < 0):
		d = 2*A-B
		while (x <= x1):
			plot(screen, color, x, y)
			if (d<0):
				y-=1
				d-=2*B
			x+=1
			d+=2*A



	# dy/dx < -1
	# Octant 7
	elif (dy < -dx):	
		d = A-2*B
		while (y >= y1):
			plot(screen, color, x, y)
			if (d>0):
				x+=1
				d+=2*A
			y-=1
			d-=2*B

	# dy/dx = 1
	elif (dy == dx):	
		while (x <= x1):
			plot(screen, color, x, y)
			x+=1
			y+=1


	# dy/dx = -1
	elif (dy == -dx):
		while (x <= x1):
			plot(screen,color, x,y)
			x+=1
			y-=1

	# dy/dx = 0
	elif (dy == 0) :
		while (x<=x1):
			plot(screen, color, x,y)
			x+=1


	# dy/dx = infinity
	elif (dx== 0 and dy > 0):
		while (y<=y1):
			plot(screen,color,x,y)
			y+=1


	# dy/dx = -infinity	
	elif (dx == 0 and dy < 0):
		while (y>=y1):
			plot(screen,color,x,y)
			y-=1


	pass