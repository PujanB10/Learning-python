# Copy here code of line function from previous exercise
def line(num,cha):
    print(num*cha)

def box_of_hashes(height):
    i=0
    # You should call function line here with proper parameters
    while i<height:
        line(10, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
