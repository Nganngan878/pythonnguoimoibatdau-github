#20/07/2026
"""
3.Generator Functions and yield
Exercise
Task: Write a generator function named even_numbers(n) that yields all even numbers from 0 up to n (inclusive). Test it by looping through even_numbers(6).
Expected Output: 0, 2, 4, 6
"""
def even_nums(n):
    count=0
    while count<=n:
        yield count
        count+=2
print("Result:")
for num in even_nums(6):
    print(num)
