def timeConversion(s):
    hour_difference = 12
    time = s.split(":")
    hour = time[0]
    minutes = time[1]
    seconds = time[2][:2]
    time_of_day = time[2][2:]

    if time_of_day == "AM" and hour == "12":
        return f"00:{minutes}:{seconds}"
    elif time_of_day == "AM":
        return f"{hour}:{minutes}:{seconds}"
    elif time_of_day == "PM" and hour == "12":
        return f"12:{minutes}:{seconds}"
    else:
        return f"{str(int(hour) + hour_difference)}:{minutes}:{seconds}"


print(timeConversion("06:40:03AM"))
