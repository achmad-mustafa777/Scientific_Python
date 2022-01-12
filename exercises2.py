# Exercise 6: Rewrite your pay computation with time-and-a-half for over-
# time and create a function called computepay which takes two parameters
# (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# def computepay(hours, rate):
#     if hours > 40:
#         print('over time, give bonus $1.5')
#         pay = (hours * rate) + 1.5

#     else:
#         print('Gajih reguler')
#         pay = hours * rate

#     total = 'upah kariayawan yang harus di bayar $ '

#     return print(total + str(pay))


# jam = float(input('Enter total jam kerja: '))
# upah = float(input('Enter upah perjam: '))

# computepay(jam, upah)


# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.


# Score     # Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       E
# 41          F

def computegrade(score):
    if score >= 0.9 and score < 1.0:
        grade = 'grade A'
    elif score >= 0.8 and score < 0.9:
        grade = 'grade B'
    elif score >= 0.7 and score < 0.8:
        grade = 'grade C'
    elif score >= 0.6 and score < 0.7:
        grade = 'grade D'
    elif score < 0.6:
        grade = 'grade E'

    else:
        grade = 'Bad score'

    return grade


skor = float(input('Enter score terkini: '))

print(computegrade(skor))
