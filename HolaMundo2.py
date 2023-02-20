# print the multiplication  table 1-10 without duplicates (if a*b=c appears, then b*a=c should not)

# suppose you can only do additions. Write a program that reads two positive, integer numbers a and b It computes a ** b

# Read an int number. Check if the number is a palindrome. (A palindrome number read backwards has the same value)
# Example of a palindrome numbers: 123454321, 999, 1598951

for i in range(1, 11):
    for j in range(i, 11):
        print(f"{i}X{j}={i*j}")
    print()

