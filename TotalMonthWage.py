import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
WORKING_DAY_PER_MONTH = 20
TOTAL_WORKING_HOURS = 100

wage_per_day = 0
part_time_wage_per_day = 0
day_count = 0
total_wage = 0
worked_hours = 0

_wage = {
    0: {'attendance': 'Absent', 'wage': 0, 'worked_hr': 0},
    1: {'attendance': 'Present', 'wage': wage_per_day, 'worked_hr': FULL_DAY_HOUR},
    2: {'attendance': 'part-time', 'wage': part_time_wage_per_day, 'worked_hr': PART_TIME_HOUR}
}

while WORKING_DAY_PER_MONTH > day_count:
    attendance = random.randint(0, 2)
    day_count += 1
    __wage = _wage.get(attendance).get('wage')
    total_wage += __wage
    worked_hours += _wage.get(attendance).get('worked_hr')
    if worked_hours > TOTAL_WORKING_HOURS:
        break

    print('Working day per month {}'.format(total_wage))
    print('Worked hour per month {}'.format(worked_hours))
    print('Worked for {}'.format(day_count))