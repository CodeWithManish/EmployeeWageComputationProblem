import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

attendance = random.randint(0, 2)
if attendance == 1:
    print("Employee is present")
    wage_per_day = WAGE_PER_HOUR * FULL_DAY_HOUR
    print('Wage per day {}'.format(wage_per_day))
else:
    print("Employee is Absent")
