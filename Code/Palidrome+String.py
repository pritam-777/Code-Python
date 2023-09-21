def isPalidrome(string):
    for i in range(int(len(string)/2)):
        if string[i]!=string[len(string)-i-1]:
            return False
    return True




if __name__=="__main__":

    s="wow"
    ans=isPalidrome(s)
    if (ans):
        print("Yes")
    else:
        print("No")
