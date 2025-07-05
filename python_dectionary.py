# A dictionary in Python is an unordered, mutable collection of key-value pairs.

# creating a dictionary 

student = {
    "name": "ramakrishna",
    "age": 24,
    "course": "Developer"
}
print(student)
# empty_dictionary
empty_dict =  {} 
#  Keys must be unique and immutable (like strings, numbers, or tuples). Values can be of any data type.

# 2🔹 Accessing Items
print(student["name"])       # Alice
print(student.get("age"))    # 21
print(student.get("grade", "Not Found"))  # Returns default value

# 3🔹 Adding & Updating Items
student["grade"] = "A"         # Add new key
student["age"] = 22            # Update value

# 4🔹 Removing Items
student.pop("course")          # Removes "course"
student.popitem()              # Removes last inserted item
del student["age"]             # Deletes key 'age'
student.clear()                # Removes all items

# 🔹 Looping Through a Dictionary

for key in student:
    print(key, student[key])     # Access keys and values

for key, value in student.items():
    print(key, value)

# 🔹 Nested Dictionary

students = {
    "101": {"name": "Alice", "age": 21},
    "102": {"name": "Bob", "age": 22}
}

print(students["101"]["name"])  # Alice


# 🔹 Example Use Case: Word Counter
text = "apple banana apple orange banana apple"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

