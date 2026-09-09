# #Question 1
# def safe_divide(numerator, denominator):
#     try:
#         result = numerator / denominator
#         print(f"The result of {numerator} divided by {denominator} is {result}.")
#     except:
#         print("Error: Division by zero is not allowed.")

# safe_divide(10, 2)
# safe_divide(10,0)

# #Question 2
# import math
# def number1(number):
#     try:
#         result = math.sqrt(number)
#         print(f"The square root of {number} is {result}.")
#     except ValueError:
#         print("Error: Cannot calculate the square root of a negative number.")

# number1(16)
# number1(-4)


# #Question 3
# def compute(number):
#     try:
#         result = number / (number - 5)
#         print(f"The result of {number} divided by {number - 5} is {result}.")
#     except:
#         print("Error: Division by zero is not allowed.")

# compute(10)
# compute(5)