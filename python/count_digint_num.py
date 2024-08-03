def count_digit(num):
    count = 0
    while num > 0:
        num= num // 10
        count = count + 1
    return count
        
num = int(input("Enter the number:"))
print(f"count of digits in {num} is { count_digit(num) }")