xs1=[7, 4, 12, 18, 13, 21]
xs2=[3, 2, 5]
i=0
while i<len(xs1):
  can_div=False
  for b in xs2:
    if xs1[i]%b==0:
      can_div=True
      break
  if can_div:
    xs1.pop(i)
  else:
    i=i+1
print(xs1)

