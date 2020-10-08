import math

def candidate(m,A):
    j,c,count=m,A[m],1
    while j<len(A)-1 and count>0:
        j+=1
        if A[j]==c:
            count+=1
        else:
            count-=1
    if j==len(A)-1:
        return c
    else:
        return candidate(j+1,A)

str = input('以逗号为间隔输入一组数:')
A=[int(n) for n in str.split(',')]
c=candidate(0,A)
count=0
for j in range(len(A)):
    if A[j]==c:
        count+=1
if count>math.floor(len(A)/2):
    print('the majority element is：{}'.format(c))
else:
    print('no majority element')