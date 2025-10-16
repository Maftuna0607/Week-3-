print("--- Running Total Calculator ---")
total=0
while True:
    user_input=input("Enter numbers to add them up or type 'done' to see the total result. ")
    if user_input == "done":
        break
    total+= float(user_input)
    print(total)
print(f"the final total is: {total}")