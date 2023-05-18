import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import*
import sqlite3
import connectDB


#Window
r = tk.Tk()
r.title('Quản lý sân bóng mini')
r.geometry('800x500')
r.resizable(False,False)
frm=Frame(r)
frm.pack(side=tk.LEFT)

Label(frm,text='QUẢN LÝ SÂN BÓNG MINI',fg='green',font=('cambria',14),width=25).pack()

#TreeView
style = ttk.Style()
style.theme_use('clam')
tree=ttk.Treeview(frm,columns=(1,2,3,4,5,6,7,8),show='headings',height='7')
for i in range(1,9):
    tree.column(i,anchor='center',width=100)
tree.heading(1,text='Tên Khách hàng') 
tree.heading(2,text='Số điện thoại')
tree.heading(3,text='Tên sân')
tree.heading(4,text='Start(h)')
tree.heading(5,text='Start(m)')
tree.heading(6,text='Stop(h)')
tree.heading(7,text='Stop(m)')
tree.heading(8,text='Ngày đặt sân')
#Load Table
rows = connectDB.show_data()

#Load DB
for i in rows:
    tree.insert('','end',iid=i[0],values=i)

tree.pack()

def delete():
    selected = tree.selection()[0]
    query = 'delete from khach_hang where id = ?'
    data = (selected,)
    q_del = connectDB.connection.cursor()
    q_del.execute(query,data)
    connectDB.connection.commit()
    tree.delete(selected)

#insert button
b1=tk.Button(frm,text='DELETE',bg='yellow',width=20,command=delete)
b1.pack(pady=5)
b2=tk.Button(frm,text='EXIT',bg='yellow',width=20,command=exit)
b2.pack(pady=5)


r.mainloop()