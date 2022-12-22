l1=[1,2,3,4,5]
a= slice(2)
print(l1[a])

b=slice(0,5,2)
print(l1[b])


l1_copy=l1[slice(len(l1))]
print(l1.copy())
print(l1)
