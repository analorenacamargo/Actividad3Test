#crea un algoritmo que calcule los dias que faltan para dia de muertos y navidad

from datetime import datetime

# Get today's date
today = datetime.now().date()

# Day of the Dead (November 2nd)
day_of_the_dead = datetime(today.year, 11, 2).date()

# Christmas (December 25th)
christmas = datetime(today.year, 12, 25).date()

# Calculate days left for each event
days_until_day_of_the_dead = (day_of_the_dead - today).days
days_until_christmas = (christmas - today).days

# Display the number of days left for each event
print(f"Days left until Day of the Dead: {days_until_day_of_the_dead} days")
print(f"Days left until Christmas: {days_until_christmas} days")