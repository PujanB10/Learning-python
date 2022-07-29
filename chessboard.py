def chessboard(length):
    i,j,k=1,1,1
    a,b="0","1"
    t1,t2="",""
    while i<=length:
        if i%2!=0:
            t1+=b
            t2+=a
        else:
            t1+=a
            t2+=b
        i+=1
                   
    while k<=length:
        print(t1)
        if length-k==0:
            break
        print(t2)
        k+=2

        chessboard(3)
