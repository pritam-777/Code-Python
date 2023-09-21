def minion_game(string):
    ln = len(string)
    p1=0
    p2=0
    for i in range(ln):
        if string[i] in "AEIOU":
            p1 += ln-i
        else:
            p2 +=ln-i
    if p1 > p2:

        print("Kevin", p1)
    elif p1 < p2:
        print("Stuart", p2)
    else:
        print("Draw")
        # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)