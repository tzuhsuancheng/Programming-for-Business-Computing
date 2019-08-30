import datetime

weekday_counter = [0] * 7   # for answer

while True: # loop until "BREAK"
    input_str = input()
    if input_str == "BREAK":    # End of input, output the answer
        for weekday in range(7):
            print(str(weekday + 1) + " " + str(weekday_counter[weekday]))
        break
    birthday = input_str.split('/') # split by '/'
    if len(birthday) != 3:  # if true, means input is not "x/x/x"
        print("DATA_ERROR")
        break
    try:    # check for number. Year, month, day should all be number
        year = float(birthday[0])
        month = float(birthday[1])
        day = float(birthday[2])
    except:
        print("DATA_ERROR")
        break

    # convert to integer
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    if year != year_int or month != month_int or day != day_int: # if not equal, there is a fraction part, which is invalid.
        print("DATA_ERROR")
        break
    try:
        birthday_datetime = datetime.datetime(year_int, month_int, day_int) # check for valid date. Days in a month, leap year, etc.
    except:
        print("DATA_ERROR")
        break

    
    weekday_counter[birthday_datetime.weekday()] += 1   # increase the corresponding weekday count