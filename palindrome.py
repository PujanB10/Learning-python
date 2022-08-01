def palindromes(word):
    check=""
    for i in range(-1,-len(word)-1,-1):
        check+=word[i]
    return word==check

while True:
    string=input("Please type in a palindrome:")
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

    
