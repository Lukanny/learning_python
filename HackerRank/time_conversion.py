

def timeConversion(s):
    hours_minutes_seconds = s.split(":")
    hours = int(hours_minutes_seconds[0])
    seconds = hours_minutes_seconds[-1][:-2]
    day_period = hours_minutes_seconds[-1][-2:]
    if day_period == "PM":
        if hours < 12:
            hours += 12
    else:
        if hours == 12:
            hours = str("00")
        elif hours < 12:
            hours = "0" + str(hours)
    hours_minutes_seconds[0] = str(hours) if type(hours) == int else hours
    hours_minutes_seconds[-1] = seconds
    converted_time = ":".join(hours_minutes_seconds)
    return converted_time

if __name__ == '__main__':
    input = "06:40:03AM"
    result = timeConversion(input)
    print(result)