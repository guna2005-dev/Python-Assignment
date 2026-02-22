from datetime import date
def question4():
    day = int (input(" Enter birth day:"))
    month = int (input(" Enter birth month:"))
    year = int (input(" Enter birth year:"))
    
    birth_date = date(year, month, day)
    today = date.today()
    
    age_days = (today - birth_date). days
    age_years = age_days // 365


    print("\nExtact Age:")
    print("Age in Years:", age_years)
    print("Age in Days:", age_days)

question4()
    

