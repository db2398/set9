uyms1,uyms2=map(int,input().split())
maxima=max(ucys1,ucys2)
while(1):
   if(maxima%uyms1==0 and maxima%uyms2==0):
          print(maxima)
          break
   maxima+=1
