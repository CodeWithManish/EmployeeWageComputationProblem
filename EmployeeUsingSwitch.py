import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
wage_per_day = 0
part_time_wage_per_day = 0

_wage = {
    0: {'attendance': 'Absent', 'wage': 0, 'worked_hr': 0},
    1: {'attendance': 'Present', 'wage': wage_per_day, 'worked_hr': FULL_DAY_HOUR},
    2: {'attendance': 'part-time', 'wage': part_time_wage_per_day, 'worked_hr': PART_TIME_HOUR}
}

attendance = random.randint(0, 2)
print('Wage according to attendance :', _wage.get(attendance))