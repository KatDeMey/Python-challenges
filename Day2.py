print("Welcome to the tip calculator!")
bill = float(input("What was the total of your bill? $"))
tip = int(input("How much % would you like to tip? 10, 12, or 15? "))
people = int(input("how many people would you like to split the bill with? "))

tip_amount = bill * (tip / 100)
full_bill = bill + tip_amount
total_per_person = full_bill / people
final_total = round(total_per_person, 2)


print(f"Each person should pay: ${final_total}")
