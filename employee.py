from fileinput import close
from logging import root
from re import search
from sqlite3 import Cursor, connect
from tkinter import*                #type: ignore
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk       #type: ignore
from tkinter import messagebox
import mysql.connector    #type: ignore

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("JR COMPLIANCE")

        # VARIABLES

        self.var_Department=StringVar()
        self.var_Name=StringVar()
        self.var_Designation=StringVar()
        self.var_Email=StringVar()
        self.var_Employee_ID=StringVar()
        self.var_married_Status=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_ID_Proof_Type=StringVar()
        self.var_ID_Proof=StringVar()
        self.var_Gender=StringVar()
        self.var_Phone=StringVar()
        self.var_Country=StringVar()
        self.var_Salary=StringVar()



        lbl_title=Label(self.root,text='Employee Managment System',font=('times new roman',30,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1380,height=50)

        # logo
        img_logo=Image.open("Logo.jpg")  # type: ignore
        img_logo=img_logo.resize((50,50),Image.Resampling.LANCZOS)  # type: ignore
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=370,y=0,width=50,height=50)

        # Image FRAME
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1365,height=160)

        # 1st
        img1=Image.open("BANNER.jpg")  # type: ignore
        img1=img1.resize((1365,160),Image.Resampling.LANCZOS)    # type: ignore
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=1365,height=160)

        # Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=0,y=190,width=1365,height=552)

        # upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee information',font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        upper_frame.place(x=10,y=10,width=1345,height=270)

        # Labels and Entry field
        # Department
        lbl_dep=Label(upper_frame,text='Department',font=('arial',10,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_Department,font=('arial',11,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','Sales','Admin','HR','Development','Degital marketing','CA','Adminstration')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name
        lbl_name=Label(upper_frame,font=('arial',10,'bold'),text='Name',bg='white')
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_Name,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        
        # Designition
        lbl_Designation=Label(upper_frame,font=('arial',10,'bold'),text='Designation',bg='white')
        lbl_Designation.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_Designation,width=22,font=('arial',11,'bold'))
        txt_Designation.grid(row=1,column=1,padx=2,pady=7)

        # Email
        lbl_Email=Label(upper_frame,font=('arial',10,'bold'),text='Email',bg='white')
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_Email,width=22,font=('arial',11,'bold'))
        txt_Email.grid(row=1,column=3,padx=2,pady=7)

        # EMP ID
        lbl_emp_id=Label(upper_frame,text='Employee ID',font=('arial',10,'bold'),bg='white')
        lbl_emp_id.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_emp_id=ttk.Entry(upper_frame,textvariable=self.var_Employee_ID,width=22,font=('arial',11,'bold'))
        txt_emp_id.grid(row=2,column=1,padx=2,pady=7)

        # Married
        lbl_married_status=Label(upper_frame,text='Married Status',font=('arial',10,'bold'),bg='white')
        lbl_married_status.grid(row=2,column=2,pady=7,padx=2,sticky=W)

        combo_married=ttk.Combobox(upper_frame,textvariable=self.var_married_Status,font=('arial',11,'bold'),width=17,state='readonly')
        combo_married['value']=('Married','UnMarried')
        combo_married.current(0)
        combo_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)


        # Dob
        lbl_Dob=Label(upper_frame,font=('arial',10,'bold'),text='DOB',bg='white')
        lbl_Dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_Dob=ttk.Entry(upper_frame,textvariable=self.var_DOB,width=22,font=('arial',11,'bold'))
        txt_Dob.grid(row=3,column=1,padx=2,pady=7)

        # Doj
        lbl_Doj=Label(upper_frame,font=('arial',10,'bold'),text='DOJ',bg='white')
        lbl_Doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_Doj=ttk.Entry(upper_frame,textvariable=self.var_DOJ,width=22,font=('arial',11,'bold'))
        txt_Doj.grid(row=3,column=3,padx=2,pady=7)

        # Select ID PROFF
        combo_id_proof=ttk.Combobox(upper_frame,textvariable=self.var_ID_Proof_Type,font=('arial',11,'bold'),width=17,state='readonly')
        combo_id_proof['value']=('Select id proof','Pan card','Adhar card','Other')
        combo_id_proof.current(0)
        combo_id_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        lbl_ID_PROFF=ttk.Entry(upper_frame,textvariable=self.var_ID_Proof,width=22,font=('arial',11,'bold'))
        lbl_ID_PROFF.grid(row=4,column=1,padx=2,pady=7)

         # Gender
        lbl_gender=Label(upper_frame,text='Gender',font=('arial',10,'bold'),bg='white')
        lbl_gender.grid(row=4,column=2,pady=7,padx=2,sticky=W)

        combo_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_Gender,font=('arial',11,'bold'),width=17,state='readonly')
        combo_txt_gender['value']=('Select','Male','Female','Other')
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        # Phone
        lbl_phone=Label(upper_frame,font=('arial',10,'bold'),text='Phone No',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_Phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        # Country
        lbl_Country=Label(upper_frame,font=('arial',10,'bold'),text='Country',bg='white')
        lbl_Country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_Country=ttk.Entry(upper_frame,textvariable=self.var_Country,width=22,font=('arial',11,'bold'))
        txt_Country.grid(row=1,column=5,padx=2,pady=7)

        # CTC
        lbl_ctc=Label(upper_frame,font=('arial',10,'bold'),text='Salary(CTC):',bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_Salary,width=22,font=('arial',11,'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

    
        #Button Fram
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        Button_frame.place(x=1150,y=10,width=170,height=210)

        btn_add=Button(Button_frame,text="Save",command=self.add_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(Button_frame,text="Update",command=self.update_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(Button_frame,text="Delete",command=self.delete_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(Button_frame,text="Clear",command=self.reset_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        

        # down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee information Table',font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        down_frame.place(x=10,y=280,width=1345,height=270)

        # search Fram
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='search Employee information',font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        search_frame.place(x=0,y=0,width=1355,height=65)

        # Search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=('arial',12,'bold'),width=18)

        com_txt_search['value']=('select option','Phone','ID_Proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text='Search',command=self.search_data,width=14,font=('arial',11,'bold'))
        btn_search.grid(row=0,column=3,padx=5)

        btn_showALL=Button(search_frame,text='Show ALL',command=self.fetch_data,width=14,font=('arial',11,'bold'))
        btn_showALL.grid(row=0,column=4,padx=5)

        # IMAGE LOGO

        img_mask=Image.open("1.png")    # type: ignore
        img_mask=img_mask.resize((50,50),Image.Resampling.LANCZOS)    # type: ignore
        self.photo_mask=ImageTk.PhotoImage(img_mask)

        #=======================employee Table======================

        # table Frame

        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1345,height=170)

        # scrool bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=('dep','name','degi','email','Employee_ID','married','dob','doj','idproofcombo','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)  

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('Employee_ID',text='Employee_ID')
        self.employee_table.heading('married',text='Married_Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcombo',text='ID_Proof_Type')
        self.employee_table.heading('idproof',text='ID_Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'

        self.employee_table.column('dep',width=150)
        self.employee_table.column('name',width=150)
        self.employee_table.column('degi',width=150)
        self.employee_table.column('email',width=150)
        self.employee_table.column('Employee_ID',width=150)
        self.employee_table.column('married',width=150)
        self.employee_table.column('dob',width=150)
        self.employee_table.column('doj',width=150)
        self.employee_table.column('idproofcombo',width=150)
        self.employee_table.column('idproof',width=150)
        self.employee_table.column('gender',width=150)
        self.employee_table.column('phone',width=150)
        self.employee_table.column('country',width=150)
        self.employee_table.column('salary',width=150)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)    # type: ignore

        self.fetch_data()


    #----------------------------------Function Declaration--------------------------------------------------------------


    def add_data(self):
        if self.var_Department.get()=="" or self.var_Email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Root',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                        self.var_Department.get(),
                                                                                                        self.var_Name.get(),
                                                                                                        self.var_Designation.get(),
                                                                                                        self.var_Email.get(),
                                                                                                        self.var_Employee_ID.get(),
                                                                                                        self.var_married_Status.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_DOJ.get(),
                                                                                                        self.var_ID_Proof_Type.get(),
                                                                                                        self.var_ID_Proof.get(),
                                                                                                        self.var_Gender.get(),
                                                                                                        self.var_Phone.get(),
                                                                                                        self.var_Country.get(),
                                                                                                        self.var_Salary.get()

                                                                                                        ))
                conn.commit()
                self.fetch_data   
                conn.close()
                messagebox.showinfo('success','Employee has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Root',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children()) 
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # Get Cursor

    def get_cursor(self,event=""):
        Cursor_row=self.employee_table.focus()
        content=self.employee_table.item(Cursor_row)  
        data=content['values']

        self.var_Department.set(data[0])
        self.var_Name.set(data[1])
        self.var_Designation.set(data[2])
        self.var_Email.set(data[3])
        self.var_Employee_ID.set(data[4])
        self.var_married_Status.set(data[5])
        self.var_DOB.set(data[6])
        self.var_DOJ.set(data[7])
        self.var_ID_Proof_Type.set(data[8])
        self.var_ID_Proof.set(data[9])
        self.var_Gender.set(data[10])
        self.var_Phone.set(data[11])
        self.var_Country.set(data[12])
        self.var_Salary.set(data[13])
        
#       Update Data

    def update_data(self):
        if self.var_Department.get()=="" or self.var_Email.get()=="":
            messagebox.showerror('Error','All fields are required')

        else:
            try:
                update=messagebox.askyesno('update','Are sure update this employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Root',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Employee_ID=%s,Married_Status=%s,DOB=%s,DOJ=%s,ID_Proof_Type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s WHERE ID_Proof=%s',(
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                    self.var_Department.get(),
                                                                                                                                                                                                                                    self.var_Name.get(),
                                                                                                                                                                                                                                    self.var_Designation.get(),
                                                                                                                                                                                                                                    self.var_Email.get(),
                                                                                                                                                                                                                                    self.var_Employee_ID.get(),
                                                                                                                                                                                                                                    self.var_married_Status.get(),
                                                                                                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                                                                                                    self.var_DOJ.get(),
                                                                                                                                                                                                                                    self.var_ID_Proof_Type.get(),
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                                                                                                    self.var_Phone.get(),
                                                                                                                                                                                                                                    self.var_Country.get(),
                                                                                                                                                                                                                                    self.var_Salary.get(),
                                                                                                                                                                                                                                    self.var_ID_Proof.get()
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        ))

                else:
                    if not update:
                        return
                conn.commit()   #type: ignore
                self.fetch_data()
                conn.close()    #type: ignore
                messagebox.showinfo('success','Employee successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Delete Data

    def delete_data(self):
        if self.var_ID_Proof.get()=="":  
            messagebox.showerror('Error',"All field are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Root',database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_ID_Proof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()   #type: ignore  
                self.fetch_data()
                conn.close()    #type: ignore
                messagebox.showinfo('Delete','Employee successfully Delete',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Reset data

    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Name.set("")
        self.var_Designation.set("")
        self.var_Email.set("")
        self.var_Employee_ID.set("")
        self.var_married_Status.set("Married")
        self.var_DOB.set("")
        self.var_DOJ.set("")
        self.var_ID_Proof_Type.set("Select ID Proof")
        self.var_ID_Proof.set("")
        self.var_Gender.set("")
        self.var_Phone.set("")
        self.var_Country.set("")
        self.var_Salary.set("")

    # Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Root',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('SELECT * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()