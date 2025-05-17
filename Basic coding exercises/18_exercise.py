# 18. Check if a given year is a leap year

def is_leap_year(year):
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 != 0:
                print("Leap year.")
            else:
                print("Not a leap year. ")
        else:
            print("Leap year.")
    else:
        print("Not a leap year.")


year = int(input("Enter a year: "))
is_leap_year(year)
