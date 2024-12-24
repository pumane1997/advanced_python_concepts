import yagmail
import pandas as pd

df = pd.read_excel('people.xlsx')

# print(df.head())



for index, row in df.iterrows():
    # print(row)
    # print(row['email'])
    # email = yagmail.SMTP(user="matecolab01@gmail.com", password='tmpazmytpehunmar')
    # email.send(to=row['email'],
    #         subject=f"your {row['interest']} news for today",
    #         contents=f"Hi {row['name']},\n See what's on about {row['interest']} today \n Pratik")
    pass

from datetime import date, timedelta

# Get today's date
today = date.today()-timedelta(days=1)

# Print the date
print(today)  