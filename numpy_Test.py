# Q1. Create a 1D array from 1 to 100.

import numpy as np
# arr=np.arange(1,101)
# print(arr)




#  Q2. Create an array from 10 to 200 with step 10. 

# arr=np.arange(10,201,10)
# print(arr)





# Q3. Create a 5x5 random integer matrix (1-100). 

from numpy import random
# random_matrix = random.randint(1, 101, size=(5, 5))
# print("5x5 Random Integer Matrix (1-100):")
# print(random_matrix)






# Q4. Create a 4x5 array and print first row, last row, second column, last column, middle 2x2. 

# matrix = random.randint(1, 101, size=(4, 5))
# print("Original 4x5 Array:")
# print(matrix)
# print("First Row:")
# print(matrix[0])
# print("Last Row:")
# print(matrix[-1])
# print("Second Column:")
# print(matrix[:, 1])
# print("Last Column:")
# print(matrix[:, -1])
# print("Middle 2x2:")
# print(matrix[1:3, 1:3])







# Q5. Create a 3D array (2,3,4) and print first block, last block, second row of first block, last element.

# matrix_3d = random.randint(1, 101, size=(2, 3, 4))
# print("Original 3D Array (2,3,4):")
# print(matrix_3d)
# print("First Block:")
# print(matrix_3d[0])
# print("Last Block:")
# print(matrix_3d[-1])
# print("Second Row of First Block:")
# print(matrix_3d[0, 1])
# print("Last Element:")
# print(matrix_3d[-1, -1, -1])











#  Q6. Reshape 24 elements into (4,6), (2,12), (3,2,4).


# arr = np.arange(24)
# arr_4x6 = arr.reshape(4, 6)
# arr_2x12 = arr.reshape(2, 12)
# arr_3x2x4 = arr.reshape(3, 2, 4)
# print("Original Array:")
# print(arr)
# print("Reshaped to (4,6):")
# print(arr_4x6)
# print("Reshaped to (2,12):")
# print(arr_2x12)
# print("Reshaped to (3,2,4):")
# print(arr_3x2x4)









#  Q8. Perform addition, subtraction, multiplication, division, modulus, power on two arrays.

arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = np.array([5, 4, 3, 2, 1])

# print("Addition:", arr_1 + arr_2)
# print("Subtraction:", arr_1 - arr_2)
# print("Multiplication:", arr_1 * arr_2)
# print("Division:", arr_1 / arr_2)
# print("Modulus:", arr_1 % arr_2)
# print("Power:", arr_1 ** arr_2)


#  Anotyher way to perform these operations is by using numpy's built-in functions:

# print("Addition:", np.add(arr_1, arr_2))
# print("Subtraction:", np.subtract(arr_1, arr_2))
# print("Multiplication:", np.multiply(arr_1, arr_2))
# print("Division:", np.divide(arr_1, arr_2))
# print("Modulus:", np.mod(arr_1, arr_2))
# print("Power:", np.power(arr_1, arr_2))










# Q9. Find sum, mean, median, std, variance. 

# arr = np.array([1, 2, 3, 4, 5])
# print("Sum:", np.sum(arr))
# print("Mean:", np.mean(arr))
# print("Median:", np.median(arr))
# print("Standard Deviation:", np.std(arr))
# print("Variance:", np.var(arr))







# Q10. Find max, min, argmax, argmin

# arr = np.array([1, 2, 3, 4, 50, 6, 7, 8, 9, 10])
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))
# print("Argmax:", np.argmax(arr))
# print("Argmin:", np.argmin(arr))

# argmax returns the index of the maximum value in the array, while argmin returns the index of the minimum value in the array.










# Q11. Print elements >50, even, odd, divisible by 3. 

# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# for i in arr:
#     print(i)    # Output :- 10,20,30,40,50,60,70,80,90,100
#     if i>50:
#         print("Greater than 50:", i)
#     if i%2 == 0:
#         print("Even:", i)
#     if i%2 != 0:
#         print("Odd:", i)
#     if i%3 == 0:
#         print("Divisible by 3:", i)







# Q12. Replace elements >60 with 100 using where().

# num=np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# c=[]
# for i in num:
#     if i > 60:
#         c.append(100)
#     else:
#         c.append(i)
# print(c)








# Q13. Print unique values from duplicate array. 

# arr = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9])
# unique_values = np.unique(arr)
# print(unique_values)  # Output: [1 2 3 4 5 6 7 8 9]









# Q14. Sort ascending and descending.

# arr = np.array([5, 2, 9, 1, 5, 6])
# print(np.sort(arr))  # Ascending order
# print(np.sort(arr)[::-1])  # Descending order








# Q15. Generate random integers, random floats, and a 4x4 random matrix. 

# num = np.random.randint(1, 101, size=5)  # Random integers between 1 and 100
# floats = np.random.rand(5)  # Random floats between 0 and 1
# matrix_4x4 = np.random.randint(1, 101, size=(4, 4))  # 4x4 random integer matrix

# print("Random Integers:", num)
# print("Random Floats:", floats)
# print("4x4 Random Integer Matrix:", matrix_4x4)









# Q16. Matrix addition, subtraction, dot product, element-wise multiplication. 

# matrix_a = np.array([[1, 2], [3, 4]])
# matrix_b = np.array([[5, 6], [7, 8]])
# add = np.add(matrix_a, matrix_b)
# print("Matrix Addition:\n", add)
# subtract = np.subtract(matrix_a, matrix_b)
# print("Matrix Subtraction:\n", subtract)
# dot_product = np.dot(matrix_a, matrix_b)
# print("Matrix Dot Product:\n", dot_product)
# element_wise_mul = np.multiply(matrix_a, matrix_b)
# print("Element-wise Multiplication:\n", element_wise_mul)











# Q17. Find transpose of a 4x4 matrix.

# matrix = np.random.randint(1, 101, size=(4, 4))
# print("Original 4x4 Matrix:\n", matrix)
# transpose = np.transpose(matrix)
# print("Transpose of the Matrix:\n", transpose)

# another way 

# print(matrix[: : -1 ,: :-1])  # This will reverse the order of rows and columns, effectively giving the transpose.







# Q18. Create identity, zeros, ones, and full(value=7) matrices. 

# identity_matrix = np.eye(4)  # 4x4 Identity matrix
# zeros_matrix = np.zeros((4, 4))  # 4x4 Zeros matrix
# ones_matrix = np.ones((4, 4))  # 4x4 Ones matrix
# full_matrix = np.full((4, 4), 7)  # 4x4 Full matrix with value 7

# print("Identity Matrix:\n", identity_matrix)
# print("Zeros Matrix:\n", zeros_matrix)
# print("Ones Matrix:\n", ones_matrix)
# print("Full Matrix (value=7):\n", full_matrix)










# Q20. Split 24 elements into 2, 3, and 6 equal parts.

# arr = np.arange(10)
# split_2 = np.array_split(arr, 2)
# split_3 = np.array_split(arr, 3)
# split_6 = np.array_split(arr, 6)

# print("Original Array:", arr)
# print("Split into 2 parts:", split_2)
# print("Split into 3 parts:", split_3)
# print("Split into 6 parts:", split_6)






# Q21. Use broadcasting to add a 1D array to each row of a 3x3 matrix. 

# matrix=np.arange(1,10)
# matrix=matrix.reshape(3,3)
# print("Original 3x3 Matrix:\n", matrix)
# arr_1d = np.array([10, 20, 30])
# for i in matrix:
#     print(np.add(i, arr_1d))  # This will add the 1D array to each row of the 3x3 matrix using broadcasting.







# Q22. Demonstrate copy() vs view(). 


original_array = np.array([1, 2, 3, 4, 5])
copied_array = original_array.copy()  # Creates a copy of the original array
viewed_array = original_array.view()  # Creates a view of the original array
print("Original Array:", original_array)
print("Copied Array:", copied_array)
print("Viewed Array:", viewed_array)


# Modifying the copied array does not affect the original array
copied_array[0] = 100   
print("After modifying copied array:")
print("Original Array:", original_array)
print("Copied Array:", copied_array)
print("Viewed Array:", viewed_array)



# if the original array is modified, the view will reflect those changes, but the copied array will remain unchanged.
original_array[0] = 200
print("After modifying original array:")
print("Original Array:", original_array)
print("Copied Array:", copied_array)
print("Viewed Array:", viewed_array)



# if viewed_array is modified, the original array will also be affected, but the copied array will remain unchanged.
viewed_array[1] = 300
print("After modifying viewed array:")  
print("Original Array:", original_array)