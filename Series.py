'''
a, b = 0, 1
while b < 10:
    print (b)
    a, b = b, a+b
'''

limit = int(input("Please input the limit for the fibonaci number seqence:"))
a, b = 0, 1
sum = 0
i = 0
while i < limit - 1:
    print (b)
    a, b = b, a+b
    sum += a
    i+=1
print ("\n#####################")
print ("sum = " + str(sum))