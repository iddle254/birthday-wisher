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


birthdays_dict = {(row.month, row.day): row for (index, row) in mails.iterrows()}
if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    file_path = f"letter_templates/letter_{(randint(1,3))}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("Angela", "Moss")
        contents = contents.replace("[NAME]", birthday_person["name"].title())
        print(contents)


    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy birthday\n\n{contents}"

        )

