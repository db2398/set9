md1=input()
md2=[]
for i in md1:
   if i.isnumeric():
      md2.append(i)
print("".join(md2))
