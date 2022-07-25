# State the purpose of the program
print("This program calculates the mass of a radioactive substance after a certain time.")

# Ask the user to input the initial mass and half life of the radioactive substance and the time passed
initial_mass = float(input("Please enter the original mass of the substance in kilograms: "))
half_life = float(input("Please enter the half life of the substance in years: "))
time_passed = float(input("Please enter the time passed in years: "))

# Calculate the new mass of the substance
new_mass = initial_mass * (0.5) **(time_passed / half_life)

# Show the new mass to the user
print("The new mass is " + str(new_mass) + "Kg")
