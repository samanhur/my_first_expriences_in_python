# again, who's better than myself ?
fav_num = {
    '1st': [19, 7, 14],
    '2nd': [17], 
    '3rd': [20, 21, 86],
    '4th': [23, 89], 
    '5th': [27, 16, 18, 20, 23],
    }
print(fav_num)
print("...")
for keys,values in fav_num.items() : 
    if len(values) == 1 :
        print(f"\n{keys}'s person favorite number is:")
        for value in values : 
            print(value)

    elif len(values) > 1 :
        print(f"\n{keys}'s person favorite number are:")
        for value in values : 
            print(value)
