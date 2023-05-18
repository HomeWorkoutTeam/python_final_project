from tkinter import *
from tkcalendar import Calendar
import connectDB
from tkinter import messagebox

# Create Object
root = Tk()
 
# Set geometry
root.geometry("500x600")

Label(root,text='ĐẶT SÂN BÓNG',fg='green',font=('cambria',16),width=25).pack(pady=5)

# Add Calendar
cal = Calendar(root, selectmode = 'day', date_pattern='dd/mm/yyyy')
 
cal.pack(pady = 5)

Label(root,text='Tên khách hàng: ').place(x=50,y=300)
tenKh = Entry(root,width=40)
tenKh.place(x=200,y=300)
Label(root,text='Số điện thoại: ').place(x=50,y=350)
sdtKh = Entry(root,width=40)
sdtKh.place(x=200,y=350)
Label(root,text='Đặt sân số: ').place(x=50,y=400)
id_san = Spinbox(root, width=40, values=connectDB.show_data_spin_box())
id_san.place(x=200, y=400)
sp1 = Spinbox(root, width=5, from_=16,to=21)
sp1.place(x=100, y=450)
Label(root,text=':').place(x=150,y=450)
sp2 = Spinbox(root, width=5, from_=00, to=59)
sp2.place(x=170, y=450)
Label(root,text='tới').place(x=250,y=450)
sp3 = Spinbox(root, width=5, from_=16,to=22)
sp3.place(x=300, y=450)
Label(root,text=':').place(x=350,y=450)
sp4 = Spinbox(root, width=5, from_=0,to=59)
sp4.place(x=370, y=450)

def add():
    ten = tenKh.get()
    sdt = sdtKh.get()
    h_start = sp1.get()
    m_start = sp2.get()
    h_stop = sp3.get()
    m_stop = sp4.get()
    id_san_thue = id_san.get()
    check_error()
    if(check_error()):
        query = "insert into khach_hang(ten,sdt,h_start,m_start,h_stop,m_stop,date,id_san) values (?,?,?,?,?,?,?,?)"
        data = (ten,sdt,h_start,m_start,h_stop,m_stop,cal.get_date(),id_san_thue)
        q_add = connectDB.connection.cursor()
        q_add.execute(query,data)
        result = connectDB.connection.cursor().fetchall()
        connectDB.connection.commit()
        messagebox.showinfo("Thông báo", "Đặt sân thành công !")

def check_error():
    if(tenKh.get()=='')or(sdtKh.get()=='')or(sp1.get()=='')or(sp2.get()=='')or(sp3.get()=='')or(sp4.get()==''):
        messagebox.showinfo("Cảnh báo","Dữ liệu không hợp lệ !")
        return False
    if(sp1.get()>sp3.get()):
        messagebox.showinfo("CẢnh báo","Thời gian không hợp lệ !")
        return False
    if(sp1.get()==sp3.get()):
        if(sp2.get()<sp4.get()):
            messagebox.showinfo("Cảnh báo","Thời gian không hợp lệ !")
            return False
        if((int(sp4.get())-int(sp2.get()))<30):
            messagebox.showinfo("Cảnh báo","Thời gian không hợp lệ !")
            return False
    return True
Button(root, text = "Đặt sân", width= 50, bg='green',
       command = add).place(x=70,y=500)
Button(root, text = "Thoát", width= 50, bg='yellow',
       command = exit).place(x=70,y=550)

# Execute Tkinter
root.mainloop()