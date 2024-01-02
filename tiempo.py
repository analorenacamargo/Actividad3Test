# usuario: velocidad y distancia, entrega tiempo

# Ask the user to input speed and distance
speed = float(input("Enter the speed (in mph or km/h): "))
distance = float(input("Enter the distance (in miles or kilometers): "))

# Calculate time using the formula time = distance / speed
time = distance / speed

# Display the calculated time
print(f"The time taken to cover {distance} units at a speed of {speed} units per hour is {time} hours.")

