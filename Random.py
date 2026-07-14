from numpy import random

# x = random.randint(100)
# print(x)


# import numpy as np
# x = np.random.randint(100)
# print(x)


# 1. Generate a random integer between 0 and 10.

# y= random.randint(10)
# print(y)

# Output :- 0 ≤ number < 10


# 2. Generate an array of 5 random integers between 1 and 100.

# for i in range(0,5):
    #  print(i) 
            #    output :- 0,1,2,3,4
            
    # y= random.randint(1, 101)
    # print(y)
    
    
# OR

# import numpy as np
# random_integers = np.random.randint(1, 101, size=5)   
# print("Random Integers between 1 and 100:")
# print(random_integers)
    
    
    
    
# 3. Generate 10 random numbers from a standard normal distribution using np.random.randn().

numbers = random.randn(10)
print(numbers)

# random.randn() generates samples from the standard normal distribution (mean = 0, standard deviation = 1). The output will be an array of 10 random numbers drawn from this distribution.

# random.rand() generates samples from a uniform distribution over [0, 1). The output will be an array of random numbers between 0 and 1.
# Generate a random float from 0 to 1: Is done by  random.rand()

# random.randint(high) → Generates a random integer from 0 to high - 1.
# random.randint(low, high) → Generates a random integer from low to high - 1.
# random.randint(low, high,size) → Generates a random integer from low to high - 1 , size specifies the shape of the output array.





# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.normal(size=1000), kind="kde")

# plt.show()





# 4. Generate an array of 5 random floats between 0 and 1 using np.random.rand().

# print("Random floats between 0 and 1:")
# random_floats = random.rand(5)
# print(random_floats)



# 5. Generate a 2×3 array of random floats between 0 and 1.

# print("2×3 array of random floats between 0 and 1:")
# random_array = random.rand(2, 3)
# print(random_array)




# 6. Set a random seed 42 and generate 5 random numbers to make the result reproducible.

import numpy as np

# np.random.seed(42)

# print(np.random.rand(5))






# 7. Set a random seed and generate a 3×3 array of random integers between 0 and 50.

import numpy as np

# np.random.seed(42)

# print(np.random.randint(0, 51, (3, 3)))





# 8. Generate 10 random integers between 0 and 20 and sort them.

# random_integers = np.random.randint(0, 21, 10)
# sorted_integers1 = np.sort(random_integers)  # Sort in ascending order
# sorted_integers = np.sort(random_integers)[::-1]  # Sort in descending order
# print(sorted_integers)






# 9. Randomly select 3 elements from the array [10, 20, 30, 40, 50].

# array = np.array([10, 20, 30, 40, 50])
# selected_elements = np.random.choice(array, size=3, replace=False)  # replace=False ensures unique selection
# print(selected_elements)




# array = np.array([10, 20, 30, 40, 50])
# x= np.random.choice(array, size=3) 
# print(x)  # This will print 3 random elements from the array, allowing for duplicates since replace=True by default.










# 10. Randomly shuffle the array [1, 2, 3, 4, 5].

# array = np.array([1, 2, 3, 4, 5])
# random.shuffle(array)
# print(array)  # This will print the array in a random order each time the code is run.  








# 11. Randomly select 5 elements from the array [1,2,3,4,5,6,7,8,9,10] with replacement.

# array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# selected_elements = np.random.choice(array, size=5, replace=True)
# print(selected_elements)  # This will print 5 random elements from the array, allowing for duplicates since replace=True.





# 12. Randomly select 5 elements from the same array without replacement.

# array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# selected_elements = np.random.choice(array, size=5, replace=False)
# print(selected_elements)








# 13. Create a random permutation of the numbers from 0 to 9.

# array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# random_permutation = np.random.permutation(array)
# print(random_permutation)

# permutation does not modify the original array, it returns a new array with the elements randomly permuted.







# 14. Generate 5 random numbers from a normal distribution with mean 10 and standard deviation 2.

# np.random.seed(42)  # Setting a seed for reproducibility
# random_numbers = np.random.normal(loc=10, scale=2, size=5)
# print(random_numbers)







# 15. Generate 5 random numbers from a uniform distribution between 5 and 15.

# random_numbers = np.random.uniform(low=5, high=15, size=5)
# print(random_numbers)




# 16. Generate 5 random numbers from a binomial distribution with n=10 and p=0.5.

# random_numbers = np.random.binomial(n=10, p=0.5, size=5)
# print(random_numbers)




# 17. Generate 5 random numbers from a Poisson distribution with λ=3.

# random_numbers = np.random.poisson(lam=3, size=5)
# print(random_numbers)




# 18. Generate 5 random numbers from an exponential distribution with scale=2.

# random_numbers = np.random.exponential(scale=2, size=5)
# print(random_numbers)





# 19. Create a 3×3 random integer array and find its maximum and minimum values.

# random_array = np.random.randint(0, 100, (3, 3))
# print("Random Array:")
# print(random_array)
# print("Maximum Value:", np.max(random_array))
# print("Minimum Value:", np.min(random_array))









# 20. Create a 1D array of 10 random floats and calculate the mean.

# x=random.rand(10)
# mean_value = np.mean(x)
# print("Random Floats:", x)
# print("Mean Value:", mean_value)







