def duplicate_num(list):
    for i in range(0,length):
        for j in range(i+1,length):
            if (list[i] == list[j]):
                 dup_list=print(list[j])
    return dup_list
   
                

list=[5,0,1,6,35,0,4,6,0,27]
length=len(list)
duplicate_num(list)
   