def add(my_dict):
    name=input("name:")
    number=input("number:")
    if name not in my_dict:
        my_dict[name]=[]
    my_dict[name].append(number)
    print("ok!")
    return my_dict


def show(my_dict):
    name=input("name:")
    if name in my_dict:
        for numbers in my_dict[name]:
            print(numbers)
    else:
        print("no number")        
    


my_dict={}
while True:
    command=int(input("command (1 search, 2 add, 3 quit):"))
    if command==2:
        add(my_dict)
    if command==1:
        show(my_dict)
    if command==3:
        break
print("quitting...")
