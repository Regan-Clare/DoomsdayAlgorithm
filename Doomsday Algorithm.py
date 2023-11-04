century = {24: 2, 23: 3, 22: 5, 21: 0, 20: 2, 19: 3, 18: 5, 17: 0, 16: 2, 15: 3}
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
number_to_day = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 0: 'Sunday'}

# CENTURY/YEAR CALCULATION
while True:
    try:
        year = int(input("What is the year? Note: in the form 1923, 1602, 2487... and only dates from 1582 to 2499"))
        if not (1582 <= year <= 2499):
            raise ValueError("Year is not within the specified range.")
        break  # Exit the loop if input is valid
    except ValueError as e:
        print(e)

# century
century_str = str(year)  # Convert the year to a string
first_two_digits = int(century_str[:2])  # getting century
century_code = century[first_two_digits]  # getting corresponding century code

# year
numerical_year = year % 100  # last two digits of year
leap_years = numerical_year // 4  # ignoring remainders

# DOOMSDAY FOR THAT YEAR
doomsday = century_code + numerical_year + leap_years

# MONTH & DAY CALCULATION
while True:
    try:
        month = str(input("What is the month? Note: in the form Jan, Feb, Mar..."))
        if month not in months:
            raise ValueError("Invalid month name.")
        break  # Exit the loop if input is valid
    except ValueError as e:
        print(e)

if numerical_year / 4 == int:  # if numerical year has no remainder => if year is a leap year
    months_doomsdays = {'Jan': 4, 'Feb': 29, 'Mar': 14, 'Apr': 4, 'May': 9, 'Jun': 6, 'Jul': 11, 'Aug': 8, 'Sep': 5,
                        'Oct': 10, 'Nov': 7, 'Dec': 12}
    max_days_in_month = {'Jan': 31, 'Feb': 29, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31,
                         'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
else:  # if not on a leap year
    months_doomsdays = {'Jan': 3, 'Feb': 28, 'Mar': 14, 'Apr': 4, 'May': 9, 'Jun': 6, 'Jul': 11, 'Aug': 8, 'Sep': 5,
                        'Oct': 10, 'Nov': 7, 'Dec': 12}
    max_days_in_month = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31,
                         'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}

while True:
    try:
        day = input("What is the day? Note: in the form 9, 18, 25...")
        day = int(day)
        if not (1 <= day <= max_days_in_month[month]):  # Check if it's at least 1 digit long and at most 2 digits long
            raise ValueError("Day should be at least 1 digit long and at most 2 digits long.")
        break  # Exit the loop if input is valid
    except ValueError as e:
        print(e)

month_doomsday = months_doomsdays[month]  # special doomsday for specific month

difference_to_doomsday = month_doomsday - day  # taking day, and finding difference to month doomsday
numerical_day_of_week = (difference_to_doomsday + doomsday) % 7  # getting into 0-6 form (days of week)

actual_day_of_date = number_to_day[numerical_day_of_week]  # presenting day
print(actual_day_of_date)