f = True
n= int(raw_input())
print('Maximize')
for x in range(1, n+ 1):
    for y in range(1, n+1):
        if f:
            f = False
        else:
            print '+',
        print 'a'+ str(x)+'_' + str(y),
     
print('')
print('Subject to')

for x in range (1,n+1):
    f = True
    for y in range (1, n+1):
        if f:
            f = False;
        else:
            print '+',
        print 'a'+ str(x)+'_' + str(y),
    print('<= 1')

for y in range (1,n+1):
    f = True
    for x in range (1, n+1):
        if f:
            f = False;
        else:
            print '+',
        print 'a'+ str(x)+'_' + str(y),
    print('<= 1')

for s in range (3, 2 * n):
    f = True
    for x in range (1, n + 1):
        y = s - x
        if y < 1 or y > n:
            continue
        if f:
            f = False;
        else:
            print '+',
        print 'a' + str(x) + '_' + str(y),
    print('<= 1')

for s in range (-n+2, n-1):
    f = True
    for x in range (1, n + 1):
         y=s+x
         if y < 1 or y > n:
             continue
         if f:
             f= False;
         else:
             print '+',
         print 'a'+ str(x) + '_' + str(y),
    print('<= 1')    
 
print('Bounds') 
for x in range (1,n+1):
    for y in range (1,n+1):
        print ('0<= ' + 'a' + str(x) + '_' + str(y)+ ' <=1')
print('Generals')
for x in range (1,n+1):
    for y in range (1,n+1):
        print('a' + str(x) + '_' + str(y))
print ('End')       
