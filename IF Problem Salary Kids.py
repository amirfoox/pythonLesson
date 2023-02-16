###
# Given the 'gross' salary of a person, calculate the "net".
# Here are the constraints:
# 1. if the gross is less than 1000, then the income tax is 10%
# 2. if the gross is less than 2000, then the income tax is 12%
# if the gross is less than 4000, then the income tax is 14%
# if the gross is more than 4000, then the income tax is 18%
# if the gross is less than 1000, then the income tax is 10%
# if the gross is less than 2000, every child gets you a tax cut of 1%
# if the gross is more than 2000, every child gets you a tax cut of 0.5%

# Read the "gross" and the number of children
# Print the "net"

# Michael Seletsky's solution:

gross=int(input('What is your gross salary? '))
kids=int(input('How many kids do you have? '))

if gross < 1000:
    tax = 10 - kids
elif gross < 2000:
    tax = 12 - kids
elif gross < 4000:
    tax = 14 - kids / 2
else:
    tax = 18 - kids / 2
if tax < 0:
    tax = 0

net = gross - gross * (tax * 0.01)
print(net)