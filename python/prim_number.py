def prime_num(n):
    for i in range (2, n):
        if n % i == 0:
            return False
        else:
            return True

n = int(input("Enter the number:"))

if n > 0:
    print(prime_num(n))
else: 
    print("Enter the valid number !")