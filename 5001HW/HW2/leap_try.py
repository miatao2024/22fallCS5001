def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__  == "__main__":
    year = int(input("Please enter a year greater than 0:"))
    if is_leap_year(year):
        print(f'The year {year} is a leap year')
    else:
        print(f'The year {year} is not a leap year')

    

