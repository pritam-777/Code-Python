with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("Hello i am pritam")
myfile.close()