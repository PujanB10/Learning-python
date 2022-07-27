
while True:
    fact=1
    number=int(input("Please type in a number:"))
    i=number
    if number<=0:
        fact="inv"
        break
    while i>0:
        fact*=i
        i-=1
    print(f"The factorial of the number {number} is {fact}")
if fact=="inv":
    print("Thanks and bye!")

    

     
    
