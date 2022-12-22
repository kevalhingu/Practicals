a=[2,2.5,'keval',-5]
print(a)
print(a[2])
print(a[-1])

#for i in range(3):
#    print(a)
i=0
while i in range(5):
    print(a)
    i=i+2

a.pop()

print (a)
a[1]=5
print (a)


l1=[1,2,'keval']
l2=[-2,'friend',0.5]

l1.extend(l2)
print(l1)
l1.reverse()

print(l1)

for a in l2:
    l1.remove(a)
l1.sort()
print(l1)
