# program to calculate area of basic geometrical shapes
print("Launching Area Calculator")
shape = raw_input("Enter one of the options listed: \n 1.S for square \n 2.R for Rectangle \n 3.C for circle \n 4.T for triangle \n")
if shape.upper() == "S":
	sideSquare = float(raw_input("Enter the value of side of the square:"))
	areaSquare = sideSquare ** 2
	print "Area of the Square is :%s" %(areaSquare)
elif shape.upper() == "R":
	rectLen = float(raw_input("Enter the length of the rectangle:"))
  	rectBreadth = float(raw_input("Enter the breadth of the rectangle:"))
	areaRect = rectLen * rectBreadth
	print areaRect
elif shape.upper() == "C":
	radius=float(raw_input("Enter the radius of the circle:"))
  	areaCircle=float( (3.14159 * (radius **2)))
  	print areaCircle
elif shape.upper() == "T":
	base = float(raw_input("Enter the base value of the triangle:"))
  	height = float(raw_input("Enter the height of the triangle:"))
  	areaTri = float(0.5*base*height)
  	print "Area of Triangle: %s" %(areaTri)
else:
  	print("Invalid Option! Please choose one of the above:")
  
print("Exiting Program!")
 
  
  
   

