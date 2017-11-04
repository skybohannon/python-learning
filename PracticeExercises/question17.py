# Question 17
# Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

totalAmount = 0
userInput = "D 500 W 200 D 100 W 200"
x = tuple(userInput.split(" "))
print(x)
operation = x[0]
amount = int(x[1])

if operation == "D":
    amount += totalAmount
    print(totalAmount)
elif operation == "W":
    amount -= totalAmount
else:
    pass

print(str(totalAmount))