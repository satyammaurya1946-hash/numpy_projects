# Q1. How do you create a NumPy array from a Python list?
import numpy as np

# l=[1,2,3,4,5,6]
# print(type(l))

# num=np.array([l])
# print(num)
# print(num.dtype)



# Q2. What is the difference between np.arange() and np.linspace()?

# num=np.arange(1,10,5)
# print(num)

# In arrange numpy arrange make the matrix as the gap of 5 element 


# num1=np.linspace(1,10,5)
# print(num1)

# In linespace numpy arrange make the matrix from the given range containg the 5 element





# Q3. Create a 3x3 zero matrix and a 3x3 identity matrix.

#  zeros matrix

# num=np.zeros((4,4))
# print(num)

# identity matrix

# num=np.eye((3))
# print(num)





# Q4. How do you access the element in the 2nd row and 3rd
# column of an array?

# num = np.arange(1,31)
# arr=num.reshape(5,6)
# print(arr)
# print(arr[1,2])




# Q5. Give an example of negative indexing.

# num = np.arange(1,31)
# arr=num.reshape(5,6)
# print(arr)
# print(arr[: :-1,::-1])



# Q6. How can you extract an entire column from a 2D array?

# num = np.arange(1,31)
# arr=num.reshape(5,6)
# print(arr)
# for i in arr:
#     for j in i:
#         print(j)
    
    
    
    





# Q7. How do you print the first 5 elements using slicing?

# num=np.array([1,2,3,4,5,6])
# print(num[:5])







# Q8. Print the last 3 elements of an array using slicing.

# num=np.array([1,2,3,4,5,6])
# print(num[-3:])




# Q9. How do you slice the first 2 rows and last 2 columns of a 2D array?

# num = np.arange(1,31)
# arr=num.reshape(5,6)
# print(arr)

# first 2 rows

# print(arr[0:2])

# last 2 columns

# print(arr[0:,-2:])









# Q10. Which function is used to check the data type in NumPy?

# d.type

# num=np.array([1.1,2.6,3.5,4.22,0.5,6.6,8])
# # c=num.astype(int)
# c=np.int64(num)
# print(num)
# print(c.dtype)








# Q11. What is the use of the astype() function?

# astype() is used for convert the data type of array

# num=np.array([1.1,2.6,3.5,4.22,0.5,6.6,8])
# # c=num.astype(int)
# c=np.int64(num)
# print(num)
# print(c.dtype)






# Q12. Write code to convert a float array into an integer array.

# num=np.array([1.1,2.6,3.5,4.22,0.5,6.6,8])
# # c=num.astype(int)
# c=np.int64(num)
# print(num)
# print(c.dtype)












# Q13. What is the difference between Copy and View in NumPy?

# copy just copy the array at once it dose not change if the origional array change

# l=np.array([[1,1,1,1],[2,2,2,2],[3,7,8,9],[4,4,4,4]])
# x= l[0:2,0:].copy()
# l[0]=32

# print(l)
# print(x)


# view just keep the eye on the origional array if the origional array change then the value of view is also change 

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)










# Q14. What happens to the original array if you change a view?
# Q15. Write an example showing both copy and view.


# Done in Question number 13








# Q16. What does the shape attribute represent?

# define the shape of the array that what is the dimansions of array

# num = np.array([1,2,3,4,5])
# print(num.shape)


# Q17. What does the shape (5,) mean for a 1D array?

# The 5 represent the number of column
# after the commas the dimension represent because it is in 1D so nothing is written here






# Q18. Explain ndim and size with an example.

# l=[1,2,3]
# c=np.array(l)

# print(type(c))
# print(c.ndim)
# print(type(l))
# print(c.dtype)

# print(c.size)










# Q19. How do you reshape a 1D array into a 2D (3x3) array?

# num=np.arange(1,10)
# arr=num.reshape(3,3)
# print(arr)








# Q20. What error occurs if the element count does not match during reshape?

# num=np.arange(1,15)
# arr=num.reshape(3,3)
# print(arr)

# The error is generated is ValueError








# Q21. What does the -1 parameter do in reshape()?

# d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(d)
# print(d.reshape(-1))

# here -1 calculate the number of row and 5 indicates that the number of element contaon by each row
# or by -1 we can say that to numpy to calculate automatically if -1 is first place then it calculate the row automatically or other wise it calculate column







# Q22. How can you print each element of a 2D array using a loop?

# num=np.arange(1,10)
# arr=num.reshape(3,3)
# print(arr)
# for i in arr:
#     for j in i:
#         print(j)









# Q23. What is the purpose of the np.nditer() function?

arr = np.array([[1, 2], [3, 4]])
for element in np.nditer(arr):
    print(np.nditer(arr))
    
    
# The numpy.nditer object offers a various way to iterate over arrays. It allows iteration in different orders and provides better control over the iteration process.


# Q24. What is the difference between np.concatenate() and np.stack()

# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

# axis = 1 means along y axis


# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)


# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)




# np.stack()


# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)

# 1
# NumPy provides a helper function: hstack() to stack along rows.

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))

# print(arr)


# 2 

# NumPy provides a helper function: vstack()  to stack along columns.

# | Function           | Adds New Axis? | Equivalent To                                                         |
# | ------------------ | -------------- | --------------------------------------------------------------------- |
# | `np.concatenate()` | ❌ No           | Join along an existing axis                                           |
# | `np.stack()`       | ✅ Yes          | Join along a new axis                                                 |
# | `np.hstack()`      | ❌ No           | `concatenate(axis=1)` for 2D, `concatenate(axis=0)` for 1D            |
# | `np.vstack()`      | ❌ No           | `concatenate(axis=0)` (after promoting 1D arrays to rows when needed) |


# Q25. Give an example of joining two arrays horizontally and vertically.

# horizontal
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)


# vertically
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=0)
# print(arr)



# Q26. What does the np.array_split() function do ?


# Split the array into given number of array

# Q27. Split a 1D array into 3 equal parts.

# a=np.array([1,2,3,4,5,6,5])
# print(np.array_split(a,3))

# Q28. What is the difference between np.where() and np.searchsorted()?


# np where is a conditional statement used in numpy
# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.
# where contain at the index of array
# where act as a loop in the array.


# n=np.array([1,2,3,4,6,8])
# print(np.where(n%2==0))

# np.searchsorted

# np.searchsorted() is used to find the position (index) where a value should be inserted in a sorted array so that the array remains sorted.

# arr = np.array([10, 20, 30])
# val = 15
# idx = np.insert(arr,np.searchsorted(arr, val),val)
# print("Insertion index:", idx)
# print(arr) 



# Q29. Show an example of sorting an array in ascending and descending order.


# descending order.

# arr=np.array([5,8,7,2,3,5,6,0])
# y=np.sort(arr)[::-1]
# print(y)



# asceding order

# arr=np.array([5,8,7,2,3,5,6,0])
# y=np.sort(arr)
# print(y)


# l=[2,5,4,6,9,8,7,1]
# l.sort(reverse=True)
# print(l)


# numbers = [34, 1, 9, 5, 22]
# numbers.sort(reverse=True)
# print(numbers)




# Q30. Give an example of filtering an array using boolean indexing (print elements greater than 5).



# num = np.array([12,1,2,45,56,63,96,87,0.2,2,1,3,4,5])
# arr=[]
# for i in num:
#     print(i)
#     if i >5:
#         arr.append(True)
#     else:
#         arr.append(False)
# x=num[arr]
# print(x)
# print(arr)
# print(num)