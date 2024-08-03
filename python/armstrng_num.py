def armstrong_num(num):
    count = len(str(num))
    temp = num
    sum = 0
    for i in range (0,count):
        last_digit = temp%10
        last_digit_power = pow(last_digit,count)
        temp = temp//10
        sum = sum + last_digit_power
    return sum

num = int(input("Enter the number:"))
Total = armstrong_num(num)
if (num == Total):
    print(f"{ num } is amstrong number")
else:
    print(f"{ num } is not amstrong number")