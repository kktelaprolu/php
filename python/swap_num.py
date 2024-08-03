
def swap_num(num1,num2):
    if num1 < num2 :
        print("values of num1,num2 before swap", num1, num2)
        num2 = num2+num1
        num1 = num2-num1
        num2 = num2-num1
        print("vaules of num1,num2 after swap", num1, num2)
    else:
        print("values of num1,num2 before swap", num1, num2)
        num1=num2+num1
        num2=num1-num2
        num1=num1-num2
        print("values of num1, num2 after swap", num1, num2)
    return num1,num2

num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
swap_num(num1,num2)
