def str_length(my_str):
    len_count = 0
    for i in my_str:
        len_count = len_count + 1
    return len_count


my_str = "Hey, How are you?"

str_length = str_length(my_str)
print("lengthe of string:", str_length)
