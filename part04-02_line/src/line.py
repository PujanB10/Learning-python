# Write your solution here
# You can test your function by calling it within the following block
def line(number,letter):
    if letter=="":
        print("*"*number)
    else:
        print(letter[0]*number)



if __name__ == "__main__":
    line(5, "x")