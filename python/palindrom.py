def reverse_num(n):
    rev=0
    while n!=0:
        rev = (rev *10) + (n%10)
        n = n//10
    return rev

num = int(input("Enter the number:"))
rev=reverse_num(num)

if rev==num:
    print(f"{num} is palindrom number")
else:
    print(f"{num} is not palindrom number")