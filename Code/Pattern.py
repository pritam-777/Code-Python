def pattern(limit):
    for i in range(1,limit+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" ")

if __name__=="__main__":
    pattern(10)
