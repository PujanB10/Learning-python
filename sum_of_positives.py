def sum_of_positives(list):
    total=0
    for i in list:
        if i>0:
            total+=i
    return total
if __name__ == "__main__":
    list=[1,-2,3,-4,5]
    print(f"The result is {sum_of_positives(list)}")
