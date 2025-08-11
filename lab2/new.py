import numpy as np


arr1 = np.array([[1,2,3,4,5,6], [1,2,9]])
arr_c = arr1.copy()
arr_c1 = arr1
arr_c1[1] = 10

arr3 = arr1.view()
print(arr3)
print(arr1.shape)
print(arr1.reshape(-1))




arr1 = np.array([1,5,9,3,2,1,5,6]) 

# print(arr1)
# print(arr1.shape)  

print(arr1.reshape(2,1,4))
print(arr1.reshape(1,1,8))
# make three dimensional array
print(arr1.reshape(2,2,2))
print(arr1.reshape(2,3,1))