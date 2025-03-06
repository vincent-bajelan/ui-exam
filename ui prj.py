from tkinter import*
win=Tk()
win.geometry("550x400")
win.title("vince")
win.resizable(0,0)
win.configure(background="light gray")
#################widjet

lbl_name=Label(win,text="name :", font="arial 15 ",bg="light gray")
lbl_name.place(x=20,y=10)
ent_name=Entry(win)
ent_name.place(x=140,y=15)

lbl_year=Label(win,text="last name :",font="arial 15 ",bg="light gray")
lbl_year.place(x=20,y=40)
ent_year=Entry(win)
ent_year.place(x=140,y=45)

lbl_writer=Label(win,text="course :",font="arial 15 ",bg="light gray")
lbl_writer.place(x=300,y=10)
ent_writer=Entry(win)
ent_writer.place(x=400,y=15)

lbl_isbn=Label(win,text="password :",font="arial 15",bg="light gray")
lbl_isbn.place(x=300,y=40)
ent_isbn=Entry(win)
ent_isbn.place(x=400,y=45)

lst_show = Listbox(win,width=40,font="arial 13")
lst_show.place(x=20,y=100)

lbl_pasword=Label(win,text="login password :",font="arial 11",bg="light gray")
lbl_pasword.place(x=20,y=330)

ent_login=Entry(win , width=63)
ent_login.place(x=140,y=332)
#________________
Btn_seeall=Button(win,text="see all",width=12,font="arial  11",bg="white")
Btn_seeall.place(x=405,y=100)

btn_add=Button(win,text="add",width=12,font="arial  11",bg="white")
btn_add.place(x=405,y=135)      

btn_clearent=Button(win,text="clear",width=12,font="arial  11",bg="white")
btn_clearent.place(x=405,y=170)

btn_delete=Button(win,text="delete",width=12,font="arial  11",bg="white")
btn_delete.place(x=405,y=205)

btn_exit=Button(win,text="exit",width=12,font="arial  11",bg="white")
btn_exit.place(x=405,y=240)

btn_enterweb=Button(win,text="enter to web",width=12,font="arial  11",bg="white")
btn_enterweb.place(x=405,y=275)




win.mainloop()