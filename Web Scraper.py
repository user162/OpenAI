import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("Web Scraper")

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Web Scraper', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

label2 = tk.Label(root, text='Enter a URL to scrape:', bg='lightsteelblue2')
label2.config(font=('helvetica', 10))
canvas1.create_window(150, 130, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(150, 160, window=entry1)


def getTable():
    url = entry1.get()
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    df = df[0]
    df.to_csv('webscraper_output.csv', index=False, encoding='utf-8')
    messagebox.showinfo("Success", "Table scraped and saved to webscraper_output.csv")


button1 = tk.Button(text='Scrape Table', command=getTable, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(150, 190, window=button1)

root.mainloop()
