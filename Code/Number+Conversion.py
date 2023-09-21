def D2B(n):
    dec = int(n)
    print(n,"in Binary :",bin(dec))
def D2O(n):
    dec = int(n)
    print(n,"in Octal :",oct(dec))
def D2H(n):
    dec= int(n)
    print(n,"in Hexadecimal :",hex(dec))

if __name__ =='__main__':
    decimalNumber = 105
    D2B(decimalNumber)
    D2O(decimalNumber)
    D2H(decimalNumber)