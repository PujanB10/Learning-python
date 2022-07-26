a=input("Please type in a word:")
b=input("Please type in a character:")
while True:
    length=len(a)
    index=a.find(b)
    if index==-1 or (length-index)<3:
        break
    print(a[index:index+3])
    a=a[index+1:]
        
        
