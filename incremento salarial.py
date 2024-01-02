#calcular el incremento salarial de una persona: si su salario es menor a 15mil el incremento será del 20%
#y si es mayor a 15 mil el incremento será del 15%

# Ask the user to input their current salary
current_salary = float(input("Enter your current salary: "))

# Check the salary and calculate the increase accordingly
if current_salary < 15000:
    increase_percentage = 0.20  # 20% increase
else:
    increase_percentage = 0.15  # 15% increase

# Calculate the increased salary
salary_increase = current_salary * increase_percentage
new_salary = current_salary + salary_increase

# Display the increased salary
print(f"Your new salary after the increase is: {new_salary}")