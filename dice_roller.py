from random import choice

def roll(die: str):
    if die=="A":
        return choice([3, 3, 3, 3, 3, 6])
    if die=="B":
        return choice([2, 2, 2, 5, 5, 5])
    if die=="C":
        return choice([1, 4, 4, 4, 4, 4])

def play(die1: str, die2: str, times: int):
    win_A, win_B, draw = 0,0,0
    for i in range(times):
        value_A=roll(die1)
        value_B=roll(die2)
    
        if value_A > value_B:
            win_A+=1
        elif value_B > value_A:
            win_B += 1
        else:
            draw+=1
    
    return(win_A,win_B,draw)




if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    
    print()

    result = play("A", "C", 10)
    print(result)
    result = play("B", "B", 10)
    print(result)
