# format_ft_time.py
import time
import datetime

PRINT_FORMAT = (
    'Seconds since {month} {day}, {year}: {seconds} or'
    ' {scientific_notation} in scientific notation'
)


def check_valid_date(month, day, year):
    if month < 1 or month > 12:
        print("Invalid month")
        return
    if day < 1 or day > 31:
        print("Invalid day")
        return
    if year < 1 or year > 9999:
        print("Invalid year")
        return
    if month == 2 and (year % 4 == 0 and day > 29 or year % 4 != 0 and day > 28):
        print("Invalid day for February")
        return
    if month in [4, 6, 9, 11] and day > 30:
        print("Invalid day for this month")
        return


def calculate_difference(current_time, month, day, year):
    current_year = current_time.tm_year
    current_month = current_time.tm_mon
    current_day = current_time.tm_mday
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec
    current_date = datetime.datetime(
        current_year,
        current_month,
        current_day,
        current_hour,
        current_minute,
        current_second)
    given_date = datetime.datetime(year, month, day, 0, 0, 0)
    difference = given_date - current_date
    seconds = difference.total_seconds()
    scientific_notation = "{:.2e}".format(seconds)
    return seconds, scientific_notation


def main(month=1, day=1, year=2021, *args):
    current_time = time.localtime()
    check_valid_date(month, day, year)
    seconds, scientific_notation = calculate_difference(
        current_time,
        month,
        day,
        year)
    month_in_words = datetime.date(1900, month, 1).strftime('%B')
    print(PRINT_FORMAT.format(
        month=month_in_words,
        day=day,
        year=year,
        seconds=seconds,
        scientific_notation=scientific_notation))
    current_month_in_words = datetime.date(
        1900,
        current_time.tm_mon, 1).strftime('%B')
    current_day = current_time.tm_mday
    current_year = current_time.tm_year
    print(f"{current_month_in_words} {current_day} {current_year}")


if __name__ == "__main__":
    while True:
        try:
            month = 1
            day = 1
            year = 1970
            main(month, day, year)
            break
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
