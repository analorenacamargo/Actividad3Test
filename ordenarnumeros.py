##crea un algoritmo que ordene 5 numeros de menor a mayor 

# Ask the user to input five numbers
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Sort the numbers in ascending order
sorted_numbers = sorted(numbers)

# Display the numbers in ascending order
print("Numbers in ascending order:")
print(sorted_numbers)

