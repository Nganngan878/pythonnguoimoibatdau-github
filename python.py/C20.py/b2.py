#20/07/2026
"""
2:Generator Expressions
Task: Create a Generator Expression that generates numbers from 1 to 5, where each number is doubled (x * 2). Use a for loop to print each value produced by the generator.
Expected Output: 2, 4, 6, 8, 10 (each on a new line)
"""
gen_ex=[x*2 for x in range(1,5)]
print(gen_ex)