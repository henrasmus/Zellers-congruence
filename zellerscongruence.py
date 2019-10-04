"""
Rasmus Hen
Windows 10
"""

maxdays = [31,28,31,30,31,30,31,31,30,31,30,31]
weekday = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

#Year
while True:
    year = input("Year: ")
    if not year.isdigit():
        print("Out of allowed range 1583 – 9999")
        continue
    year = int(year)
    if year < 1583 or year > 9999:
        print("Out of allowed range 1583 – 9999")
        continue
    else:
        break

#Checks if it's leap year and if that's the case: Changes February to 29 days
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    maxdays[1] = 29

#Month
while True:
    month = input("Month: ")
    if not month.isdigit():
        print("Out of allowed range 1 – 12")
        continue
    month = int(month)
    if month < 1 or month > 12:
        print("Out of allowed range 1 – 12")
        continue
    else:
        break

#Day
f = maxdays[month - 1]
while True:
    day = input("Day: ")
    if not day.isdigit():
        print("Out of allowed range 1 –",f)
        continue
    day = int(day)
    if day < 1 or day > f:
        print("Out of allowed range 1 –",f)
        continue
    else:
        break

#Changes January and February to the year before
if month == 1 or month == 2:
    month += 12
    year -= 1

#Zeller's congruence
zeller = ( day + 13*(month+1)//5 + year + year//4 - year//100 + year//400 ) % 7 

print("It is a",weekday[zeller])
