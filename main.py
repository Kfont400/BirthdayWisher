import smtplib
import datetime as dt
import pandas as pd
import random
import os

my_email = "kai2flie@gmail.com"
password = #Password

data = pd.read_csv("birthdays.csv")
df = {'name':'Kali', 'email':'keilandraije@icloud.com', 'year':2022, 'month':5, 'day':25}
data = data.append(df, ignore_index = True)

now = dt.datetime.now()
month = now.month
day = now.day
bday_list = data.loc[(data["month"] == month) & (data['day'] == day)]

path = f"F:/Python/Projects/BirthdayWisher/birthday-wisher-extrahard-start/LetterTemplates/letter_{random.randint(1,3)}.txt"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    for i in range(len(bday_list)):
        with open(path) as file:
            file = file.read()
            personalized_msg = file.replace('[NAME]', bday_list.iloc[i, 0])
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=bday_list.iloc[i, 1], 
            msg=f"Subject:HAPPY BIRTHDAY!!\n\n{personalized_msg}"
        )
