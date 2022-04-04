import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

attendance = random.randint(0, 2)
if attendance == 1:     # check employee is present
    print("Employee is present")
    wage_per_day = WAGE_PER_HOUR * FULL_DAY_HOUR
    print('Wage per day {}'.format(wage_per_day))
elif attendance == 2:   # check employee present for partTime
    print("Employee present for PartTime")
    part_time_wage_per_day = WAGE_PER_HOUR * PART_TIME_HOUR
    print('Part time wage per day {0}'.format(part_time_wage_per_day))
else:
    print("Employee is Absent")
