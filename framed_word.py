a=input("Word:")
length=len(a)
space=int((28-length)/2)
print(30*"*")
if length%2==0:
    print("*"+space*" "+a+space*" "+"*")
else:
    print("*"+space*" "+a+(space+1)*" "+"*")
print(30*"*")
