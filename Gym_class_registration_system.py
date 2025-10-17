print("=== Gym Class Registration System ===")
total=0
while True:
    level=input("Please enter your class level: beginner, intermediate or advanced: ")
    if level == "done":
        break
    if level=="beginner":
        price=12.00
    elif level=="intermediate":
        price=15.00
    elif level=="advanced":
        price=18.00
    else:
        print("Invalid class level")
    total+=price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")
discount=0.0
if total>=60.00:
    discount=10.00
final_total=total-discount
print("\n=== Registration Summary ===")
print(f"Subtoal: ${total:.2f}")
print(f"Multi-Class Discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for registering")