from datetime import datetime, timedelta

def get_dates_in_interval(start_date, end_date):
    if start_date is None or end_date is None:
        return None
    
    start_dt = datetime.strptime(start_date, "%m/%d/%Y")
    end_dt = datetime.strptime(end_date, "%m/%d/%Y")
    interval = (end_dt - start_dt).days

    if interval < 0:
        return None

    dates = []  
    for date in range(interval + 1):
        result = start_dt + timedelta(days=date)
        dates.append(str(result.strftime("%m/%d/%Y")).lstrip('0'))
        
    return dates


def get_default_date_data(start_date, end_date, default_value):
    dates = []
    interval = get_dates_in_interval(start_date, end_date)
    if interval is None:
        return dates
    dates.extend([ {'date': i, 'participants':default_value} for i in interval ])
    
    print(dates)
    return dates

