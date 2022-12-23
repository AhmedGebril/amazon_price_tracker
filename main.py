import time
from scraping import Scrabing
import twilio
from datetime import datetime, timedelta
import smtplib
from unidecode import unidecode
from tkinter import *


def radio_choice():
    state = radio_state.get()
    if state == 'Everyday':
        day = (24 * 60 * 60)
        start(day)
    elif state == 'Everyweek':
        week = (6 * 24 * 60 * 60)
        start(week)

def start(waiting_time):
    BUY_PRICE = price.get()
    now_time = datetime.now().strftime("%I:%M %p")
    print(BUY_PRICE)
    if now_time == "03:53 AM":
        searching = Scrabing(url=url_Entry.get())
        price_without_tag = searching.Get_Price()
        print(price_without_tag)
        product_title = searching.Get_Title().strip()
        print(unidecode(product_title))
        if price_without_tag <= float(BUY_PRICE):
            message = f"{product_title} is now {BUY_PRICE} or less."
            print("message sent.")
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                # Enter your Private Email and password here.
                connection.login(user=, password=)
                connection.sendmail(from_addr="ahmedgebril1889@gmail.com",
                                    to_addrs="ahmedgebril1889@gmail.com",
                                    msg=f"Subject:\n\n{unidecode(product_title)} is now {BUY_PRICE} or less.")
        else:
            print('still not the right price')
    else:
        print('still waiting for the right time')
        time.sleep(waiting_time)



window = Tk()
window.title("price tracker")
window.geometry("400x250")

label1 = Label(text="Welcome to Amazon Tracker App.")
label1.grid(row=0, column=1, columnspan=3)

url_label = Label(text="Enter Your url")
url_label.grid(row=4, column=0)

url_Entry = Entry(width=30)
url_Entry.grid(row=4, column=1)

price_label = Label(text="price you want to track")
price_label.grid(row=5, column=0)

price = IntVar()
price_Entry = Entry(width=30, textvariable=price)
price_Entry.grid(row=5, column=1)

track_btn = Button(text="Track Price", command=radio_choice, highlightthickness=1)
track_btn.grid(row=6, column=1)

radio_state = StringVar()
radio1 = Radiobutton(variable=radio_state, text="Everyday", value='Everyday')
radio2 = Radiobutton(variable=radio_state, text="Everyweek", value='Everyweek')
radio1.grid(row=7, column=0)
radio2.grid(row=7, column=1)

window.mainloop()
