

from datetime import datetime, timedelta


def conv_date_to_str(date):
    return "{0:04}-{1:02}-{2:02}T00:00:00Z".format(date.year, date.month, date.day)


def get_date_string_list(date, verbose=False):
    date_str_list = list()

    #get_todays_date
    if date == "TODAY":
        date = datetime.now()


    day_num = date.weekday()
    if verbose:
        print(date)
        print(day_num)
    #always get beg and end as fri - fri
    back = (day_num - 4)%7
    forward = (4 - day_num)%7
    if back == 0:
        back = 7

    beg_date = date - timedelta(days=back)
    end_date = date + timedelta(days=forward)
    date_str_list.append(conv_date_to_str(beg_date))
    date_str_list.append(conv_date_to_str(end_date))
    return date_str_list




#   0,   1,   2,     3,   4,   5,   6,
# mon, tue, wed, thurs, fri, sat, sun