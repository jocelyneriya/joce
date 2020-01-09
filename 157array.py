n=int(input())
l=list(map(int,input().split()))
sum=0
t=[]
for i in range(len(l)):
    sum=sum+l[i]
    if(sum%2==0):
        t.append(str(sum))
    else:
        t.append(str(l[i]))
print(" ".join(t))
