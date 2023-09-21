def Multiple(a):
    b=[]
    for i in a:
        if(i%5!=0):
            b.append(i)
    for i in range(len(b)):
        print(b[i],end=" ")



if __name__ =="__main__":
    a=[int(x) for x in input().split()]
    Multiple(a)