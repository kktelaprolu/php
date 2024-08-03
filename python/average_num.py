def Avg_nums():
    sum = 0
    for i in my_list:
       sum = sum+i
    Avg = sum/total_numbers
    return Avg


def collect_numbers(total_numbers):
    print("enter numbers:")
    for i in range (0, total_numbers):
        ele=float(input())
        my_list.append(ele)
        
my_list=[]
total_numbers = int(input("Enter total numbers:"))
collect_numbers(total_numbers)
Average = Avg_nums()
print("Average:", Average)
