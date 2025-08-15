import datetime as dt


def age_calculator():
    desired_date = input(
        'Enter the desired date in YYYY-MM-DD format: ').strip().split('-')
    for i in range(len(desired_date)):
        desired_date[i] = int(desired_date[i])
    formatted_date = dt.date(desired_date[0], desired_date[1], desired_date[2])
    difference = dt.date.today() - formatted_date
    return difference.days


print(age_calculator(), 'days')
