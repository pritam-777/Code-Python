def gcd(a,b):
    if(a==b):
        return a
    if(a<b):
        return gcd(a,b-a)
    return gcd(a-b,b)
def lcm(a,b):
    return (a*b)/gcd(a,b)




if __name__=='__main__':
    a=15
    b=25
    print(lcm(a,b))
    print(gcd(a,b))