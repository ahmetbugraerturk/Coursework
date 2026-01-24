import datetime

def parse_date(year_str, month_str, day_str):
    
    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except:
        year = year_str
        month = month_str
        day = day_str
        raise ValueError("Year, month, and day strings must contain integers.")
    else:
        if year < 1900 or year > 2100:
            raise YearRangeError("Year must be between 1900 and 2100.")   
            
    try:
        date = datetime.date(year, month, day)
    except:
        raise ValueError("Invalid date specified.")
    else:
        return str(date)

class YearRangeError(Exception):
    pass
        
    
