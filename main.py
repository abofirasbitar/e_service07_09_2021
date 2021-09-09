from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


# =========================== variables ===========================================

# =========================== Functions ===========================================
def donothing():
    pass
root=Tk()
root.configure(background="#e1d8b2")
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry(("%dx%d+0+0") % (width_value,height_value))
root.title("أوفاكس E Service")
# root.iconbitmap(r'scanner.ico')
message_bar_frame=Frame(root,background="#e1d8b2",bd=5,padx=2,pady=5,relief=RIDGE)
message_bar_frame.grid(row=0,column=0,columnspan=1)
messages_bar_label=Label(root,width=200,height=2,text="Hello evry one ")
messages_bar_label.grid(row=0,column=0,columnspan=2)
search_frame=Frame(root,bd=5,width=800,height=00,padx=2,pady=5,relief=RIDGE)
search_frame.grid(row=1,column=1)
workframe=Frame(root,background="#e1d8b2",bd=5,width=800,height=00,padx=2,pady=5,relief=RIDGE)
workframe.grid(row=2,column=0)

entryframe=Frame(workframe,background="#e1d8b2",bd=1,height=00,padx=2,pady=5,relief=RIDGE)
entryframe.grid(row=0,column=1,columnspan=1)


listframe=Frame(workframe)
#listfram.geometry=("600x400")
listframe.grid(row=0,column=0,columnspan=1,pady=50)
# e = Entry(listfram, textvariable=sv,bd=3,width=40)
e = Entry(listframe,font=('tahoma',12,'bold'),bd=2,width=40,justify=LEFT,show="Enter your user name...")
e.grid(row=0,column=0,pady=20)

entry_1=Entry(entryframe,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
entry_2=Entry(entryframe,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
entry_3=Entry(entryframe,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
# countrylist=ttk.Combobox(entryframe,font=('tahoma',12,'bold'),width=39,justify=RIGHT)
#
# city=ttk.Combobox(entryframe,font=('tahoma',12,'bold'),width=39,justify=RIGHT)
#
# # entry_4=Entry(entryframe,textvariable=clientcountry,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
# # entry_5=Entry(entryframe,textvariable=clientcity,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
# entry_6=Entry(entryframe,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
# entry_7=Entry(entryframe,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
# entry_8=Entry(entryframe,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
# entry_9=Entry(entryframe,font=('tahoma',12,'bold'),bd=5,width=40,justify=RIGHT)
entry_1.grid(row=0,column=0)
entry_2.grid(row=1,column=0)
entry_3.grid(row=2,column=0)
# countrylist.grid(row=3,column=0)
# city.grid(row=4,column=0)
# entry_6.grid(row=5,column=0)
# entry_7.grid(row=6,column=0)
# entry_8.grid(row=7,column=0)
# entry_9.grid(row=8,column=0)


tv=ttk.Treeview(listframe,columns=("id","name","company","country","city","address","phone","mobil","email"),show="headings",
                height=16,selectmode="extended")
# tv.pack()
tv.grid(row=1,column=0)
tv.heading('id', text="كود", anchor=W)
tv.heading('name', text="الاسم", anchor=W)
tv.heading('company', text="الشركة", anchor=W)
tv.heading('country', text="الدولة", anchor=W)
tv.heading('city', text="المدينة", anchor=W)
tv.heading('address', text="العنوان", anchor=W)
tv.heading('phone', text="الهاتف", anchor=W)
tv.heading('mobil', text="الموبايل", anchor=W)
tv.heading('email', text="الايميل", anchor=W)
tv.column('#0', stretch=NO, minwidth=0, width=20)
tv.column('#1', stretch=NO, minwidth=0, width=20)
tv.column('#2', stretch=NO, minwidth=0, width=80)
tv.column('#3', stretch=NO, minwidth=0, width=120)
tv.column('#4', stretch=NO, minwidth=0, width=90)
tv.column('#5', stretch=NO, minwidth=0, width=80)
tv.column('#6', stretch=NO, minwidth=0, width=120)
tv.column('#7', stretch=NO, minwidth=0, width=80)
tv.column('#8', stretch=NO, minwidth=0, width=80)
tv.column('#9', stretch=NO, minwidth=0, width=80)

buttoms_frame=Frame(root,background="#e1d8b2",bd=1,width=800,height=00,padx=2,pady=5,relief=RIDGE)
buttoms_frame.grid(row=3,column=0)
# ======================= Clients control buttoms ===============================

clientadd = Button(buttoms_frame, text="إضافة", width=9, height=1, bg="#0c2ef5", fg="white", command=donothing)
clientadd.config(font=("tahoma", 10, "bold",))
clientadd.grid(row=0, column=6, padx=10, pady=5)
clientsearch = Button(buttoms_frame, text="بحث", width=9, height=1, bg="#0acf83", fg="white", command=donothing)
clientsearch.config(font=("tahoma", 10, "bold"))
clientsearch.grid(row=0, column=5, padx=10, pady=5)
clientamed = Button(buttoms_frame, text="تعديل", width=9, height=1, bg="#1abcfe", fg="white", command=donothing)
clientamed.config(font=("tahoma", 10, "bold"))
clientamed.grid(row=0, column=4, padx=10, pady=5)
clientdelete = Button(buttoms_frame, text="إلغاء", width=9, height=1, bg="#a259ff", fg="white", command=donothing)
clientdelete.config(font=("tahoma", 10, "bold"))
clientdelete.grid(row=0, column=3, padx=10, pady=5)
clientlist = Button(buttoms_frame, text="جدول", width=9, height=1, bg="#ff7262", fg="white",  command=donothing)
clientlist.config(font=("tahoma", 10, "bold"))
clientlist.grid(row=0, column=2, padx=10, pady=5)
clientclear = Button(buttoms_frame, text="تفريغ الحقول", width=9, height=1, bg="#f24e1e", fg="white",command=donothing)
clientclear.config(font=("tahoma", 10, "bold"))
clientclear.grid(row=0, column=1, padx=10, pady=5)
clientclose = Button(buttoms_frame, text="إغلاق", width=9, height=1, bg="#fdab23", fg="white",command=donothing)
clientclose.config(font=("tahoma", 10, "bold"))
clientclose.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()

