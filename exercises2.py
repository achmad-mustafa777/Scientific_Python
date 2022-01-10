# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

# hours = float(input('Enter total jam kerja: '))
# rate = float(input('Enter upah perjam: '))

# if hours > 40:
#     print('over time, give bonus $1.5')
#     pay = (hours * rate) + 1.5

# else:
#     print('Gajih reguler')
#     pay = hours * rate

# print('total gajih yang diperoleh: $', pay)

# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:

# try:
#     hours = float(input('Enter total jam kerja: '))
#     rate = float(input('Enter upah perjam $ '))

#     if hours > 40:
#         pay = (hours * rate) + 1.5
#         print('over time, give bonus $1.5')

#     else:
#         print('Gajih reguler')
#         pay = hours * rate

#     print('total gajih yang diperoleh: $', pay)

# except:
#     print('please masukan angka bro, supaya ndik erorr')

# Exercise 3: Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:

# Score     # Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       E
# 41          F

try:
    score = float(input('Enter score: '))

    if score >= 0.9 and score < 1.0:
        print('grade A')
    elif score >= 0.8 and score < 0.9:
        print('grade B')
    elif score >= 0.7 and score < 0.8:
        print('grade C')
    elif score >= 0.6 and score < 0.7:
        print('grade D')
    elif score < 0.6:
        print('grade E')

    else:
        print('Bad score')
except:
    print('Bad Score, masukan angka kaka')
