def fact(n):
    fact=1
    while n !=0:
        fact=fact*n
        n=n-1
    return fact

num = int(input("Enter the number:"))
print(f"factorial of {num} is {fact(num)}")