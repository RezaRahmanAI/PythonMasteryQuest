# Conditional : Check a score
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")


# For loop: Sum a list of numbers
numbers = [10, 20, 33, 40, 50]
total = 0

for n in numbers:
    total += n
print(f"Total: {total}")

# While loop: Count down
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off!")

# Problem-solving example: Find even numbers

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    if i % 2 == 1:
        odd.append(i)

print(f"Even: {even}")
print(f"Odd: {odd}")

# AI prep: Filter dataset
dataset = [
    {"id": 1, "value": 0.9, "label": "positive"},
    {"id": 2, "value": 0.4, "label": "negative"},
    {"id": 3, "value": 0.7, "label": "positive"}
]

higher_value = [data["value"] for data in dataset if data["value"] > 0.5]

lower_value = [d["value"] for d in dataset if d["value"] < 0.5]
print(f"Higher value: {higher_value}")
print(f"Highest value: {lower_value}")


# LeetCode-Style Challenge
# To sharpen your problem-solving skills, try this: Reverse a list of numbers.
# Reverse a list
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
for n in range(len(numbers) -1, -1, -1):
    reversed_numbers.append(numbers[n])

print(f"Reversed numbers: {reversed_numbers}")

# AI Prep Challenge
# To get closer to AI, try filtering a dataset by label:

dataset = [
    {"id": 1, "value": 0.9, "label": "positive"},
    {"id": 2, "value": 0.4, "label": "negative"},
    {"id": 3, "value": 0.7, "label": "positive"}
]

filtered_data = [data for data in dataset if data["label"] == "positive"]
print(f"Filtered positive data point: {filtered_data}")





