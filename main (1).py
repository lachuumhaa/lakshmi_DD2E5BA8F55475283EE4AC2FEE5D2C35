#  leap year
def isleapyear(year):
    if (year % 4 == 0 and year % 100 == 0) or  year % 400 == 0:
       return true
    else:
       return False
year=int(input("enter the year:"))
if isleapyear(year):
 print (year,"is a leap year")
else:
 print(year,"is not a leap year")
