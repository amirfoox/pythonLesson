s = 'My mom said: "Get home!"'
print(s)
print(s[0], s[1], s[5], s[-1])

s1 = "Hello"
s2 = "Bye"
print(s1+str(s2))
print(3*s2) # nsync reference
print(len(s1))
print(s1[len(s1) - 1]) # the len is 5, but the index of "Hello" is 0-4. -1 fixes the issue

# string is iterable, so you can use for:
for c in s1:
    print(c, end = " ") # print each character
print("\n")

# print a string backwards
s = "racecar"
i = len(s) - 1
while i >= 0:
    print(s[i], end =" ")
    i -= 1

s = "My name is Amir"
i = len(s) - 1
while i >= 0:
    print(s[i], end =" ")
    i -= 1

print("Slice Examples!")
s = "0123456789X"
print(s[0: 2])
print(s[: 3]) # 0 - 3
print(s[3:]) # 3 - to end
print(s[2::2]) # in steps 2
print(s[::-1]) # reverse the string

s = "IP address - 127.0.0.1"
if s[0:2] == "IP":  # check for the word IP
    print("this is an ip address")

print("\nString comparison")
# string comparison
a = "banana"
b = "Banana"

print (a == b)

# CAPITAL letters are considered SMALLER than lower case letters, Banana is smaller than banana

a = "banana"
b = "banana"
print (a is b)

a = "apple"  # a is now something else, a different assignment
print(b)


