yy1,yy2=map(int,input().split())
n=1
while(n<=yy1 and n<=yy2):
   if(yy1%n==0 and yy2%n==0):
      ccv=n
   n=n+1
print(ccv)
