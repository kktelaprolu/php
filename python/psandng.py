
number = int(input("Enter the number:"))

def posng(number):
    if number<0:
        print(f"number { number } is Negative")
    if number>0:
        print(f"Number { number } is positive")
    else:
        print(f"number is zero")
posng(number)