def char_count(char):
    count = 0
    for i in str:
        if i == char:
            count = count+1
    return count

str = input("Enter the string:")
char = input("Enter the char to be counted in string:")

print(char_count(char))