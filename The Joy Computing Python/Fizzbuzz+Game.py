def Fizzbuzz(n):
    for i in range(1,n):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        else:
            if(i%3==0):
                print("Fizz")
            else:
                if(i%5==0):
                    print("Buzz")
        print(i)


if __name__ == "__main__":
    Fizzbuzz(15)

