from utils.dates import start_day_number, get_week_day_name, days_in_month


def print_month_calendar(mm,yy):
    start_day =  start_day_number(1,mm,yy)
    month_days = days_in_month(mm,yy) 
    i = 1
    print('|',end='')
    for x in range(7):
        print(get_week_day_name(x)[0:3],end='\t|')
    print()
    while i < month_days:
        print('|', end='')
        for col in range(7):
            if i==1 and col< start_day:
                print('\t',end='')
            elif(i<=month_days):
                print(f'{str(i)}\t', end='')
                i+=1
            print('|',end='')
        print()