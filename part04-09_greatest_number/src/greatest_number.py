def greatest_number(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    return num3


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)