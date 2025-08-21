name = "Python Master"
score = 95
accuracy = 0.98
is_pro = True
skills = ["Python", "AI", "Problem Solving"]
stats = { "win": 10, "losses": 2}


# Basic Operation
score = score + 5
greeting = f"Hi, {name}! Your accuracy is {accuracy*100}%"
skills.append("LeetCode")
skills.append(".Net Core")

# Print results
print(greeting)
print("Skills:",skills)
print("Stats:",stats)
print("Score",score)
print("Is pro? ",is_pro)

# Mini Problem-Solving Challenge (LeetCode Style)
# To get you thinking like a top coder, try this simple problem: Calculate the average of a list of scores.

scores = [85, 90, 95, 100, 88]
average_score = sum(scores)/len(scores)
print("Average Score:",average_score)

# Mini AI Prep: Simulating a Dataset
# AI often involves working with data. Let’s create a simple “dataset” using a list of dictionaries:

dataset = [
    {"id": 1, "feature": 0.5, "label": "positive"},
    {"id": 2, "feature": 0.8, "label": "negative"},
    {"id": 3, "feature": 0.3, "label": "positive"},
    {"id": 4, "feature": 0.7, "label": "negative"}
]

for data in dataset:
    print(f"Data point:  {data['id']}: Feature {data['feature']}, Label {data['label']}")

for d in dataset:
    print(f"Data point: {d['id']} Feature {d['feature']} Label {d['label']}")


# Challenge:
#
# Create a list of 5 numbers and print only the numbers greater than 90.
# Hint: Use a loop (we’ll cover loops in the next step, but try for num in scores: if num > 90: print(num)).


numbers = [84, 99, 200, 233, 89]
for number in numbers:
    if number > 90: print(f"Number {number} is greater than 90")
