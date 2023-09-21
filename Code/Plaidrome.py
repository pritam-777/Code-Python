def isPalidrome(n):
    p=n
    sum=0
    while(n!=0):
        r=n%10
        sum=sum*10+r
        n//=10

    if(p==sum):

        print("yes")
    else:
        print("No")
if __name__=='__main__':

    n= 121
    isPalidrome(n)