def check_leap_year(year):
    return year % 400==0 or (year%4==0 and year % 100!=0) 


def days_in_month(month,year):
    if month==2:
        return 28 + int(check_leap_year(year))
    
    elif(month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30
        

def get_week_day_name(index):
    if(index == 0): return 'Sunday'
    if(index == 1): return 'Monday'
    if(index == 2): return 'Tuesday'
    if(index == 3): return 'Wednesday'
    if(index == 4): return 'Thursday'
    if(index == 5): return 'Friday'
    if(index == 6): return 'Saturday'
    return ''


def date_value(day,month,year):
    days_elapsed = 0
    y = year - 1
    days_elapsed = y*365 + y//4 - y//100 + y//400

    m = 1
    while(m<month):
        days_elapsed += days_in_month(m, year)
        m+=1
    days_elapsed +=day

    return days_elapsed


def start_day_number(dd,mm,yy):
    ref_date = date_value(1,1,1978)
    inpUt_date = date_value(dd,mm,yy)
    diff =  (inpUt_date - ref_date)%7
    return diff

def week_day_name(diff):
    return get_week_day_name(diff)

    