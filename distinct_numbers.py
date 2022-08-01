def distinct_numbers(list):
    list=sorted(list)
    numbers=[]
    for num in list:
        if num not in numbers:
            numbers.append(num)
    return numbers

        


if __name__ == "__main__":
    my_list=[1,2,3,1,2,3]
    print(distinct_numbers(my_list))
