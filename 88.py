ucms1,ucms2=map(int,input().split())
maxima=max(ucms1,ucms2)
while(1):
   if(maxima%ucms1==0 and maxima%ucms2==0):
          print(maxima)
          break
   maxima+=1
