#  ---------- Break ----------

# for i in range(12):
#     if(i ==  10):
#         break
#     print("5 X", i+1, "=", 5 * (i + 1))

    # ----------- Skip(Continue) ------------

# for i in range(12):
#     if(i == 7):
#         print("Skip The Iteration")
#         continue
#     print("5 X", i, "=", 5 * (i))

# Emulate do while loops--------

i = 0
while True:
    print(i+1)
    i = i + 1
    if(i%100 == 0):
        break
