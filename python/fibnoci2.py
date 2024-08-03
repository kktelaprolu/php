# 0 1 1 2 3 5 8 13

def fib(i):
    if i==0:
       return i
    if i==1:
        return i
    else:
      return fib(i-2) + fib(i-1)



index=int(input("Enter the index till you want to print fib:"))
if index<0:
   print("please enter positive number")
else:
   for i in range (0,index):
        print(fib(i))