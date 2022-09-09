# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def triangle(num,char):
    print(num*char)

def rectangle(num,char):
    print(num*char)

def shape(num1,char1,num2,char2):
    i,j=0,0
    while i<=num1:
        triangle(i,char1)
        i+=1
    while j<num2:
        rectangle(num1,char2)
        j+=1


if __name__ == "__main__":
    shape(5, "x", 2, "o")