def ChekVowel(string):
    vowels=('a','e','i','o','u')
    for i in string.lower():
        if i in vowels:
            string=string.replace(i,"")
    print(string)



if __name__=="__main__":
    string="Complete exit from lockdown not possible, Modi tells CMs";
    ChekVowel(string)