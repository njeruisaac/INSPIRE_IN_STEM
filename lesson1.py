#Volume of a Cube

length = int(input("What is the Length of the Cube"))
volume = length * length * length
print("Volume of the cube is equals to " + str(volume) + "cm3")

#Surface area of a Cylinder
radius = int(input("What is the Radius of the cylinder"))
height = int(input("What is the Height of the cylinder"))
PI= 3.142
surfaceArea= 2 * PI * radius * height + 2 * PI * radius * radius 
print("The suface area of the cylinder is " + str(surfaceArea) + "cm2")

#Volume of a Cylinder
volume_cylinder = PI * radius * radius * height
radius = int(input("Radius of the Cylinder"))
height = int(input("Height of the cylinder"))
print("The volume of the cylinder is " + str(volume_cylinder) + "cm3")