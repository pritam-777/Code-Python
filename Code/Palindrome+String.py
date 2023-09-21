def isPalindrome(str):
    for i in range(0,int(len(str)/2)):

        if str[i]!=str[len(str)-i-1]:
            return False
    return True





if __name__=='__main__':
    str = "Pritam"
    ans = isPalindrome(str)
    if(ans):
        print("Yes")
    else:
        print("No")