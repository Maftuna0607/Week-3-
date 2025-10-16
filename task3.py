print("--- Triangle Pattern Printer ---")
h=int(input("Enter the desired height of the triangle: "))
for i in range(1, h+1):
    for j in range(i):
        print("*", end=" ")
    print()