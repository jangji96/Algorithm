arr=[0 for i in range(10000)]
dn = 0
for i in range(1,10001) :
  dn = i
  if(i>=10000) :
    dn += i // 10000
    i %= 10000
  if(i>=1000) :
    dn += i // 1000
    i %= 1000
  if(i>=100) :
    dn += i // 100
    i %= 100
  if(i>=10) :
    dn += i // 10
    i %= 10
  dn += i
  if(dn>10000):
    continue
  arr[dn-1] = 1

for j in range(10000) :
  if(arr[j]==1) :
    continue
  print(j+1)