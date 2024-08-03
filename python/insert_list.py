my_list = [5,9,10]
print(my_list)
my_list.append(5)
print(my_list)
my_list.extend([6,7])
print(my_list)

print("---------------------------")

list=[1,2,3]
number=int(input("Enter a number"))
index = int(input("Enter index"))

if index > len(list):
    print("index out of range")
else:
    list.insert(index,number)
    print(list)