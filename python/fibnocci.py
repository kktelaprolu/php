# 0 1 1 2 3 5 8 13

index = int(input("Enter the index till wher the sib series need to print:"))

firstnumber=0
secondnumber=1
temp=0
print(firstnumber)
print(secondnumber)

for i in range (0,index):
   temp = firstnumber + secondnumber
   firstnumber = secondnumber
   secondnumber = temp
   print(temp)