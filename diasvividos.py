#tomando la fecha de nacimiento ingresada por la usuario calcalar el numero de dias que ha vivido. 

from datetime import datetime

# Ask the user to input their birthdate in yyyy-mm-dd format
birthdate_str = input("Enter your birthdate (yyyy-mm-dd): ")

# Convert the input string to a datetime object
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

# Get today's date
today = datetime.now().date()

# Calculate the difference between today's date and the birthdate
days_lived = (today - birthdate).days

# Display the number of days lived
print(f"You have lived for approximately {days_lived} days.")
