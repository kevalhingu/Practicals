import numpy as np
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
n=5
a=np.repeat(List1,n,axis=0)
print(a)
