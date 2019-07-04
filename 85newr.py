vet=list(input())
sel=[]
for i in vet:
  if(i not in sel):
    vet.append(i)
if(vet==sel):
  print("Yes")
else:
  print("No")
