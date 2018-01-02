name = 'bigmuug'
numarray = [34, 23, 26, 7347, 734, 32, 15, 62, 151, 636, 34, 6]
age = 23

print(name[4:])

# .format usage
print("""Monday {5}, 
Tuesday {4},
Wednesday {2},
Thursday {7},
Friday {8},
Saturday {2},
Sunday {5}""".format(34, 23, 26, 7347, 734, 32, 15, 62, 151, 636, 34, 6))
print('')
for i in range(1, 12):
    print("No. {0:<2} squared is {1:4} and cubed is {2:4}" .format(i, i**2, i**3))
print('')
# learn what tuples are and how to format with arrays


# % usage
print('My age is %d %s, %d %s' % (age, "years", 6, "months"))
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))
