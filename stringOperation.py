s = input("Enter a string: ")

print("Length of string:", len(s))

start = int(input("Enter starting index of substring: "))
length = int(input("Enter substring length of substring: "))
print("Substring:", s[start:start+length])

s2 = input("Enter another string to compare: ")
if s == s2:
    print("Strings are Equal")
else:
    print("Strings are NOT Equal")

print("\nIndexing:")
for i, ch in enumerate(s):
    print(f"Index {i} -> {ch}")

s3 = input("\nEnter string to concatenate: ")
print("Concatenated string:", s + " " + s3)
