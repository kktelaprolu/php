def str_length(my_str):
    len_count = 0
    for i in my_str:
        len_count = len_count + 1
    return len_count

def reverse_string(my_str):
    reverse_string = ""
    for i in my_str:
        #print(i)
        reverse_string = i +reverse_string
    return reverse_string

my_str = "Hey, How are you?"

str_length = str_length(my_str)
print("lengthe of string:", str_length)

print(reverse_string(my_str))