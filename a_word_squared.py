
def squared(word,num):
    i=0
    start=0
    while i<num:
        out=""
        while len(out)<num:
            if start==len(word):
                start=0
            out+=word[start]
            start+=1
        print(out)
        i+=1
squared("aybabtu", 5)
