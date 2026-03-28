import openpyxl
from openpyxl import Workbook
import customtkinter as ctk
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkmb
book=Workbook()
sheet=book.active
sheet['A1']="username"
sheet['B1']="password"
def submit():
    username=entry1.get()
    password=entry2.get()
    sheet.append([username,password])
    book.save(filename='data.xlsx')
    print("data saved")
def clear():
    entry1.delete(0,"end")
    entry2.delete(0,"end")    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app=ctk.CTk()
app.geometry("400x400")
app.title("Log In UI")
frame=ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill="both",expand=True)
entry1=ctk.CTkEntry(master=frame,placeholder_text="username")
entry1.pack(pady=12,padx=10)
entry2=ctk.CTkEntry(master=frame,placeholder_text="password",show="*")
entry2.pack(pady=12,padx=10)
button=ctk.CTkButton(master=frame,text="submit",command=submit)
button.pack(pady=10,padx=10)
button=ctk.CTkButton(master=frame,text="clear",command=clear)
button.pack(pady=10,padx=10)
app.mainloop()