def reverse_num(n):
    rev=0
    while n != 0:
        rev = (rev*10) + (n%10)
        n=n//10
    return rev

number = int(input("Enter the Number to be reversed:"))

print(f"reverse of the number is {reverse_num(number)}")