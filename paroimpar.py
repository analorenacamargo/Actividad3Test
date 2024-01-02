#crea un algoritmo que te diga si un numero es par o impar

# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")