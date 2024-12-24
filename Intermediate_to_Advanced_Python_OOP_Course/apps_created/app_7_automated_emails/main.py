import pandas as pd
import yagmail
from news import Newsfeed
from datetime import date, timedelta


while True: # the scripts executes continuously

    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 45:

        data = pd.read_excel('people.xlsx')
        for index, row in data.iterrows():
            news = Newsfeed(
                            interests=row['interest'], 
                            from_date=(date.today()-timedelta(days=1)),
                            to_date=(date.today()-timedelta(days=1))
                            )
            email = yagmail.SMTP(user="matecolab01@gmail.com", password='tmpazmytpehunmar')
            email.send(to=row['email'],
                    subject=f"your {row['interest']} news for today",
                    contents=f"Hi {row['name']}, \
                            \n See what's on about {row['interest']} today  \
                            \n {news.get()}  \
                            \n Pratik")

# python ./main.py