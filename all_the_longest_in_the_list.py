def all_the_longest(list):
    longest=len(list[0])
    new_list=[]
    for i in list:
        if len(i)==longest:
            new_list.append(i)
        elif len(i)>longest:
            longest=len(i)
            new_list.clear()
            new_list.append(i)
            
    return new_list


if __name__ == "__main__":
    my_list=["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(all_the_longest(my_list))
