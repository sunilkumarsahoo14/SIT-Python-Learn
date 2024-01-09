# Conditionals In Python Language
# ---------------------------------

# if ...else

# a = int (input("Enter Your Age: "))
# print("Your Age Is: ", a)
# if(a > 18):
#     print("You Can Drive.")
# else:
#     print("You Can't Drive!")

# ------------------------

# if ...elif...else  Statement In Python Language (Note The Colon[:] Symbol in every conditions)

# num = int (input("Enter Number: "))

# if(num > 0):
#     print("+ve")
# elif(num == 0):
#     print("0")
# else:
#     print("-ve")

# ----------------------------

# nested if else statements in python...

num = int (input("Enter Number: "))

if(num < 0):
    print("Negative Number!")
elif(num > 0):
    if(num <= 10):
        print("Number Is Between 1-10")
    elif(num > 10 and num <= 50):
        print("Number Is Between 11-50")
    else:
        print("Number Is Greater Than 50!")
else:
    print("Number Is Zero!")