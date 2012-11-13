import ASCIIGL, math
from ASCIIGLConstants import *

class STATE(object):
	ROOT op0, op1, op2, op3 = range(5)


class TextButton(object):
	
	def __init__(x, y, sx, sy, vert, horiz, a, b, c, d, fill, PrimaryText, minorText):
	
		self.x            = x            
		self.y            = y            
		self.sx           = sx           
		self.sy           = sy           
		self.vert         = vert         
		self.horiz        = horiz        
		self.a            = a            
		self.b            = b            
		self.c            = c            
		self.d            = d            
		self.fill         = fill         
		self.primaryText  = primaryText  
		self.minorText    = minorText    
		
		self.renderer     = renderer
	
	def draw():
	
		#We don't use the built in rectangle.
		
		#Draw the fill of the rectangle.
		for i in range(sx-2):
			for k in range(sy-2):
				renderer.character(x+i+1, y+k+1, fill)
		
		#Draw the top and bottom rows.
		for i in range(sx-2):
			renderer.character(x+i+1, y, horiz)
			renderer.character(x+i+1, 
		
	
		
		
		