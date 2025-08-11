import numpy as np
arr=np .array( ['A', 2.5, 6])
arr1=np .array( [4, 2.5, 6] , [3,4,5])
print(arr)
print(type(arr))
print(arr1)
print(type(arr1))
arr2=np .array(10)
print(type(arr2))

# fix the dimensiomn of arr1

arr1=np .array( [4, 2.5, 6] , ndmin=3)
print(arr1)



arr6 = np.array([[4, 2.5, 6], [2, 32, 111]])
print(arr6[0, 1])


arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])

print(arr3d[1, 0, 1])  
print(arr3d[0, 0, 1])  



np.zeros((2,3))
np.ones((2,3))
np.full((2,3))
np.arrange(0,100,5)
np.eye(5)
np.random.rand(0,10)
np.random.randit(0,10)

#print them
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.full((2, 3), 5))


arr= np.array([[1,2,5,6],[5,9,2,3]])
arr[0,2:3]
print(arr)