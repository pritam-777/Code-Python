N=int(input())
A=[int(i)for i in input().split()]
B=[]
rev=A.reverse()
for i in range(len(A)):
    B.append(A[i]+rev[i])
for i in range(len(B)):
    print(B[i])
