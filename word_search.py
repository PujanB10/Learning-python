def find_words(search_term: str):
    result=[]
    with open("words.txt") as new_file:
        check=search_term.replace("*","")
        for lines in new_file:
            lines=lines.strip()
            if "*" in search_term:
                if search_term[0]=="*":
                    if lines.endswith(check):
                        result.append(lines)
                else:
                    if lines.startswith(check):
                        result.append(lines)

            elif "." in search_term:
                if len(search_term)==len(lines):
                    check=True
                    for i in range(len(search_term)):
                        if search_term[i]!="." and lines[i]!=search_term[i]:
                            check=False
                            break
                    if check:
                        result.append(lines)

            else:
                if lines==search_term:
                    result.append(lines)
    return result
                    


if __name__ == "__main__":
    print(find_words("*vokes"))
    print(find_words("ca."))
