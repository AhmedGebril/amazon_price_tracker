from scraping import Scrabing
import twilio
import datetime
import smtplib
from unidecode import unidecode
from tkinter import *

def start():
    BUY_PRICE=price.get()
    now_time = datetime.datetime.now().strftime("%I:%M %p")
    print(now_time)
    if now_time == "08:00 AM":
        searching = Scrabing()
        price_without_tag = searching.Get_Price()
        product_title = searching.Get_Title().strip()
        print(unidecode(product_title))
        if price_without_tag <= float(BUY_PRICE):
            message = f"{product_title} is now {BUY_PRICE} or less."
            print("message sent.")
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user="ahmedgebril1889@gmail.com", password="gatcrnogtbtxbkdh")
                connection.sendmail(from_addr="ahmedgebril1889@gmail.com",
                                    to_addrs="ahmedgebril1889@gmail.com",
                                    msg=f"Subject:\n\n{unidecode(product_title)} is now {BUY_PRICE} or less.")


window = Tk()
window.title("price tracker")
window.geometry("400x250")

label1 = Label(text="Welcome to Amazon Tracker App.")
label1.grid(row=0,column=1,columnspan=3)

url_label=Label(text="Enter Your url")
url_label.grid(row=4,column=0)

url_Entry=Entry(width=30)
url_Entry.grid(row=4,column=1)

price_label=Label(text="price you want to track")
price_label.grid(row=5,column=0)

price=IntVar()
price_Entry=Entry(width=30,textvariable=price)
price_Entry.grid(row=5,column=1)

track_btn=Button(text="Track Price",command=start,highlightthickness=1)
track_btn.grid(row=6,column=1)

radio_state=StringVar()
radio1=Radiobutton(variable=radio_state,text="Everyday",value='9:00 PM')
radio2=Radiobutton(variable=radio_state,text="Everyweek",value='10:00 PM')
radio1.grid(row=7,column=0)
radio2.grid(row=7,column=1)


window.mainloop()
