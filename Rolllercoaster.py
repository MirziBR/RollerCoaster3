print("Welcome to the Rollercoaster! ")
height = float(input("What is your height big fella? "))
bill = 0

if height >= 120:
    print("You`re good, you can ride into the rollercoaster! ")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age < 18:
        bill = 7
        print("Sorry, you have to pay $7.")
    elif age == 18:
        bill = 12
        print("Youre 18 now, please pay $12.")
    else:
        print("Please, pay $12.")
        bill = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Photos are $3, so your final bill is ${bill}")
else:
    print("You need to grow up a little bit to go, I`m sorry! ")
