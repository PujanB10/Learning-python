def pattern(num,char,rem):
    print((num*" ")+(rem*"*"))


def spruce(num):
    init=num-1
    i=1
    j=1
    print("a spruce!")
    while i<=num:
        pattern(init,"*",j)
        i+=1
        init-=1
        j+=2
    num-=1
    print((num*" ")+"*")

if __name__ == "__main__":
    spruce(5)