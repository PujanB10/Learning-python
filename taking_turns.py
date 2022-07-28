number=int(input("Please type in a number:"))
i=1
while True:
    if number>1:
        print(i)
    print(number)
    i+=1
    number-=1
    if i-number==0:
        print(i)
        break
    if i>number:
        break
