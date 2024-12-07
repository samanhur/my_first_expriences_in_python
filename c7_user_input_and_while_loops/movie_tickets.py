message = "Hello, welcome to our theater. Please enter your age: "
message += "Enter 'q' when you are finished: "

while True:
    age = input(message)
    if age == "q":
        break
    age = int(age)

    if age < 3 :
        price = 0
    elif age >= 3 and age < 12 :
        price = 10
    else :
        price = 15

    print(f"Your ticket cost is: {price}$ !")