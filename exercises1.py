# Exercise 2: Write a program that uses input to prompt a user for their
# name and then welcomes them.

# name = input('enter your name: ')
# print('Welcome ' + name)

# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.

# haours = int(input('Enter hours: '))
# rates = int(input('enter rates: '))
# pays = haours * rates

# print('Gajih yang harus dibayar $', pays)

# Exercise 5: Write a program which prompts the user for a Celsius tem-
# perature, convert the temperature to Fahrenheit, and print out the
# converted temperature.

# rumusnya (°C × 9/5) + 32 = °F

# print('conversi celcius ke fahrenhit')

# celcius = float(input('masukan nilainya: '))

# fahrenhit = (celcius * 9/5) + 32

# print('hasilnya: ', fahrenhit)

# conversi sirup ke drop

smallest = None
print('Before: ', smallest)
for iterver in [3, 41, 12, 9, 74, 15]:
    if smallest is None or iterver < smallest:
        smallest = iterver
        break
    print('loop', iterver, smallest)

print('smallest: ', smallest)
