x=0
while x<10:
    x=x+1
    if x<3:
        continue
    print(x)
    if x>7:
        break

y=1
total=0
while 1:
    total=total+y
    if total>10000:
        print(y)
        print(total)
        break
    y=y+1
