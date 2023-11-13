#Years left calculator
age = int(input("Enter your current age: "))

years_left = 90 - age
months = years_left * 12
weeks = years_left * 52
days = years_left * 365
print(f"You have {months} months, {weeks} weeks and {days} days left.")