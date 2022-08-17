

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    check=input("Function: ")
    if check=="3":
        print("Bye!")
        break
    if check=="2":
        search=input("Search term: ")
        with open("dictionary.txt") as reading_file:
            for lines in reading_file:
                lines=lines.strip()
                lines=lines.split("-")
                if search in lines[0] or search in lines[1]:
                    print(f"{lines[0]} - {lines[1]}")
    if check=="1":
        finnish=input("The word in Finnish: ")
        english=input("The word in English: ")
        print("Dictionary entry added")
        with  open("dictionary.txt","a") as writing_file:
            writing_file.write(f"{finnish}-{english} \n")
    


