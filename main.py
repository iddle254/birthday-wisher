import smtplib
import datetime as dt
from pandas import read_csv
import datetime as dt
import smtplib
from random import randint

MY_MAIL = "mossmotaroki@yahoo.com"
MY_PASSWORD = "*****"

today = (dt.datetime.now().month, dt.datetime.now().day)

mails = read_csv("./birthdays.csv")
