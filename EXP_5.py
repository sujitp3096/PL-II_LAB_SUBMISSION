# Creating tuples
tuple1 = (1, 2, 3, "sujit", 3.14)
tuple2 = "a", "b", "c"
# Accessing elements
print(tuple1[0])
print(tuple1[3])
# Tuple slicing
print(tuple1[1:4])
# Tuple length
print(len(tuple1))
# Tuple concatenation
combined_tuple = tuple1 + tuple2
print(combined_tuple)
# Tuple repetition
repeated_tuple = tuple2 * 3
print(repeated_tuple)
# Checking if an element exists
if "sujit" in tuple1:
   print("sujit is in the tuple")
# count method for occurances
print(tuple1.count(2))
#index method
print(tuple1.index("sujit"))