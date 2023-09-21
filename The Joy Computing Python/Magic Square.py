def MagicSquare(n):
    magicSquare = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)


    p=n//2
    q=n-1
    num = n*n
    count=1
    while(count<=num):
        if(p==-1 and q ==n):
            p=0
            q=n-2
        else:
            if (q==n):
                q=0
            if(p<0):
                p=n-1
        if(magicSquare[p][q]!=0):
            q=q-2
            p=p+1
            continue
        else:
            magicSquare[p][q]=count
            count+=1
        p=p-1
        q=q+1


    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()



if __name__=="__main__":
    n=5
    MagicSquare(n)