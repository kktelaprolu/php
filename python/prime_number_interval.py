def prime_interval(first,second):
    for i in range(first,second):
        for j in range(2,i):
            if i%j == 0:
                print(i,"is not primenumber")
                break
        else:
            print(i,"is prime number")

first_number=int(input("Enter the first number in interval:"))
second_number=int(input("Enter the second number in interval:"))

if (first_number>1 and second_number>2) and first_number<second_number:
    prime_interval(first_number,second_number)
else:
    print("Entered Interval is not Valid!")