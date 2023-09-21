Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def swap_case(s):
    str= ""
    for i in(s):
        if(i.isupper()):
            str+=(i.lower())
        else:
            str+=(i.upper())
    return str


    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
