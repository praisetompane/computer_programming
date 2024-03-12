"""
    Context:
        Given
            12 hour time
    Objective:
        Write algorithm to convert it to 24 hour time

    Assumptions:
        Valid 12 hour time will be provided
        1 time string at a time
        12 hour time is:
            4 digits long
            Format : HH:MM:AM/PM
    Constraints:    
        None
    
    Example:
        input     output
        01:00PM = 13:00
        11:00AM = 11:00
        11:00PM = 23:00
        special cases:
        12:00AM = 00:00
        12:00PM = 12:00
    
    Flow:
        hour_difference = 12
        hour = substring first two
        minutes = subtring 2 and 3
        time_of_day = substring 4 and 5

        if time_of_day == AM
            if hour == 12
                return 00: minutes
            return hour : minutes
        else
            return hour + hour_difference : minutes

    Performance
        Time = O(1)
            same amount of time independent of input
        Space = O(1)
            store internal variables

"""


def format_time(hour, minutes):
    return "%s:%s" % (hour, minutes)


def twelve_hour_time_to_twenty_four(time):
    hour_difference = 12
    hour = time[0:2]
    minutes = time[3:5]
    time_of_day = time[5:]

    if hour == "12":
        if time_of_day == "AM":
            return format_time("00", minutes)
        if time_of_day == "PM":
            return format_time(hour, minutes)
    if time_of_day == "AM":
        return format_time(hour, minutes)
    else:
        return format_time(str(int(hour) + int(hour_difference)), minutes)


print(twelve_hour_time_to_twenty_four("01:01PM"))  # = 13:01
print(twelve_hour_time_to_twenty_four("11:10AM"))  # = 11:10
print(twelve_hour_time_to_twenty_four("11:50PM"))  # = 23:50
print(twelve_hour_time_to_twenty_four("12:40AM"))  # = 00:40
print(twelve_hour_time_to_twenty_four("12:35PM"))  # = 12:35
