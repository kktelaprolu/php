def num(n):
    result = ''   
    for i in range (1,n+1):
        result = result + str(i)
    return result

n = int(input("enter the value of n:"))
print(num(n))