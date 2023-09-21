def Pattern(limit):
    for i in range(limit,0,-1):
        for j in range(0,i):
            print(j,end=" ")

        print("\r")




if __name__ == "__main__":
        Pattern(10)