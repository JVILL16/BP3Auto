from datetime import date, datetime
    
#########################################
# Getting the month, day, and time currently
#########################################
def getterMonth():
    today = date.today()
    month_day = today.strftime('%m%d')
    return month_day

###########################################
# Determining for email if it is morning or afternoon
###########################################
def getterGreet():
    dt = datetime.now()
    hour_time = dt.time().hour
    if hour_time < 12:
        greet = 'Good morning,\n'
    else:
        greet = 'Good afternoon,\n'
    return greet
    
#######################################
# Getting timestamp for each BP3 generated
#######################################
def timestamp():
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    date_time = datetime.fromtimestamp(ts)
    str_date_time = date_time.strftime("%m-%d-%Y, %H:%M:%S")
    return str_date_time

def logging(type):
    log_file = open('assets/logging.log', 'a+')
    with log_file as file:
        file.seek(0)
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")
        file.write(type+": "+timestamp())

def ERC_STOP_time():
    dir_name = 'U:/DMV'
    # dir_name = '//itgcubs/Itgcubs$/prodcubsdata/load/FF_Elizabeth_River_Crossings/Output'
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    date_time = datetime.fromtimestamp(ts)
    str_date_time = date_time.strftime("%m/%d/%Y")
    year = date_time.strftime("%Y")
    return dir_name,str_date_time,year
    