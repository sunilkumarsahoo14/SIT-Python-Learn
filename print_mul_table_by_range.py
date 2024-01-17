# Multiplication table (from 1 to 10) in Python

num = int(input("Enter The Number: "))
ran = int(input("Enter Range: "))

for i in range(1, ran+1):
   print(num, 'x', i, '=', num*i)
