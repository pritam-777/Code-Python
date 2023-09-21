def merge_the_tools(string, k):
    subsegment=int(len(string)/k)
    for i in range(subsegment):
        t = string[i*k:(i+1)*k]
        u=""
        for j in t:
            if j not in u:
                u+=j
        print(u)

    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)