def add_time(start, duration, day_week=None):
    time = start.split()[0]
    Am_pm = start.split()[1]
    time_h = time.split(":")[0]
    time_m = time.split(":")[1]
    duration_h = duration.split(":")[0]
    duration_m = duration.split(":")[1]
    sum_h = int(time_h) + int(duration_h)
    sum_m = int(time_m) + int(duration_m)

    if sum_m//60 != 0:
        sum_h += sum_m // 60
        sum_m = sum_m % 60

    count = 0
    n = 0
    sum_h_full = 0
    if sum_h//24 != 0:
        n += sum_h//24
        sum_h_full = sum_h%24
    else:
        sum_h_full = sum_h


    if sum_h_full//12 ==0:
        new_Am_pm = Am_pm
    else:
        sum_h_full = sum_h_full%12
        if sum_h_full == 0:
            sum_h_full = 12
        if Am_pm == "AM":
            new_Am_pm = "PM"
        else:
            new_Am_pm = "AM"
            n += 1
    updated_time = str(sum_h_full).strip() + ":" + str(sum_m).strip().zfill(2)
    if n == 1:
        after = " (next day)"
    elif n > 1:
        after = " (" + str(n) + " days later)"
    else:
        after = ""

    if day_week is not None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day in days:
            if str(day_week).lower() == day.lower():
                i = days.index(day)
                break
        which_day = i + n
        if which_day > len(days):
            which_day = which_day%len(days)
        expected_day = days[which_day]
        new_time = updated_time + " " + new_Am_pm + ", " + expected_day + after
    else:
        new_time = updated_time + " " + new_Am_pm + after
    return new_time



print(add_time("6:30 PM", "205:12"))
