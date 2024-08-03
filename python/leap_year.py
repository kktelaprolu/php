def leap_year(year):
    if year % 100 == 0 | year % 400 == 0 & year % 4 ==0:
        return True
    else:
        return False

year=int(input("Enter the Year:"))
print(leap_year(year))