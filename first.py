# Q1. Create a 1D NumPy array from 1 to 20 and print all elements at even indexes.

import numpy as np

# num=
# for i in range(0,21):
#     num[i]=i
#     print(i)
    
#     num=np.array([i])
#     # num[i]=num+num[i]
# print(num)



# correct hai yea pr upper waale pr bhi kaam karna hai

# l=np.arange(1, 21)
# print(l[::2])



# Q2. Create a 2D array of shape (4, 5) using numbers from 1 to 20. Print the element at row 3, column 4.

# l=np.array([[1,1,1,1,1],[2,2,2,2,2],[3,7,8,9,11],[4,4,4,4,8]])
# print(l)
# print(l.shape)
# print(l[3,4]) 



# Q3. Create a 3D NumPy array with shape (2, 3, 4) and access the last element of the second block.

# n=np.array([[[0,1,2,3],[4,5,6,7],[8,9,10,11]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
# print(n.shape)
# print(n[1,2,3])




# Q4. Create an array from 10 to 50. Slice and print elements from index 5 to index 15 with a step of 2.

# l=np.arange(1, 51)
# print(l[5:16:2])

# arrange 


# Q5. Create a 2D array of shape (5, 5). Print only the middle 3 x 3 matrix using slicing.

# arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
# print(arr.shape)
# print(arr[1:4,1:4])

# a=np.array([[10,20,30],[40,50,60]])
# print(a[0:1,0:2])

# in the slicing [In this field the value of row is given:in this field the value of coloum  is selected]


# Q6. Create a NumPy array containing integers, floats, and strings. Check and print its data type.

# el=np.array([1,2,3,1.1,2.6,5.5,"apple"])
# print(type(el))

# Output class=numpynd.array



# Q7. Create an integer array and convert it into float64 data type without changing the original array.


# arr = np.array([1,2,3,4,5])
# c=arr.astype(float)
# # c=np.float64(arr)
# print(c.dtype)
# print(type(arr))

# this will be print with the help of dtypr





# Q8. Create an array with decimal values and convert it into integer type. Observe what happens to the decimal values.


# num=np.array([1.1,2.6,3.5,4.22,0.5,6.6,8])
# # c=num.astype(int)
# c=np.int64(num)
# print(num)
# print(c.dtype)
# print(c)
# print(type(num))





# Q9. Create an array using np.array([1, 2, 3, 4]). Make a copy of it, change the first value in the copied array, and print both arrays.

# arr = np.array([1, 2, 3, 4])
# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)






# Q10. Create an array and make a view of it. Change one value in the view and check whether the original array changes.

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)








# Q11. Create a 2D array and create a copy of only its first two rows. Modify the copied array and verify whether the original array changes.

# l=np.array([[1,1,1,1],[2,2,2,2],[3,7,8,9],[4,4,4,4]])
# x= l[0:2,0:].copy()
# l[0]=32

# print(l)
# print(x)






# Q13. Create an array with 30 elements and reshape it into a 2D array where the number of rows is
# automatically calculated using -1.

# num = np.arange(1, 31)
# p=num.reshape(-1,5)
# print(p)

# print(p.shape)

# here -1 calculate the number of row and 5 indicates that the number of element contaon by each row
# or by -1 we can say that to numpy to calculate automatically if -1 is first place then it calculate the row automatically or other wise it calculate column








# split are use to split the array is the given number

# a=np.array([1,2,3,4,5,6])
# print(np.array_split(a,4))












# use of linspce ??
# np.zeros 
# np.ones
# np.full
# np.eye
# where condition is the conditional statement in np
#  there is also some fuctions like sum,mean,median,mijn,max,std
# arr.itemsize
# np.linspace
# np.diag (diagnol)
# np.where(a%2==0,'even','Odd')
# np.concatenate((,))

# Broadcasting





# d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(d.ndim)
# print(d)
# # print(d.shape)
# print(d.reshape(-1))
# print(d[1,0])











# 14 . Create a 2D array of shape (3, 4). Flatten it into a 1D array using reshape(-1).

# arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arr.reshape(-1))



# Q15. Create a 3D array of shape (2, 4, 3). Print its shape, number of dimensions, and total number of
# elements.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 , 14 , 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

# newarr = arr.reshape(2, 4, 3)
# print(newarr)
# print(newarr.ndim)
# print(newarr.shape)
# print(newarr.size)



# Q16. Create a 2D array of shape (4, 4). Extract all elements from the last column using indexing.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 , 14 , 15, 16])
# newarr = arr.reshape(4, 4)           
# print(newarr)
# for i in newarr:

    # print(i)
    # print(type(i))
    
    # print(i[3])
    
    
    
    
    
    
    
    
# Q17. Create a 2D array and print alternate rows and alternate columns using slicing.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 , 14 , 15, 16])
# newarr = arr.reshape(4, 4)   
# print(newarr)
# print(newarr[0:4:2,0:4])
# print(newarr[0:4,0:4:2])










# Q18. Create an array from 1 to 36 and reshape it into (6, 6). Print: First row, Last row, First column, Last
# column, and Main diagonal elements.

# l=np.arange(1, 37)
# newarr = l.reshape(6, 6)  
# print(newarr)

# first row

# for i in newarr:
#     print(i)
#     break


# last row

# print(newarr[5:6,0:])

# first coloumn

# print(newarr[0:,0:1])

# last coloumn

# print(newarr[0:,5:6])

#  Main diagonal elements

# for i in range(0,6):
#     for j in range (0,6):
#         if i == j:
#             print(newarr[i,j])







# Q19. Create a NumPy array with shape (2, 3, 4). Reshape it into (4, 6) without losing any data. Then
# reshape it back to (2, 3, 4).

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 , 14 , 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

# newarr = arr.reshape(2, 4, 3)
# print(newarr)
# c=newarr.reshape(4,6)
# print(c)
# d=c.reshape(2,3,4)
# print(d)







# Q20. Create a 2D NumPy array with 5 rows and 6 columns. Use slicing to extract: Rows 2 to 4, Columns 3
# to 5, Every second row, Every second column, and reverse the complete array row-wise and column-wise.

# arr=np.arange(1, 31)
# new=arr.reshape(5,6)
# print(new)

# #  Rows 2 to 4
# print(new[1:4])

# # Columns 3 to 5

# print(new[:,2:6])

# Every second row

# print(new[::2])

# Every second column

# print(new[:,::2])
# ROW reverse
# print(new[::-1])
# coloumn reverse
# print(new[:,::-1])
# 
# print (new[::-1,::-1])



#  zeros matrix
# num=np.zeros((4,4))
# print(num)

# identity matrix

# num=np.eye((3))
# print(num)

# num =np.array([1,2,3])
# o=num.astype(float)
# print(num)
# print(o)

# num=np.arange(1,10,5)
# print(num)


# num1=np.linspace(1,10,5)
# print(num1)

# Working of linspace is it divide the number into given numbers of time with in range
