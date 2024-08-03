def my_decorator(func):
    def wrapper(a,b):
        print("something is happining before function is called")
        func(a,b)
        print("something is happend after excutin of function")
    return wrapper

@my_decorator
def sum(a,b):
    sum = a+b
    print(sum)

num1 = int(input("enter value of num1:"))
num2 = int(input("Enter the value of num2:"))

sum(num1,num2)