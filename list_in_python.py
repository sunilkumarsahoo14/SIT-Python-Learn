# ---------- Lists In Python -----------

marks = [2,3, "Sunil",True,4,5,8,"Lipsu",12,"Payal",20]
# print(marks)
# print(marks[0])
# print(marks[3])

# print(marks[-3]) # It Means: ( Length Of Marks -3 )

#------ List With "in" Keywords
# if "Sunil" in marks:
#     print("Yes")

# if "3" in marks:
#     print("Yes")  # Because Here 3 Stored As An Integer
# else:
#     print("No")

# ----------Jump Index-----
# print(marks[1:8:2])

#------List Comprehension--------

# lst = [i for i in range(4)]
# print(lst)

lst = [i for i in range(10) if i%2 == 0]
print(lst)




