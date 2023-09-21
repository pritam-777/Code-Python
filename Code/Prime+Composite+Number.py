def CheckPrimeComposite(n):
    if n>1:
        for i in range(2, n):

            if (n % i == 0):
                print("This is composite number")
                break
        else:
            print("Prime Number")







if __name__ == "__main__":
    CheckPrimeComposite(11)

