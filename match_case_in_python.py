# ----------match Case In Python--------

x = int(input("Enter The Value Of x: "))
match x:
    case 0:
        print("x = 0")
    case 2:
        print("x = 2")
    case 9:
        print("x = 9")
    case 11:
        print("x = 11")
    case 6:
        print("x = 6")

        #  Default with if statements...
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _ if x!=70:
        print(x, "is not 70")

