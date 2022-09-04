import difflib
sentence=input("Write text:")
text=sentence.split(" ")
result=""

check=[]
with open("wordlist.txt") as new_file:
    for words in new_file:
        check.append(words.strip())
wrong = {}


for items in text:
    if items.lower() in check:
        result=result+items+" "
    else:
        wrong[items] = []
        result=f"{result}*{items}* "

print(result)
print("suggestions:")
for items in wrong:
    wrong[items]=(difflib.get_close_matches(items, check))
    print(f"{items}: {', '.join(wrong[items])} ")
