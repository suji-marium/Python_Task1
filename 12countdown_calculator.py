from datetime import date


y1=int(input("Enter the year1:"))
m1=int(input("Enter the month1:"))
d1=int(input("Enter the day1:"))

y2=int(input("Enter the year2:"))
m2=int(input("Enter the month2:"))
d2=int(input("Enter the day2:"))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

diff=date2-date1
print("Amount of time between dates", date1,"and",date2, "is",diff.days)

