print("--- Movie Ticket Pricer ---")
age=int(input("Please enter your age: "))
if age < 13:
    print("You fall into the 'Children' category.")
    print("Your ticket price is: $8")
elif age >64:
    print("You fall into the 'Senior' category.")
    print("Your ticket price is: $10")
else:
    print("You fall into the 'Adult' category.")
    print("Your ticket price is: $15")