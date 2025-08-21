#Write code to find the maximum number in numbers.
# Hint: Use a for loop and compare each number to a max_value.
numbers = [10, -5, 0, 7, -2]
max_value = numbers[0]
for i in numbers:
    if i > max_value:
        max_value = i

print(max_value)


#Challenge (LeetCode Style):

#Find the second largest number in numbers.
# Hint: Track max_value and second_max, updating both in the loop.


