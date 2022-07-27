word=input("Please type in a string:")
char=input("Please type in a substring:")
length=len(char)
total=len(char)
i=1
while i<=2:
    index=word.find(char)
    total+=index
    word=word[index+length:]
    i+=1
    if index==-1:
        total=0
if total==0:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {total}.")
        
