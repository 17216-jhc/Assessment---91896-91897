#_____  sources  _____
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-rectangle/
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-triangle/

# ____________   IMPORTS ________________

# ____________   FUNCTIONS ________________

# ____________   MAIN  ________________
b=int(input("Length : "))
h=int(input("Height : "))
area=0.5 * b * h

print("Area of Triangle : ",area)
 
l=int(input("Length : "))
w=int(input("Width : "))
area=l*w
perimeter=2*(l+w)

print("Area of Rectangle : ",area)
print("Perimeter of Rectangle : ",perimeter)

