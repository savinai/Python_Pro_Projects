import yagmail
import pandas as pd
import datetime
from news import NewsFeed


df = pd.read_excel('people.xlsx')


def send_email():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday.strftime('%Y-%m-%d'))
    email = yagmail.SMTP(user='xxxxx@gmail.com', password='******') # insert the gmail id and password
    email.send(to=row['email'],
               subject=f'Your {row["interest"]} news for today',
               contents=f'Hi, {row["name"]},\nSee what\'s on about {row["interest"]} today. {news_feed.get()}\nYour Friend ',
               attachments='design.txt')


while True:
    if datetime.datetime.now().hour == 23 and datetime.datetime.now().minute == 12:
        for index, row in df.iterrows():
            if row['name'] == "":
                break

            send_email()

    time.sleep(60)
