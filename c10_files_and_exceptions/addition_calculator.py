print("Give me two number and I'll add them together.")
print("Enter 'q' if you want quit.")

while True:
    try:
        first = input("\nFirst namber: ")
        if first == "q":
            break
        first = float(first)

        second = input("\nSecond number: ")
        if second == "q":
            break
        second = float(second)

    except ValueError:
        print("\nPlease enter numbers!\n")
    else:
        print(f"The sum of {first} and {second} is {first+second}.")
