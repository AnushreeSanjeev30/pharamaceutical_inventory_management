from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import datetime,date
conn=sqlite3.connect("D:\Python project\data.db")

window1=Tk()
window1.title("Login")
window1.geometry('1600x900')
window1.configure(bg="turquoise3")

def login():
    username ="pharma"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        
        
        main()
    elif username_entry.get()!=username :
        messagebox.showerror(title="Error", message="Invalid Username.")
    elif username_entry.get()!=password:
        messagebox.showerror(title="Error", message="Invalid password.")



frame=Frame(bg='turquoise3')


 #creating widgets
my_Image=ImageTk.PhotoImage(Image.open("D:\Python project\pharma_logo.jpeg"))
my_l=Label(image=my_Image)
my_l.pack() 
login_label=Label(frame,text="Login System",font=("Arial", 30,"bold"),fg="white",bg="cyan4")
username_label=Label(frame, text="username",font=("Arial", 30),fg="white",bg="cyan4")
password_label=Label(frame, text="password",font=("Arial", 30),fg="white",bg="cyan4")
username_entry=Entry(frame,font=("Arial", 30))
password_entry=Entry(frame, show="*",font=("Arial", 30))
login_button=Button(frame,text="login",font=("Arial", 30),command=login)



  #placing widgets on screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2,pady=30)


  
frame.pack()

def main():
    window1.destroy()
    r=Tk()
    r.title(" WELCOME TO MY PHARMA\\PRO.com")
    r.configure(width=2000, height=2000, bg='turquoise3')

    

    label1 = Label(r, text="PID", bg="DeepPink3", relief="ridge", fg="white", font=("verdana", 14), width=25)
    entry1 = Entry(r, font=("Times", 12),width=30)

    label2 = Label(r, text="ENTER DRUG NAME", bd="2", relief="ridge", bg="DeepPink3", fg="white", font=("verdana", 14),width=25)
    entry2 = Entry(r, font=("Times", 12),width=30)

    label3 = Label(r, text="ENTER DRUG PRICE", bd="2", relief="ridge", height="1", bg="DeepPink3", fg="white",font=("verdana", 14), width=25)
    entry3 = Entry(r, font=("Times", 12),width=30)

    label4 = Label(r, text="ENTER DRUG QUANTITY", bd="2", relief="ridge", bg="DeepPink3", fg="white", font=("verdana", 14),width=25)
    entry4 = Entry(r, font=("Times", 12),width=30)

    label5 = Label(r, text="DRUG USAGE", bg="DeepPink3", relief="ridge", fg="white", font=("verdana", 14), width=25)
    entry5 = Entry(r, font=("Times", 12),width=30)

    label6 = Label(r, text="MANUFACTURER", bg="DeepPink3", relief="ridge", fg="white", font=("verdana", 14), width=25)
    entry6 = Entry(r, font=("Times", 12),width=30)

    label7 = Label(r, text="EXPIRY DATE", bg="DeepPink3", relief="ridge", fg="white", font=("verdana", 14), width=25)
    entry7 = Entry(r, font=("Times", 12),width=30)

    label8 = Label(r, text="AGE", bg="DeepPink3", relief="ridge", fg="white", font=("verdana", 14), width=25)
    entry8 = Entry(r, font=("Times", 12),width=30)
        

        

    # arranging the labels and entry sections on the screen
    label_title = Label(r, text=" ENTER THE FOLLOWING DETAILS", font=("Times", 20),bg="DodgerBlue4",fg="white")
    label_title.grid(row=1, column=0, sticky="N", padx=10, pady=10)

    label1.grid(row=3, column=0, sticky="NEWS", padx=10, pady=10)
    label2.grid(row=4, column=0, sticky="NEWS", padx=10, pady=10)
    label3.grid(row=5, column=0, sticky="NEWS", padx=10, pady=10)
    label4.grid(row=6, column=0, sticky="NEWS", padx=10, pady=10)
    label5.grid(row=7, column=0, sticky="NEWS", padx=10, pady=10)
    label6.grid(row=8, column=0, sticky="NEWS", padx=10, pady=10)
    label7.grid(row=9, column=0, sticky="NEWS", padx=10, pady=10)
    label8.grid(row=10, column=0, sticky="NEWS", padx=10, pady=10)
        
    

    entry1.grid(row=3, column=1, padx=10, pady=10)
    entry2.grid(row=4, column=1, padx=10, pady=10)
    entry3.grid(row=5, column=1, padx=10, pady=10)
    entry4.grid(row=6, column=1, padx=10, pady=10)
    entry5.grid(row=7, column=1, padx=10, pady=10)
    entry6.grid(row=8, column=1, padx=10, pady=10)
    entry7.grid(row=9, column=1, padx=10, pady=10)
    entry8.grid(row=10, column=1, padx=10, pady=10)
        


        
    #Adding an item to the database table medicines_list

    def add_func():
        
        e1 = entry1.get()
        e2 = entry2.get()
        e3 = entry3.get()
        e4 = entry4.get()
        e5= entry5.get()
        e6 = entry6.get()
        e7 = entry7.get()
        e8= entry8.get()

        x='2023-12-18'
        
        conn=sqlite3.connect("D:\Python project\data.db")
    
        table_create_query = '''CREATE TABLE if not exists medicines_list
                ( PID INT primary key not null,med_name TEXT, med_price REAL, med_qty INT,med_use TEXT,manufacturer TEXT,expiry DATE,age INT)'''
        
        if e1:
            conn.execute(table_create_query)
            
            if e7==x or e7<=x:
                messagebox.showerror("Error", f"Drug Expired")
            else:
                conn.execute("INSERT into medicines_list(PID,med_name,med_price,med_qty,med_use,manufacturer,expiry,age) values (?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8))
                messagebox.showinfo("Success", f"{e2} added successfully")
            conn.commit()
            
            
        else:
            messagebox.showerror("Error", f" Enter PID ")
        
        conn.close()


    # To display the details of a aprticular medicine

    def search_medicine():

        medicine_name = d_entry.get()
        
        if medicine_name:
            r=Tk()
            r.configure(width=2000, height=2000, bg='turquoise3')
            r.title(" MY PHARMA ")
            frame=Frame(r)
            frame.pack()
            frame.place(anchor="center",relx=0.50, rely=0.25)

            conn = sqlite3.connect("D:\Python project\data.db")
            c = conn.cursor()
        
    
            label_title = Label(frame, text=" DRUG DETAILS", font=("Times",25),bg="DEEP PINK",fg="BLACK")
            label_title.grid(row=0, column=3, sticky="N", padx=10, pady=10)

            
            c.execute(("SELECT * FROM medicines_list where med_name=? "),(medicine_name,))
            
            e1 = Label(frame, text= "PID", font=("Times", 20), width=10)
            e1.grid(row=2, column=0, sticky="W", padx=10, pady=10)

            e2 = Label(frame, text= "Med_Name", font=("Times", 20), width=10)
            e2.grid(row=2, column=1, sticky="W", padx=10, pady=10)

            e3 = Label(frame, text= "Price", font=("Times", 20), width=10)
            e3.grid(row=2, column=2, sticky="W", padx=10, pady=10)

            e4 = Label(frame, text= "Quantity", font=("Times", 20), width=10)
            e4.grid(row=2, column=3, sticky="W", padx=10, pady=10)

            e5 = Label(frame, text= "Used For", font=("Times", 20), width=8)
            e5.grid(row=2, column=4, sticky="W", padx=10, pady=10)

            e6 = Label(frame, text= "Manufactured Date", font=("Times", 20), width=15)
            e6.grid(row=2, column=5, sticky="W", padx=10, pady=10)

            e7 = Label(frame, text= "Expiry Date", font=("Times", 20), width=10)
            e7.grid(row=2, column=6, sticky="W", padx=10, pady=10)

            e8 = Label(frame, text= "Age", font=("Times", 20), width=10)
            e8.grid(row=2, column=7, sticky="W", padx=10, pady=10)

            for i in c:
                label1 = Label(frame, text=i[0], font=("Times", 18), width=10)
                label1.grid(row=3, column=0, sticky="W", padx=10, pady=10)

                label2 = Label(frame, text=i[1],  font=("Times", 18),width=10)
                label2.grid(row=3, column=1, sticky="W", padx=10, pady=10)

                label3 = Label(frame, text=i[2], font=("Times", 18), width=10)
                label3.grid(row=3, column=2, sticky="W", padx=10, pady=10)

                label4 = Label(frame, text=i[3], font=("Times", 18),width=10)
                label4.grid(row=3, column=3, sticky="W", padx=10, pady=10)

                label5 = Label(frame, text=i[4], font=("Times", 18), width=8)
                label5.grid(row=3, column=4, sticky="W", padx=10, pady=10)

                label6 = Label(frame, text=i[5], font=("Times", 18), width=15)
                label6.grid(row=3, column=5, sticky="W", padx=10, pady=10)

                label7 = Label(frame, text=i[6],font=("Times", 18), width=10)
                label7.grid(row=3, column=6, sticky="W", padx=10, pady=10)
            
                label8 = Label(frame, text=i[7], font=("Times", 18), width=10)
                label8.grid(row=3, column=7, sticky="W", padx=10, pady=10)   
        else:
            messagebox.showerror("Error", f" Select DRUG ")
        
        

    # To modify the quantity details of a medicine

    def updateitem():

        conn = sqlite3.connect("D:\Python project\data.db")
        
        e2 = entry2.get()
        e4 = entry4.get()
        
        conn.execute(('update medicines_list set med_qty =? where med_name=?'),(e4,e2))
        conn.commit()        
        conn.close()


            
        
    # To Delete a particular medicine details from the database table 

    def delete():
        conn = sqlite3.connect("D:\Python project\data.db")
        c = conn.cursor()
        
        medicine_name = d_entry.get()
        
        # Check if the medicine exists before attempting to delete
        c.execute("SELECT * FROM medicines_list WHERE med_name=?", (medicine_name,))
        result = c.fetchone()
        
        if result:
            c.execute("DELETE FROM medicines_list WHERE med_name=?", (medicine_name,))
            conn.commit()
            messagebox.showinfo("Success", f" {medicine_name} deleted successfully.")
        else:
            messagebox.showerror("Error", f" {medicine_name} Drug Not found.")



    d_label=Label(r,text="ITEM NAME",bg="DeepPink3", relief="ridge", fg="white", font=("verdana", 14), width=25)
    d_label.grid(row=4, column=2, sticky="NEWS", padx=10, pady=10)

    conn = sqlite3.connect("D:\Python project\data.db")
    c=conn.cursor()
    c.execute('Select med_name from medicines_list order by med_name')
    result=[]

    for i in c.fetchall():
        result.append(i[0]) 


    d_entry=ttk.Combobox(r,values=result)
    d_entry.grid(row=4, column=3, sticky="NEWS", padx=10, pady=10)


    def clearitem():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        entry8.delete(0, END)

    # Add_Item_Button
    add_button =Button(r, text="ADD DRUG",borderwidth=7,fg="DodgerBlue4",command=add_func)
    add_button.grid(row=11, column=1, sticky="W", padx=10, pady=10)

    #Update_Item_Button
    update_button=Button(r,text="UPDATE DRUG",borderwidth=5,fg="DodgerBlue4",command=updateitem)
    update_button.grid(row=12,column=1,sticky="W", padx=10, pady=10)

    #Clear_Screen_Button
    button9= Button(r, text="CLEAR SCREEN", fg="Dodger Blue4", command=clearitem)
    button9.grid(row=11,column=2,sticky="W", padx=10, pady=10)

    #Search_Item_Button
    search_button=Button(r,text="SEARCH DRUG",borderwidth=5,command=search_medicine,fg="DodgerBlue4")
    search_button.grid(row=5,column=2,sticky="W", padx=10, pady=10)

    #Delete_Item_Button
    delete_button=Button(r,text="DELETE DRUG",borderwidth=5,command = delete,fg="DodgerBlue4")
    delete_button.grid(row=6,column=2,sticky="W", padx=10, pady=10)
window1.mainloop()
frame.mainloop()
