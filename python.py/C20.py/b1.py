#20/07/2026
"""
Dạng 1:Comprehensions 
Exercise
Task: Given a list of numbers: nums = [10, 15, 20, 25, 30]. Use a List Comprehension to create a new list containing only the numbers greater than 15, multiplied by 2.
Expected Output: [40, 50, 60]
"""
#Lits
numbers=[1,2,3,4,5,6]
numbers_even=[x**2 for x in numbers if x%2==0]
print("Lits:",numbers_even)
print(numbers_even)

#set comprehension
fruits=["apple","banana","cherry","orange"]
fruits_slow={len(f) for f in fruits}
print(fruits_slow)
#dict
cube_dict={x:x**3 for x in range(1,4)}
print(cube_dict)
#matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flax_lits=[num for row in matrix for num in row]
print(flax_lits)
#Thực hành
nums=[10,15,20,25,30]
nums_so=[x*2 for x in nums if x>15]
print(nums_so)