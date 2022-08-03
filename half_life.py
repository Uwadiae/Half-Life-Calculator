import matplotlib.pyplot as plt
import numpy as np

# State the purpose of the program
print("This program calculates the mass of a radioactive substance after a certain time.")

# Ask the user to input the initial mass and half life of the radioactive substance and the time passed
initial_mass = float(input("Please enter the original mass of the substance in grams: "))
half_life = float(input("Please enter the half life of the substance in years: "))
time_passed = float(input("Please enter the time passed in years: "))

# Calculate the new mass of the substance
new_mass = initial_mass * (0.5) **(time_passed / half_life)

# Show the new mass to the user
print("The new mass is " + str(new_mass) + "g")

# Define a function for the new mass of the substance
def f(x,m,h):
    return m * (0.5) **(x / h)

# Make an xlist of values
xlist = np.linspace(0, time_passed, num=1000)

# Make a ylist of values
ylist = f(xlist,initial_mass,half_life)

# make a figure with good resolution
plt.figure(num=0,dpi=120)

# Plot the x and y values
plt.plot(xlist,ylist)

# Label the graph and show it
plt.title("Radioactive Decay Graph")
plt.ylabel("mass/g")
plt.xlabel("years")
plt.show()
