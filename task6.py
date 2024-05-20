import random
with open("aziz.txt","r") as file:
    my_list=file.readlines()
    res=random.choice(my_list)
    print(res)