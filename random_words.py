import random
def words(n: int, beginning: str):
    result=[]
    final=[]
    with open("words.txt") as reading_file:
        for lines in reading_file:
            lines=lines.strip()
            if lines.startswith(beginning):
                if lines.strip() not in result:
                    result.append(lines)
        if len(result)<n:
            raise ValueError

    return random.sample(result,n)


    

if __name__ == "__main__":
    word_list = words(5, 'car')
    for word in word_list:
        print(word)
