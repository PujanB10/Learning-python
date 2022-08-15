

def filter_solutions():
    with open("solutions.csv") as source_file, open("correct.csv","w") as correct_file, open("incorrect.csv","w") as incorrect_file:
        for lines in source_file:
            original=lines
            lines=lines.split(";")
            exp=lines[1]
            result=lines[2]
            if "+" in exp:
                operands=exp.split("+")
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands=exp.split("-")
                correct = int(operands[0]) - int(operands[1]) == int(result)



            if correct:
                correct_file.write(original)
            else:
                incorrect_file.write(original)
            

            
if __name__ == "__main__":
    filter_solutions()
    filter_solutions()
    filter_solutions()
    filter_solutions()

