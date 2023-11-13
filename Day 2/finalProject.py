print("welcome to the tip calculator")

bill = float(input("what was the total bill? "))
percentage = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
total = round(((percentage/100) * bill + bill) / split, 2)

print(f"Each person should pay: ${total}")