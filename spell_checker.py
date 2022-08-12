sentence=input("Write text:")
text=sentence.split(" ")
result=""

check=[]
with open("wordlist.txt") as new_file:
    for words in new_file:
        words=words.replace("\n","")
        check.append(words)
for items in text:
    if items.lower() in check:
        result=result+items+" "
    else:
        result=f"{result}*{items}* "


print(result)
