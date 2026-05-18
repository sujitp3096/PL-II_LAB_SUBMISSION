
# Python program to demonstrate list operations
# Creating a list
fruits = ["Apple", "Banana", "Cherry", "Mango"]
print("Original List:", fruits)
# Accessing elements
print("First Fruit:", fruits[0]) # Apple
print("Last Fruit:", fruits[-1]) # Mango
# Modifying a list
fruits[1] = "Blueberry"
print("Modified List:", fruits)
# Adding elements
fruits.append("Orange") # Adds to the end
print("After Append:", fruits)
fruits.insert(2, "Grapes") # Inserts at index 2
print("After Insert:", fruits)
# Removing elements
fruits.remove("Cherry") # Removes specific element
print("After Remove:", fruits)
popped_fruit = fruits.pop() # Removes last element
print("Popped Fruit:", popped_fruit)
print("After Pop:", fruits)
# List slicing
print("First two fruits:", fruits[:2]) # Slicing from start to index 2
# Iterating through a list
print("Iterating through list:")
for fruit in fruits:
    print(fruit)
# Checking membership
print("Is Mango in the list?", "Mango" in fruits)
# Sorting a list
fruits.sort()
print("Sorted List:", fruits)
# Reversing a list
fruits.reverse()
print("Reversed List:", fruits)
# List length
print("Length of List:", len(fruits))
