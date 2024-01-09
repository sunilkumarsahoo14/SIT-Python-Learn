# ---------Functions In Python-----------

# Geometric Mean Finder Function
# def calcGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)

#---------------
# # Check Greater nuumber Function
# def checkGreater(a,b):
#     if(a>b):
#         print("First Number Is Greater!")
#     elif(a==b):
#         print("Numbers Are Equal!")
#     else:
#         print("Second Number Is Greater!")


#--------------------
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))

# calcGmean(a,b)
# checkGreater(a,b)

#----------------Functions With Parse Arguments----------

# def name(fname, lname = "Sahoo"):
#     print("Hello,", fname, lname)

# name("Sunil")

# Aruments Types:
# -----Default Arguments
#--------Keyword Arguments
#-------- Required Arguments
#----Variable Length Arguments

# -------------------------
# def average(*numbers):

#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average Is: ", sum/len(numbers))

# average(5,6,4,1,6,4)

# -------- Function With Return Type-----------
def average(*numbers):

    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

c = average(5,6,4)
print(c)




