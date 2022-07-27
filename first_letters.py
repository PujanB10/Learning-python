sent=input("Please type in a sentence:")
i=0
print(sent[0])
while i<len(sent):
    dig=sent[i]
    if dig==" ":
        print(sent[i+1])
    i+=1
