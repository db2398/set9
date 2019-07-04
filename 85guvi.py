i=list(input())
o=[]
for j in i:
   if j not in o:
      o.append(j)
if i==o:
   print("Yes")
else:
   print("No")
