# 1. Use np.add() to add two arrays element-wise.

import numpy as np

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# result = np.add(array1, array2)
# print(result)





# 2. Use np.subtract() to subtract one array from another.

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# result = np.subtract(array1, array2)
# print(result)




# 3. Use np.multiply() to multiply two arrays element-wise.

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# result = np.multiply(array1, array2)
# print(result)




# 4. Use np.divide() to divide two arrays element-wise.

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# result = np.divide(array1, array2) # divide array1 by array2 element-wise
# print(result)





# 5. Use np.mod() to find the remainder when one array is divided by another.

# array1 = np.array([12, 2, 3])
# array2 = np.array([4, 5, 6])
# result = np.mod(array1, array2) # divide array1 by array2 and find the remainder
# print(result)







# 6. Use np.exp() to find the exponential of each element in an array.

# array = np.array([1, 2, 3])
# result = np.exp(array)   # exponential of each element in the array
# print(result)







# 7. Use np.log() to find the natural logarithm of each element in an array.

# array = np.array([1, 2, 3])
# result = np.log(array)   # natural logarithm of each element in the array . By default, np.log() computes the natural logarithm (base e) of each element in the input array. The result is an array of the same shape as the input, where each element is the natural logarithm of the corresponding element in the input array.
# print(result)











# 8. Use np.log10() to find the base-10 logarithm of each element in an array.

# array = np.array([1, 10, 100])
# result = np.log10(array)   # base-10 logarithm of each element in the array
# print(result)







# 9. Use np.sqrt() to find the square root of each element in an array.

import math
# array = np.array([1, 4, 9])
# result = np.sqrt(array)   # square root of each element in the array
# print(result)







# 10. Use np.power() to raise each element of one array to the power of another array.

# array1 = np.array([1, 2, 3])
# array2 = np.array([2, 3, 4])
# result = np.power(array1, array2)   # raise each element of array1 to the power of the corresponding element in array2   .    array1 = [1, 2, 3] and array2 = [2, 3, 4], the result will be [1^2, 2^3, 3^4] = [1, 8, 81].
# print(result)










# 11. Use np.sin() to find the sine values of an array of angles (in radians).

# array = np.array([0, np.pi/6, np.pi/2])
# result = np.sin(array)   # sine values of the angles in the array
# print(result)








# 12. Use np.cos() to find the cosine values of an array.

# array = np.array([0, np.pi/3, np.pi/2])
# result = np.cos(array)   # cosine values of the angles in the array
# print(result)








# 13. Use np.tan() to find the tangent values of an array.

# array = np.array([0, np.pi/4, np.pi/2])
# result = np.tan(array)   # tangent values of the angles in the array
# print(result)






# 14. Convert degree values to radians using np.deg2rad() and then find sine values.

# array_degrees = np.array([0, 30, 90])
# array_radians = np.deg2rad(array_degrees)
# result = np.sin(array_radians)
# print(result)








# 15. Use np.rad2deg() to convert radians back to degrees.

# array_radians = np.array([0, np.pi/6, np.pi/2])
# array_degrees = np.rad2deg(array_radians)
# print(array_degrees)







# 16. Use np.floor() to round down the values of a float array.

# array = np.array([1.7, 2.3, 3.9])
# result = np.floor(array)   # round down the values of the array
# print(result)




# 17. Use np.ceil() to round up the values of a float array.

# array = np.array([1.2, 2.8, 3.1])
# result = np.ceil(array)   # round up the values of the array
# print(result)






# 18. Use np.round() to round each element of a float array to 2 decimal places.

# array = np.array([1.234, 2.567, 3.891])
# result = np.round(array, decimals=2)   # round each element to 2 decimal places
# print(result)






# 19. Use np.maximum() to find the element-wise maximum between two arrays.

# array1 = np.array([1, 4, 3])
# array2 = np.array([2, 1, 5])
# result = np.maximum(array1, array2)   # element-wise maximum between the two arrays
# print(result)






# 20. Use np.minimum() to find the element-wise minimum between two arrays.

# array1 = np.array([1, 4, 3])
# array2 = np.array([2, 1, 5])
# result = np.minimum(array1, array2)   # element-wise minimum between the two arrays
# print(result)





# 21. maximum from 2D array

# array = np.array([[1, 4, 3], [2, 1, 5]])
# result = np.max(array)   # maximum value from the 2D array
# print(result)




# 22.maximum from two arrays


# array1 = np.array([[1, 4, 3], [2, 1, 5]])
# array2 = np.array([[2, 1, 5], [3, 6, 0]])
# result = np.maximum(array1, array2)   # element-wise maximum between the two arrays
# print(result)