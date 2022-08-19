def filter_incorrect():
    with open("lottery_numbers.csv") as reading_file, open("correct_numbers.csv","w") as writing_file:
            for lines in reading_file:
                try:
                    new_num=[]
                    not_repeat=True
                    new_line=lines.split(";")
                    week=new_line[0].strip().split(" ")
                    numbers=new_line[1].strip().split(",")
                    for i in range(len(numbers)):
                        new_num.append(int(numbers[i]))
                        if numbers.count(numbers[i])>1:
                            not_repeat=False
                    if int(week[1])>0 and len(new_num)==7 and max(new_num)<=39 and min(new_num)>=1 and not_repeat:
                        writing_file.write(lines)
                except:
                    continue
            

if __name__ == "__main__":
    filter_incorrect()
