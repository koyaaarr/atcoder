N=int(input())
li=[]
for i in range(N):
  a,b=input().split()
  b=str(100-int(b)).zfill(3)
  li.append(a+b)
lis = sorted(li)

for i in range(len(li)):
  for j in range(len(li)):
    if lis[i] == li[j]:
      print(j+1)