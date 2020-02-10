import math

#start with the cartesian input

print("Please provide the x, y and z coordinates:")

cartesianX = float(input("x: "))
cartesianY = float(input("y: "))
cartesianZ = float(input("z: "))

#define two separate recalculation functions so that they can be re-used in other code

def cartesianToSpherical(x, y, z):
    #calculate distance from the origin
    sphericalR = math.sqrt(x**2+y**2+z**2)
    R = round(sphericalR, 2)
    #calculate the theta angle and output the result in degrees,
    #rounding to the 2nd decimal point
    sphericalTheta = math.degrees(math.atan(y/x))
    Theta = round(sphericalTheta, 2)
    #do the same for the phi angle
    sphericalPhi = math.degrees(math.atan(math.sqrt(x**2+y**2)/z))
    Phi = round(sphericalPhi, 2)
    print("R =", R, "Theta =", Theta, "Phi =", Phi)

def cartesianToCylindrical(x, y, z):
    cylindricalR = math.sqrt(x**2+y**2+z**2)
    R = round(cylindricalR, 2)
    cylindricalTheta = math.degrees(math.atan(y/x))
    Theta = round(cylindricalTheta, 2)
    print("R =", R, "Theta =", Theta, "Z =", z)

print("Point coordinates in spherical system, rounded up to the 2nd decimal point: ")
cartesianToSpherical(cartesianX, cartesianY, cartesianZ)
print("Point coordinates in cylindrical system, rounded up to the 2nd decimal point: ")
cartesianToCylindrical(cartesianX, cartesianY, cartesianZ)