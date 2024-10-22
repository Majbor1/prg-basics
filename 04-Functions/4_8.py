def time_string(hours, minutes, time_format):
    minutes = str(minutes)
    if time_format == '24':
        result = str(hours) + ":" + minutes
    elif time_format == '12':
        if hours < 12:
            hours -= 12
            hours = str(hours)
            result = hours + ":" + minutes + "pm"
        else:
            result = str(hours) + ":" + minutes + "am"
    return result

print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '12'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))