def perfect_number(n):
    sum =0
    for i in range(1, (n//2)+1):
        rem= n%i
        if rem==0:
            sum = sum+i
    return sum


num = int(input("Enter the number:"))
sum = perfect_number(num)
if num ==sum:
    print(f" {num} is perfect number")
else:
    print(f" {num} is not a perfect number")