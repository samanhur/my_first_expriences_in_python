#numbers = list(range(1,10))
#print(numbers)
numbers = [2, 7, 8, 9, 3, 1, 4, 5, 6]
numbers.sort()
for number in numbers :
    if number == 1 :
        print(f"{number}st")
    elif number == 2 :
        print(f"{number}nd")
    elif number == 3 :
        print(f"{number}rd")
    else:
        print(f"{number}th")