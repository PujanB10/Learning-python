def invert(dic):
    dic1={}
    for element in dic:
        dic1[element]=dic[element]
    for element in dic1:
        dic[dic1[element]]=element
        dic.pop(element)


        

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
