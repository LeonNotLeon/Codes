#!\usr\bin\python3

a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
num = 0
newNum = 0
i = 0
while i < 350000:
    if f<9:
        f += 1
    elif e < 9:
        e+=1
        f = 0
    elif d<9:
        d+=1
        e, f = 0, 0
    elif c < 9:
        c+=1
        d, e, f = 0, 0, 0
    elif b < 9:
        b+=1
        c, d, e, f = 0, 0, 0, 0
    elif a < 9:
        a+=1
        b, c, d, e, f = 0, 0, 0, 0, 0

    num = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
    newNum = b*100000 + c*10000 + d*1000 + e*100 + f*10 + a
    print (num)
    print (newNum)
    print ("\n")

    if newNum == 3*num:
        print (num)
        break

    i+=1

print ("heheheha")

#14287