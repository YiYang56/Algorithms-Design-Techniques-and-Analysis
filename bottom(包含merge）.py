def merge(A,p,q,r):
    B=[]
    if p!=0:
        for i in range(p):
            B.append(A[i])
    s=p
    t=q+1
    k=p
    while s<=q and t<=r:
        if A[s]<=A[t]:
            B.append(A[s])
            s+=1
        else:
            B.append(A[t])
            t+=1
        k+=1
    if s==q+1:
        for i in range(t,r+1):
            B.append(A[i])
            i+=1
            k+=1
    else:
        for i in range(s,q+1):
            B.append(A[i])
            i+=1
            k+=1
    for i in range(p,r+1):
        A[i]=B[i]

def bottom(A):
    t=1
    n=len(A)
    while t<n:
        s=t
        t=2*s
        i=0
        while i+t<=n:
            merge(A,i,i+s-1,i+t-1)
            i=i+t
        if i+s<n:
            merge(A,i,i+s-1,n-1)

str = input('以空格为间隔连续输入一个待排序数组:')
A=[int(n) for n in str.split()]
bottom(A)
print(A)