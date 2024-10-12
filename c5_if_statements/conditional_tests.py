car = "bmw"
print("Is car == 'bmw' ? I predict True.")
print(car == "bmw")

print("\nIs car == 'benz' ? I predict False.")
print(car == "benz")
#
my_desk = ["watch", "phone", "pencilcase", "phone charger"]
print("\nIs my first thing in my desk a watch? I predict True!")
print(my_desk[0] == "watch")

print("\nIs my first thing in my desk a wallet? I predict False.")
print(my_desk[0] == "wallet")
#
myname = "Saman"
print("\nIs myname == 'saman'? I perdict True.")
print(myname.lower() == "saman")

print("\nIs myname == 'saman'? I predict True!")
print(myname == "saman")
#
friends = "no"
print("\nDo I have any friends == 'yes'? I predict True.")
print(friends == "yes")

print("\nDo I have any friends == 'no' ? I predict False.")
print(friends == "no")
#
my_favorite = "mathematics"
print("\nIs my_favorite == 'art' ? I predict False.")
print(my_favorite == "art")

print("\nIs my_favorite == 'mathematics' ? I predict True.")
print(my_favorite == "mathematics")
#
myage = 19
print("\nIs myage >= 19 ? I predict True.")
print(myage >= 19)

print("\nIs myage < 19 ? I predict False.")
print(myage < 19)
print("\n\n")
# more conditional tests

myfavfood = "pizza"
print(myfavfood == "sandwich")
print(myfavfood == "pizza")

my_name = "SAMAN"
print(f"\t{my_name.lower () == 'saman'}")

my_age = 19
myfri_age = 23
print(myage == 19)
print(my_age == 19)
print(myfri_age > 19)
print(myfri_age <= 19)
print()

print((my_age == 19) and (myfri_age == 22))
print((my_age == 19) or (myfri_age == 22))
print(my_age > 18 and my_age < 20)
print((my_name.lower() == "saman") or (friends == "yes"))
print(
    (car == "ford") and (myfavfood == "pizza") or (myage == 19) and (friends == "yes")
)
print()

countries = [
    "America",
    "China",
    "Russia",
    "Germany",
    "England",
    "Japan",
    "Canada",
    "France",
    "spain",
]
print("China" in countries)
if "Germany" in countries:
    print("exist")
my_country = "Iran"
if my_country.lower() in countries:
    print("Your country exist.")
else:
    print("Your country not exist.")
if "Iran" not in countries:
    print("False!")
if "America" not in countries:
    print("False!")
else:
    print("True!")
