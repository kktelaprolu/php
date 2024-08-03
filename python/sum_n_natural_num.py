def sum_n_num(n):
    sum = n*(n+1)/2
    return sum

number=float(input("enter the value of n:"))

if number > 0:
   print(sum_n_num(number))
else:
    print("Enter valid Number")
    