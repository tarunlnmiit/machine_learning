"""
Analyze the data -> load the data, clean it, explore it, find patterns, and then visualize results.
"""
import json

# Define some data
people = [
    {"name": "Alice", "age": 28, "field": "data science"},
    {"name": "Bob", "age": 35, "field": "software engineering"},
    {"name": "Carol", "age": 42, "field": "product management"},
]

# calculate average age
total_age = 0
for person in people:
    total_age += person['age']

average_age = total_age / len(people)

# output
print(f"Average Age: {average_age:.1f}")
print(f"Total People: {len(people)}")

# Save results
results = {
    "average_age": average_age,
    "total_count": len(people)
}

with open('results.json', 'w') as f:
    json.dump(results, f)



`ValueError: could not convert string to float` or `IndexError: list index out of range`.