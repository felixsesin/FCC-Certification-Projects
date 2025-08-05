# Solution to "Build A Time Calculator Project", 08/04/2025

# INSTRUCTIONS: Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

# MORE INFO: https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-time-calculator-project/build-a-time-calculator-project

# __________________  PROGRAM STARTS BELOW  __________________

def add_time(start, duration, wkdy=None):
    # set up list for days of the week
    if wkdy != None:
        wkdy = wkdy.capitalize()
    wkdys = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # convert input time data from string to integer
    mi0 = int(start.split()[0][-2:])
    if start.split()[1] == 'AM':
        hr0 = int(start.split()[0][:-3])
    elif start.split()[1] == 'PM':
        hr0 = 12 + int(start.split()[0][:-3])
    mi1 = int(duration[-2:])
    hr1 = int(duration[:-3])

    # minute arithmetic
    mi = f'{(mi0 + mi1) % 60}'
    if int(mi) < 10:
        mi = f'0{(mi0 + mi1) % 60}'
    hr_carry = (mi0 + mi1 - int(mi)) / 60

    # hour, day, and AM/PM arithmetic
    hr = (hr0 + hr1 + hr_carry) % 24
    day = (hr0 + hr1 + hr_carry - hr) / 24
    em = ''
    if hr == 0:
        hr = 12
        em = 'AM'
    elif 0 < hr < 12:
        em = 'AM'
    elif hr == 12:
        em = 'PM'
    elif 12 < hr:
        hr = int(hr - 12)
        em = 'PM'
    
    # day of the week arithmetic
    if wkdy != None:
        i = wkdys.index(wkdy) + int(day)
        wkdyy = wkdys[i%7]
    else:
        wkdyy = wkdy
    if wkdyy != None:
        if day == 0:
            return f'{int(hr)}:{mi} {em}, {wkdyy}'
        elif day == 1:
            return f'{int(hr)}:{mi} {em}, {wkdyy} (next day)'
        else:
            return f'{int(hr)}:{mi} {em}, {wkdyy} ({int(day)} days later)'
    if wkdyy == None:
        if day == 0:
            return f'{int(hr)}:{mi} {em}'
        elif day == 1:
            return f'{int(hr)}:{mi} {em} (next day)'
        else:
            return f'{int(hr)}:{mi} {em} ({int(day)} days later)'

** end of main.py **

