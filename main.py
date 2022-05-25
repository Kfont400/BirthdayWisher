import smtplib
import datetime as dt
import pandas as pd
import random
import os

my_email = "kai2flie@gmail.com"
password = "KaiKai0520!"
# 1. Update the birthdays.csv

data = pd.read_csv("birthdays.csv")
df = {'name':'Kali', 'email':'keilandraije@icloud.com', 'year':2022, 'month':5, 'day':25}
data = data.append(df, ignore_index = True)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
bday_list = data.loc[(data["month"] == month) & (data['day'] == day)]
    
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
path = "F:/Python/Projects/BirthdayWisher/birthday-wisher-extrahard-start/LetterTemplates"
os.chdir(path)
corpus = []
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"

        corpus.append(read_text_file(file_path))

bday_letter = random.choice(corpus)
# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    for i in range(len(bday_list)):
        personalized_msg = bday_letter.replace('[NAME]', bday_list.iloc[i, 0])
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=bday_list.iloc[i, 1], 
            msg=f"Subject:HAPPY BIRTHDAY!!\n\n{personalized_msg}"
        )




