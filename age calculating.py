##calculating age by asking user to enter the birth year
import datetime
Year_of_birth = int(input("In which year you took birth:- "))
current_year = datetime.datetime.now().year
Current_age = current_year - Year_of_birth
print("Your current age is ",Current_age)

#practiced for the question to print date from the date and time
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


