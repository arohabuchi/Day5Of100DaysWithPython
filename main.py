# Date and time

#paring a string into a timzone... co
import  datetime

dt = datetime.datetime.strptime("2023-09-05T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
dtt = datetime.datetime.strptime("2023-09-05T", "%Y-%m-%dT")

# will reformat dt to2023-09-05 08:27:18-05:00
print(dt)#will  print dt
print(dtt)

############################################  Contructing timezone aware datetime #####################################################
from datetime import  datetime, timedelta, timezone

jt= timezone(timedelta(hours=+9))
dt =datetime(2023,1,1,12,0,0,tzinfo=jt)
print(dt)
print(dt.tzname())

############################################ computing time differences #######################################

from datetime import  datetime, timedelta

now = datetime.now()
then = datetime(2023,1,1)
delta = now - then
print(delta)
print(delta.days)
print(delta.total_seconds())

##################################################To get nth number of days before or after a date ############################################

######################## N days after  #########################
import  datetime
def NDayAfter(date_format="%d %B %Y", add_days=122):
    date_n_days_after= datetime.datetime.now() + datetime.timedelta(days=add_days)
    print(date_n_days_after)
    return date_n_days_after.strftime(date_format)

NDayAfter()


######################## N days before  #########################
import  datetime
def NDayBefore(date_format="%d %B %Y", add_days=122):
    date_n_days_before= datetime.datetime.now() - datetime.timedelta(days=add_days)
    print(date_n_days_before)
    return date_n_days_before.strftime(date_format)

NDayBefore()

################################################### some basic date arithmetic-----  ###############################################################
import datetime
today=datetime.date.today()
print(today)
yesterday=today-datetime.timedelta(days=1)
print(yesterday)
tomorrow=today+datetime.timedelta(days=1)
print(tomorrow)

###################################################### sutracting month from a date accurately #############################################################
import calendar
from datetime import date
def monDelta(date, delta):
    m,y = date.month + delta % 12, date.year+((date.month)+delta-1)//12
    if not m:
        m=12
    d = min(date.day, calendar.monthrange(y,m)[1])
    print(d)
    print(m,y)
    print(date.replace(day=d, month=m, year=y))
    return date.replace(day=d, month=m, year=y)
nextMonth = monDelta(date.today(), 1)

########################################### Fuzzy datetime parsing - Extracting datetime out of a text #######################################################################
from dateutil.parser import parse
dtt=parse("today is january 1, 2023 at 8:21:00AM", fuzzy=True)
dt=parse("today is january 1, 2023 at 8:21AM", fuzzy=True)
print(dtt)
print(dt)

##################################################### Iterate over dates ###################################################################
import datetime
dayDelta = datetime.timedelta(days=1)

startDate= datetime.date.today()
endDate = startDate + 7*dayDelta
for i in range((endDate-startDate).days):
    print(startDate+i*dayDelta)

####################################################### Date formating  - Time beteen two date ####################################################################
from datetime import  datetime
a = datetime(2023, 10, 6,0,0,0)
b = datetime(2023, 10, 9,22,59,59)

print((b-a).days)
print((b-a).total_seconds())

######################################################### parsing string to datetime object ######################################
from datetime import  datetime
dString= "Oct 1 2016, 00:00:00"
dFormat="%b %d %Y, %H:%M:%S"
print(datetime.strptime(dString,dFormat))


######################################################## outputting datetime object to string ######################################
from datetime import  datetime
dString= datetime(2016,10,1,0,0,0)
dFormat="%b %d %Y, %H:%M:%S"
print(datetime.strftime(dString,dFormat))

