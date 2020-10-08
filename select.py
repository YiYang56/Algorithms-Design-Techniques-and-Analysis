import math as m

def select(A,low,high,k):
    p=high-low+1
    if p<44:
        A=sorted(A)
        return A[k-1]
    else:
        q=m.floor(p/5)
        mid=[]
        for i in range(q):
            temp = []
            for j in range(5):
                temp.append(A[5*i+j])
            sorted(temp)
            mid.append(temp[2])
        mm=select(mid,0,q-1,m.floor((q-1)/2))
        A1,A2,A3=[],[],[]
        for i in range(low,high+1):
            if A[i]<mm:
                A1.append(A[i])
            elif A[i]==mm:
                A2.append(A[i])
            else:
                A3.append(A[i])
        if len(A1)>=k:
            return select(A1,0,len(A1)-1,k)
        elif len(A1)+len(A2)>=k:
            return mm
        else:
            return select(A3,0,len(A3)-1,k-len(A1)-len(A2))

k = eval(input('请输入需要寻找第几个元素k：'))
str = input('请输入一组需要寻找第k小元素的数，用逗号分隔：')
A=[int(i) for i in str.split(',')]
res=select(A,0,len(A)-1,k)
print(res)