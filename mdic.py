from readmdict import MDX
import csv

csvaddress='ar.csv'




mdx= MDX('ar.mdx')
items = mdx.items()
tx=mdx.items().next()
lst=[]
i=0
for counter in items:
    try:
        templst=list(tx)
        lst.append(templst)
        tx=items.next()
    except:
        length=len(lst)
        #for count in xrange(20):
        with open(csvaddress,'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(lst)








"""
            string=str(lst)
            print(string.encode('utf-8'))
            #print(str(lst[count][1]).encode('utf-8'))
"""

"""
        for i in range(len(lst2)):
            print (i)
            print(type(lst2[i]))
"""





"""
file = open('fulldic2.html', "w")
for i in items:
    file.write(str(items.next())+'\n')
file.close()
"""
"""
f = codecs.open('mdic.html', encoding = 'utf')
for line in f:
    print(repr(line).decode())
"""
#result = [tuple(map(lambda x: x.encode('utf-16'), tup)) for tup in mytx]
#print(tx)

"""
with io.open("mdic.html" , "r" , encoding='utf-8') as mdic_file:
    my_unicode_str = mdic_file.read()
print(my_unicode_str)
"""


#print(mytx.decode('utf-8')))

#print(tx.decode('utf-8'))

#result = [tuple(map(lambda x: x.encode('utf-16'), tup)) for tup in tx]

"""
text= tx
print(text.decode('utf-8'))


print(items.next())

print(items.next())

print(items.next())

print(items.next())

print(items.next())

print(items.next())

print(items.next())

print(items.next())

print(items.next())

print(items.next())
"""