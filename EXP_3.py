str1 = "Sujit"
str2 = "Pawar"

print("Original Strings:")
print("str1:",str1)
print("str2:",str2)
# 1. Concatenation (Adding Strings)

full_name = str1 + " " + str2
print("Concatenation:",str1+ " "+str2)
# 2. Length of Strings
length_str1 = len(str1)
length_str2 = len(str2)
print("Length of str1:",length_str1)
print("Length of str2:",length_str2)
# 3. Slicing Strings
print("Slicing Examples:")
print(str1[:5]) # Characters from the beginning up to index 5 (exclusive)
print(str2[2:]) # Characters from index 2 to the end
print(str1[1:6]) # Characters from index 1 up to index 6 (exclusive)
# 4. Case Conversion
uppercase_str1 = str1.upper()
lowercase_str2 = str2.lower()
print("Uppercase str1:",uppercase_str1)
print("Lowercase str2:",lowercase_str2)
# 6. Finding Substrings
index_a_str1 = str1.find('a')
index_de_str2 = str2.find('de')
print("Index of 'a' in str1:",index_a_str1)
print("Index of 'de' in str2:",index_de_str2)
# 7. Splitting Strings
sentence = "This is a sample sentence"
words = sentence.split(' ')
print("Splitting a sentence:",words)