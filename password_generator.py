import string
import random

def generate_strong_password(length: int, is_numbers: bool, is_special : bool):
    db_check=string.ascii_lowercase
    db=string.ascii_lowercase
    special="!?=+-()#"
    numbers=""

    #generating a database of numbers to choose from
    for i in range(10):
        numbers+=str(i)

    #adding the numbers to the password database if required
    if is_numbers:
        db+=str(numbers)

     #adding symbols to the password database if required   
    if is_special:
        db+=special
    

    while True:

        #creating a random password
        result=""
        for i in range(length):
            result+=random.choice(db)
        check_num=0
        check_sym=0
        check_low=0

        #checking if the password contains numbers,symbols and lowercase characters
        for elements in result:
            if elements in db_check:
                check_low=1
            if elements in numbers:
                check_num=1
            if elements in special:
                check_sym=1
        if is_numbers and check_num==0:
            continue
        if is_special and check_sym==0:
            continue
        if check_low==0:
            continue
        return result


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
