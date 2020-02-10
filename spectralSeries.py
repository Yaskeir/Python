#Mateusz Fido
#Hydrogen Spectral Series Calculator

def spectralSeries(n1, n2, Z):
    """Calculates the spectral series for hydrogen-like atoms, 
    printing the required number of wavelengths to the console."""

    if not n2 > n1:
        print("Incorrect arguments provided.")
        return None
    else:
        while(n2 > n1):
            rydbergConstant = 0.0109737 #in nm
            wavelength = round(1/(Z**2*rydbergConstant*(1/(n1**2)-1/(n2**2))))
            return wavelength


def printSeries(n1Max, wavelengthCount, Z):
    """Prints the result of spectral series calculation.
    Accepts three arguments:
    the maximum possible value for n1, the number of wavelengths to be printed
    and the atomic number. """
    
    if n1Max < 1:
        print("n1 cannot be less than 1.")
        n1Max = 1
    n1 = 1 #set initial values for n1 and n2 
    n2 = 2
    for i in range(n1Max):
        print("Spectral lines for n1 =", n1, ":")
        for j in range(wavelengthCount):
            print("n2 =", n2, "| Wavelength =", spectralSeries(n1, n2, Z), "nm")
            n2 += 1
        n1 += 1 #increment after every iteration
        n2 = n1 + 1 #reset after every iteration

print("Welcome to the Spectral Series calculator for hydrogen-like atoms!")
n1Max = int(input("Please provide the maximal value for the n1 parameter: "))
wavelengthCount = int(input("Please specify how many wavelengths you want to print out: "))
Z = int(input("Please specify the atomic number for your hydrogen-like atom: "))
printSeries(n1Max, wavelengthCount, Z)