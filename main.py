from tkinter import *
from tkinter import filedialog
filetypes=(("textfiles","*.txt"),)
def s():
    w=t.get("1.0",END)
    file=(filedialog.asksaveasfile(filetypes=filetypes))
    file.write(w)
def o():
 t.delete("1.0",END)
 file=(filedialog.askopenfile())
 s=file.read()
 t.insert("1.0",s)
def c():
    if iv.get()==0:
        x["background"] = "#f2e5bf"
        t.config(bg="#f2e5bf",selectbackground="#c9b47b",insertbackground="#b09f71",font=("Stink",12))

        b.config(bg="#f2e5bf")
        bb.config(bg="#f2e5bf")


    elif iv.get()==1:
        x["background"]='#1273db'
        t.config(bg="#1273db",selectbackground="#12afdb",insertbackground="#12afdb",font=("Castellar",10),fg="white")
        b.config(bg="#1273db")

        bb.config(bg="#1273db")



x=Tk()
x.title("note_pad")
x.geometry("500x400")
x.iconbitmap("NOTEBOOK.ICO.ico")
x["background"]="#f2e5bf"
f=Frame()



x.resizable(False,False)
t=Text(x,font=("Stink",12),bg="#f2e5bf",selectbackground="#c9b47b",insertbackground="#b09f71",height=15)
b=Button(f,text="save",command=s,bg="#f2e5bf",height=5,width=10)
bb=Button(f,text="open",command=o,bg="#f2e5bf",height=5,width=10)
iv=IntVar()
cb=Checkbutton(x,text="pink mode ",bg="#f2e5bf",selectcolor='#f0dca1',variable=iv,command=c)




t.pack()
b.grid(row=0,column=0)
bb.grid(row=0,column=1)
f.pack()
cb.pack()
x.mainloop()
