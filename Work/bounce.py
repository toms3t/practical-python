# bounce.py
#
# Exercise 1.5
val = 100
for num, y in enumerate(range(10), 1):
    val = val * .6
    print(num, round(val, 4))
