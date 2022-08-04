def dict_of_numbers():
    check={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
    11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
    19:"nineteen",10:"ten"
    }
    whole_tens={20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    for i in range(2,10):
        for j in range(0,10):
            tens=i*10
            if j==0:
                check[tens]=whole_tens[tens]
            else:
                check[(i*10)+j]=f"{whole_tens[tens]}-{check[j]}"

    return check


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[25])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
    print(numbers[11])
