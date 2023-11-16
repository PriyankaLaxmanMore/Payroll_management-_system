from tkinter import *
from tkinter import messagebox
##import pymysql  # pip install pymysql
import time


class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Mangement System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10)
        title.place(x=0,y=0,relwidth=1)
        
        ################### frame 1 #########################
        
        # ********** variable *********************
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()
        self.var_address=StringVar()
        self.var_linkedin=StringVar()
        
        
        
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
        
        
        
        Frame0=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame0.place(x=10,y=60,width=1325,height=620)
        
        
        lbl_code=Label(Frame0,text="WELCOME",font=("Algerian",50),bg="white",fg="#191870",padx=10)
        lbl_code.place(x=480,y=200,width=400,height=60)
        
        lbl_code1=Label(Frame0,text="to",font=("times to ruman",20),bg="white",fg="BLACK",padx=10)
        lbl_code1.place(x=480,y=260,width=400,height=60)
        
        lbl_code2=Label(Frame0,text="Payroll  Management ",font=("Algerian",70),bg="white",fg="#800000",padx=10)
        lbl_code2.place(x=100,y=330,width=1100,height=60)
        
        lbl_code3=Label(Frame0,text="System",font=("Algerian",70),bg="white",fg="#800000",padx=10)
        lbl_code3.place(x=480,y=430,width=400,height=60)
        
        
        
        btn_emp_name=Button(Frame0,text="NAME",command=self.employee_frame1,font=("times new roman",18),bg="#00ced1",fg="white",padx=10)
        btn_emp_name.place(x=50,y=50,width=230,height=60)

        btn_contact=Button(Frame0,text="Detail",command=self.employee_frame2,font=("times new roman",18),bg="#696969",fg="white",padx=10)
        btn_contact.place(x=300,y=50,width=230,height=60)
        
        btn_status=Button(Frame0,text="CONTACT",command=self.employee_frame3,font=("times new roman",18),bg="#008080",fg="white",padx=10)
        btn_status.place(x=550,y=50,width=230,height=60)
        
        btn_status=Button(Frame0,text="STATUS",command=self.employee_frame4,font=("times new roman",18),bg="#ff1493",fg="white",padx=10)
        btn_status.place(x=800,y=50,width=230,height=60)
        
        btn_status=Button(Frame0,text="SALARY",command=self.employee_frame5,font=("times new roman",18),bg="#0000ff",fg="white",padx=10)
        btn_status.place(x=1050,y=50,width=230,height=60)
        
        
        
    def employee_frame1(self):
            
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="#FFE4E1")
        Frame1.place(x=10,y=200,width=1325,height=620)
        
        #title2=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10)
        #title2.place(x=0,y=0,relwidth=1)
        
        lbl_code=Label(Frame1,text="Employee code",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_code.place(x=50,y=50,width=300,height=60)
        txt_code=Entry(Frame1,font=("times new roman",25),textvariable=self.var_emp_code ,bg="#ffff00",fg="black")
        txt_code.place(x=380,y=50,width=300,height=60)
        
        #btn_search=Button(Frame1,text="Search",font=("times new roman",13),bg="pink",fg="purple",padx=10)
        #btn_search.place(x=600,y=10)
        
       
        #   frame 1 button
        btn_save1=Button(Frame1,text="SAVE",command=self.add,font=("times new roman",25),bg="#ff0000",fg="white",padx=10)
        btn_save1.place(x=1050,y=50,width=230,height=60)

        btn_delete1=Button(Frame1,text="DETELE",command=self.delete, font=("times new roman",25),bg="#00ff00",fg="white",padx=10)
        btn_delete1.place(x=1050,y=150,width=230,height=60)
        
        btn_update1=Button(Frame1,text="UPDATES",command=self.update, font=("times new roman",25),bg="#8b008b",fg="white",padx=10)
        btn_update1.place(x=1050,y=250,width=230,height=60)
        
        btn_clear1=Button(Frame1,text="CLEAR",command=self.clear,font=("times new roman",25),bg="#00008b",fg="white",padx=10)
        btn_clear1.place(x=1050,y=350,width=230,height=60)
        
        
    
        
        # ************************* Row 1 ****************************
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_designation.place(x=50,y=150,width=300,height=60)
        txt_designation=Entry(Frame1,font=("times new roman",25),textvariable=self.var_designation ,bg="#ffff00",fg="black")
        txt_designation.place(x=380,y=150,width=300,height=60)
        
        
        
        lbl_Name=Label(Frame1,text="Name",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_Name.place(x=50,y=250,width=300,height=60)
        txt_Name=Entry(Frame1,font=("times new roman",25),textvariable=self.var_name,bg="#ffff00",fg="black")
        txt_Name.place(x=380,y=250,width=300,height=60)
        
        
       
        
        
        # *****************  Calculator Frame  ****************************
        self.var_txt=StringVar()
        self.var_operator=''
        
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)  
        
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator='' 
            
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
            
        
        
    
    def add(self): 
        if self.var_emp_code.get()=='':
            messagebox.showerror("ERROR","Employee deatail are required")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_detail1 where emp_code=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                
                if rows!=None:
                    messagebox.showerror("Error","This Employee ID has already available in our record,try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_detail1 values(%s,%s,%s)",
                    (
                        self.var_emp_code.get(),
                        self.var_designation.get(),  
                        self.var_name.get(),
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Added Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                
    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error"," employee Id must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_detail1 where emp_code=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","Invalide employee id,try again with another ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_detail1 where emp_code=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
        
    def clear(self):
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        
    
    def update(self): 
        if self.var_emp_code.get()=='':
            messagebox.showerror("ERROR","Employee deatail are required")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_detail1 where emp_code=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","This Employee ID is invalid ,try again with another ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_detail1` SET `designation`=%s,`name`=%s WHERE `emp_code`=%s",
                    (
                        
                        self.var_designation.get(),  
                        self.var_name.get(),
                        self.var_emp_code.get()
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Updated Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                    
    
        
  
    def employee_frame2(self):
        #self.root2=Tk()
        #self.root2.title("Employee Payroll Management System")
        #self.root2.geometry("1350x700+0+0")
        #self.root2.config(bg="white")
        #title=Label(self.root2,text="Employee Payroll Mangement System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10)
        #title.place(x=0,y=0,relwidth=1)
        
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="#F5FFFA")
        Frame2.place(x=10,y=200,width=1325,height=620)

        
        lbl_gender=Label(Frame2,text="Gender",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_gender.place(x=50,y=150,width=300,height=50)
        txt_gender=Entry(Frame2,font=("times new roman",25),textvariable=self.var_gender ,bg="#ffff00",fg="black")
        txt_gender.place(x=380,y=150,width=300,height=50)
        
        
        lbl_age=Label(Frame2,text="Age",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_age.place(x=50,y=50,width=300,height=50)
        txt_age=Entry(Frame2,font=("times new roman",25),textvariable=self.var_age,bg="#ffff00",fg="black")
        txt_age.place(x=380,y=50,width=300,height=50)
        
        lbl_dob=Label(Frame2,text="D.O.B.",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_dob.place(x=50,y=250,width=300,height=50)
        txt_dob=Entry(Frame2,font=("times new roman",25),textvariable=self.var_dob,bg="#ffff00",fg="black")
        txt_dob.place(x=380,y=250,width=300,height=50)
        
        
        lbl_doj=Label(Frame2,text="D.O.J",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_doj.place(x=50,y=350,width=300,height=50)
        txt_doj=Entry(Frame2,font=("times new roman",25),textvariable=self.var_doj,bg="#ffff00",fg="black")
        txt_doj.place(x=380,y=350,width=300,height=50)
        
        
        # BUTTON 
        btn_save2=Button(Frame2,text="SAVE",command=self.add2,font=("times new roman",25),bg="#ff0000",fg="white",padx=10)
        btn_save2.place(x=1050,y=50,width=230,height=60)

        btn_delete2=Button(Frame2,text="DETELE",command=self.delete2, font=("times new roman",25),bg="#00ff00",fg="white",padx=10)
        btn_delete2.place(x=1050,y=150,width=230,height=60)
        
        btn_update2=Button(Frame2,text="UPDATES",command=self.update2, font=("times new roman",25),bg="#8b008b",fg="white",padx=10)
        btn_update2.place(x=1050,y=250,width=230,height=60)
        
        btn_clear2=Button(Frame2,text="CLEAR",command=self.clear2, font=("times new roman",25),bg="#00008b",fg="white",padx=10)
        btn_clear2.place(x=1050,y=350,width=230,height=60)
        
        
        
    
    def add2(self): 
        if self.var_age.get()=='':
            messagebox.showerror("ERROR","Employee age is required")
            #self.var_age=StringVar()    
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_detail2 where age=%s",(self.var_age.get()))
                rows=cur.fetchone()
                
                
                if rows!=None:
                    messagebox.showerror("Error","This Employee ID has already available in our record,try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_detail2 values(%s,%s,%s,%s)",
                    (
                        self.var_age.get(),  
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_doj.get()
                    )
                    )
                    
                    
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Added Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                
            
                
    def delete2(self):
        if self.var_age.get()=='':
            messagebox.showerror("Error"," employee age must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_detail2 where age=%s",(self.var_age.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","Invalide employee id,try again with another ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_detail2 where age=%s",(self.var_age.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.clear2()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    
    def clear2(self):
        self.var_age.set('')
        self.var_gender.set('')
        self.var_dob.set('')  
        self.var_doj.set('')          
    
    
    def update2(self): 
        if self.var_age.get()=='':
            messagebox.showerror("ERROR","Employee  age re isquired")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_detail2 where age=%s",(self.var_age.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","This Employee ID is invalid ,try again with another ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_detail2` SET `gender`=%s,`dob`=%s,`doj`=%s WHERE `age`=%s",
                    (  
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_age.get()
                        
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Updated Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                    
    
    
    def employee_frame3(self):
       # self.root3=Tk()
        #self.root3.title("Employee Payroll Management System")
        #self.root3.geometry("1350x700+0+0")
        #self.root3.config(bg="white")
        #title=Label(self.root,text="Employee Payroll Mangement System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10)
        #title.place(x=0,y=0,relwidth=1)
        
        
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="#F8F8FF")
        Frame3.place(x=10,y=200,width=1325,height=620)
        
        
        
        lbl_address=Label(Frame3,text="E-MAIL",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_address.place(x=50,y=150,width=300,height=50)
        txt_address=Entry(Frame3,font=("times new roman",25),textvariable=self.var_email,bg="#ffff00",fg="black")
        txt_address.place(x=380,y=150,width=300,height=50)
        
        
        lbl_phone=Label(Frame3,text="PHONE NO.",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_phone.place(x=50,y=50,width=300,height=50)
        txt_phone=Entry(Frame3,font=("times new roman",25),textvariable=self.var_contact,bg="#ffff00",fg="black")
        txt_phone.place(x=380,y=50,width=300,height=50)
        
        lbl_email=Label(Frame3,text="ADDRESS",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_email.place(x=50,y=250,width=300,height=50)
        txt_email=Entry(Frame3,font=("times new roman",25),textvariable=self.var_address,bg="#ffff00",fg="black")
        txt_email.place(x=380,y=250,width=300,height=50)
        
        
        lbl_link=Label(Frame3,text="LINKEDIN-ID",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_link.place(x=50,y=350,width=300,height=50)
        txt_link=Entry(Frame3,font=("times new roman",25),textvariable=self.var_linkedin,bg="#ffff00",fg="black")
        txt_link.place(x=380,y=350,width=300,height=50)
        
        
        # BUTTON 
        btn_save3=Button(Frame3,text="SAVE",command=self.add3,font=("times new roman",25),bg="#ff0000",fg="white",padx=10)
        btn_save3.place(x=1050,y=50,width=230,height=60)

        btn_delete3=Button(Frame3,text="DETELE",command=self.delete3, font=("times new roman",25),bg="#00ff00",fg="white",padx=10)
        btn_delete3.place(x=1050,y=150,width=230,height=60)
        
        btn_update3=Button(Frame3,text="UPDATES",command=self.update3, font=("times new roman",25),bg="#8b008b",fg="white",padx=10)
        btn_update3.place(x=1050,y=250,width=230,height=60)
        
        btn_clear3=Button(Frame3,text="CLEAR",command=self.clear3, font=("times new roman",25),bg="#00008b",fg="white",padx=10)
        btn_clear3.place(x=1050,y=350,width=230,height=60)
        
       # self.root3.mainloop()
        
        
        
    def add3(self): 
        if self.var_contact.get()=='':
            messagebox.showerror("ERROR","Employee contact deatail are required")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_contact where contact=%s",(self.var_contact.get()))
                rows=cur.fetchone()
                
                
                if rows!=None:
                    messagebox.showerror("Error","This Employee ID has already available in our record,try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_contact values(%s,%s,%s,%s)",
                    (
                        self.var_contact.get(), 
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_linkedin.get()
                    )
                    )
                    
                    
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Added Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                
    def delete3(self):
        if self.var_contact.get()=='':
            messagebox.showerror("Error"," employee contact must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_contact where contact=%s",(self.var_contact.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","Invalide contact no ,try again with another no",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_contact where contact=%s",(self.var_contact.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.clear3()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                
    
    def clear3(self):
        self.var_contact.set('')
        self.var_email.set('')
        self.var_address.set('')
        self.var_linkedin.set('')
        
        
    def update3(self): 
        if self.var_contact.get()=='':
            messagebox.showerror("ERROR","Employee contact is quired")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_contact where contact=%s",(self.var_contact.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","This Employee ID is invalid ,try again with another ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_contact` SET `email`=%s,`address`=%s,`linkedin`=%s WHERE `contact`=%s",
                    (  
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_linkedin.get(),
                        self.var_contact.get() 
                        
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Updated Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    def employee_frame4(self):
        #self.root4=Tk()
        #self.root4.title("Employee Payroll Management System")
        #self.root4.geometry("1350x700+0+0")
        #self.root4.config(bg="white")
        #title=Label(self.root4,text="Employee Payroll Mangement System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10)
        #title.place(x=0,y=0,relwidth=1)
        
        
        Frame4=Frame(self.root,bd=3,relief=RIDGE,bg="#F0F8FF")
        Frame4.place(x=10,y=200,width=1325,height=620)
        
        #title4=Label(Frame4,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10)
        #title4.place(x=0,y=0,relwidth=1)
        
        
        lbl_pf=Label(Frame4,text="EXPERIENCE",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_pf.place(x=50,y=150,width=300,height=60)
        txt_pf=Entry(Frame4,font=("times new roman",25),textvariable=self.var_experience,bg="#ffff00",fg="black")
        txt_pf.place(x=380,y=150,width=300,height=60)
        
        
        lbl_exp=Label(Frame4,text="PF ID",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_exp.place(x=50,y=50,width=300,height=60)
        txt_exp=Entry(Frame4,font=("times new roman",25),textvariable=self.var_proof_id,bg="#ffff00",fg="black")
        txt_exp.place(x=380,y=50,width=300,height=60)
        
        lbl_hr=Label(Frame4,text="HR LOCATION",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_hr.place(x=50,y=250,width=300,height=60)
        txt_hr=Entry(Frame4,font=("times new roman",25),textvariable=self.var_hr_location,bg="#ffff00",fg="black")
        txt_hr.place(x=380,y=250,width=300,height=60)
        
        
        lbl_status=Label(Frame4,text="STATUS",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_status.place(x=50,y=350,width=300,height=60)
        txt_status=Entry(Frame4,font=("times new roman",25),textvariable=self.var_status,bg="#ffff00",fg="black")
        txt_status.place(x=380,y=350,width=300,height=60)
        
        
        # BUTTON 
        btn_save4=Button(Frame4,text="SAVE",command=self.add4,font=("times new roman",25),bg="#ff0000",fg="white",padx=10)
        btn_save4.place(x=1050,y=50,width=230,height=50)

        btn_delete4=Button(Frame4,text="DETELE",command=self.delete4, font=("times new roman",25),bg="#00ff00",fg="white",padx=10)
        btn_delete4.place(x=1050,y=150,width=230,height=50)
        
        btn_update4=Button(Frame4,text="UPDATES",command=self.update4, font=("times new roman",25),bg="#8b008b",fg="white",padx=10)
        btn_update4.place(x=1050,y=250,width=230,height=50)
        
        btn_clear4=Button(Frame4,text="CLEAR",command=self.clear4, font=("times new roman",25),bg="#00008b",fg="white",padx=10)
        btn_clear4.place(x=1050,y=350,width=230,height=50)
        
        
        
    def add4(self): 
        if self.var_proof_id.get()=='':
            messagebox.showerror("ERROR","Employee proof id is required")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_status where pfid=%s",(self.var_proof_id.get()))
                rows=cur.fetchone()
                
                
                if rows!=None:
                    messagebox.showerror("Error","This proof id has already available in our record,try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_status values(%s,%s,%s,%s)",
                    ( 
                        self.var_proof_id.get(),
                        self.var_experience.get(),
                        self.var_hr_location.get(),
                        self.var_status.get()
                    )
                    )
                    
                    
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Added Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    
    def delete4(self):
        if self.var_proof_id.get()=='':
            messagebox.showerror("Error"," employee proof id must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_status where pfid=%s",(self.var_proof_id.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","Invalide proof id ,try again with another no",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_status where pfid=%s",(self.var_proof_id.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.delete4()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                            
    
    def clear4(self):
        self.var_proof_id.set('')
        self.var_experience.set('')
        self.var_hr_location.set('')
        self.var_status.set('')
    
    def update4(self): 
        if self.var_proof_id.get()=='':
            messagebox.showerror("ERROR","Employee proof  is quired")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_status where pfid=%s",(self.var_proof_id.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","This Employee ID is invalid ,try again with another ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_status` SET `experience`=%s,`hr_location`=%s,`status`=%s WHERE `pfid`=%s",
                    (
                        self.var_experience.get(),
                        self.var_hr_location.get(),
                        self.var_status.get(),
                        self.var_proof_id.get()
                        
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Updated Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    
    
    
    def employee_frame5(self):
        #self.root4=Tk()
        #self.root4.title("Employee Payroll Management System")
        #self.root4.geometry("1350x700+0+0")
        #self.root4.config(bg="white")
        #title=Label(self.root4,text="Employee Payroll Mangement System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10)
        #title.place(x=0,y=0,relwidth=1)
        
        
        Frame4=Frame(self.root,bd=3,relief=RIDGE,bg="#E0FFFF")
        Frame4.place(x=10,y=200,width=1325,height=620)
        
        lbl_month=Label(Frame4,text="Month",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_month.place(x=30,y=10,width=100,height=30)
        txt_month=Entry(Frame4,font=("times new roman",10),textvariable=self.var_month, bg="#ffff00",fg="black")
        txt_month.place(x=140,y=10,width=100,height=30)
        
        lbl_year=Label(Frame4,text="Year",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_year.place(x=270,y=10,width=100,height=30)
        txt_year=Entry(Frame4,font=("times new roman",10),textvariable=self.var_year,bg="#ffff00",fg="black")
        txt_year.place(x=380,y=10,width=100,height=30)
        
        lbl_salary=Label(Frame4,text="Salary",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_salary.place(x=500,y=10,width=100,height=30)
        txt_salary=Entry(Frame4,font=("times new roman",10),textvariable=self.var_salary,bg="#ffff00",fg="black")
        txt_salary.place(x=610,y=10,width=100,height=30)
        
        
        # ****************** Row 2 *********************************
        
        lbl_days=Label(Frame4,text="Total Days",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_days.place(x=30,y=60,width=100,height=30)
        txt_days=Entry(Frame4,font=("times new roman",10),textvariable=self.var_t_days,bg="#ffff00",fg="black")
        txt_days.place(x=180,y=60,width=160,height=30)
        
        lbl_absent=Label(Frame4,text="Absent",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_absent.place(x=410,y=60,width=100,height=30)
        txt_absent=Entry(Frame4,font=("times new roman",10),textvariable=self.var_absent,bg="#ffff00",fg="black")
        txt_absent.place(x=550,y=60,width=160,height=30)
        
        # ****************** Row 3 *********************************
        
        lbl_medical=Label(Frame4,text="Medical",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_medical.place(x=30,y=110,width=100,height=30)
        txt_medical=Entry(Frame4,font=("times new roman",10),textvariable=self.var_medical,bg="#ffff00",fg="black")
        txt_medical.place(x=180,y=110,width=160,height=30)
        
        lbl_pf=Label(Frame4,text="PF",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_pf.place(x=410,y=110,width=100,height=30)
        txt_pf=Entry(Frame4,font=("times new roman",10),textvariable=self.var_pf,bg="#ffff00",fg="black")
        txt_pf.place(x=550,y=110,width=160,height=30)
        
        # ****************** Row 4 *********************************
        
        lbl_convence=Label(Frame4,text="Covence",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_convence.place(x=30,y=160,width=100,height=30)
        txt_convence=Entry(Frame4,font=("times new roman",10),textvariable=self.var_convence,bg="#ffff00",fg="black")
        txt_convence.place(x=150,y=160,width=160,height=30)
        
        lbl_netsalary=Label(Frame4,text="Net Salary",font=("times new roman",15),bg="#191870",fg="white",padx=10)
        lbl_netsalary.place(x=410,y=160,width=100,height=30)
        txt_netsalary=Entry(Frame4,font=("times new roman",10),textvariable=self.var_net_salary,bg="#ffff00",fg="black")
        txt_netsalary.place(x=550,y=160,width=160,height=30)
        
        btn_save5=Button(Frame4,text="SAVE",command=self.add5,font=("times new roman",25),bg="#ff0000",fg="white",padx=10)
        btn_save5.place(x=1050,y=50,width=230,height=60)

        btn_delete5=Button(Frame4,text="DETELE",command=self.delete5, font=("times new roman",25),bg="#00ff00",fg="white",padx=10)
        btn_delete5.place(x=1050,y=150,width=230,height=60)
        
        btn_update5=Button(Frame4,text="UPDATES",command=self.update5, font=("times new roman",25),bg="#8b008b",fg="white",padx=10)
        btn_update5.place(x=1050,y=250,width=230,height=60)
        
        btn_clear5=Button(Frame4,text="CLEAR",command=self.clear5,font=("times new roman",25),bg="#00008b",fg="white",padx=10)
        btn_clear5.place(x=800,y=150,width=230,height=60)
        
        
        btn_calculate=Button(Frame4,text="Calculate",command=self.calculate, font=("times new roman",25),bg="orange",fg="white",padx=10)
        btn_calculate.place(x=800,y=50,width=230,height=60)
        
        btn_print=Button(Frame4,text="PRINT",command=self.update, font=("times new roman",25),bg="#00bfff",fg="white",padx=10)
        btn_print.place(x=800,y=250,width=230,height=60)
        
        lbl_Name=Label(Frame4,text="Employee Id",font=("times new roman",32),bg="#191870",fg="white",padx=10)
        lbl_Name.place(x=800,y=350,width=230,height=60)
        txt_Name=Entry(Frame4,font=("times new roman",25),textvariable=self.var_emp_code,bg="#ffff00",fg="black")
        txt_Name.place(x=1050,y=350,width=230,height=60)
        
        
        
        
        self.var_txt=StringVar()
        self.var_operator=''
        
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)  
        
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator='' 
            
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
        
        
        cal_Frame=Frame(Frame4,bg="white",bd=2,relief=RIDGE)
        cal_Frame.place(x=5,y=200,width=270,height=280)
        
        txt_Result=Entry(cal_Frame,bg="lightyellow",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT)
        txt_Result.place(x=0,y=0,relwidth=1,height=58)
        
        
        
        
        
        btn_7=Button(cal_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold"))
        btn_7.place(x=0,y=42,width=65,height=56)
        
        btn_8=Button(cal_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold"))
        btn_8.place(x=67,y=42,width=65,height=56)
        
        btn_9=Button(cal_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold"))
        btn_9.place(x=133,y=42,width=65,height=56)
        
        btn_div=Button(cal_Frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold"))
        btn_div.place(x=200,y=42,width=65,height=56)
        
        btn_4=Button(cal_Frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold"))
        btn_4.place(x=0,y=100,width=65,height=56)
        
        btn_5=Button(cal_Frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold"))
        btn_5.place(x=67,y=100,width=65,height=56)
        
        btn_6=Button(cal_Frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold"))
        btn_6.place(x=133,y=100,width=65,height=56)
        
        btn_mul=Button(cal_Frame,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold"))
        btn_mul.place(x=200,y=100,width=65,height=56)
        
        btn_1=Button(cal_Frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold"))
        btn_1.place(x=0,y=159,width=65,height=56)
        
        btn_2=Button(cal_Frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold"))
        btn_2.place(x=67,y=159,width=65,height=56)
        
        btn_3=Button(cal_Frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold"))
        btn_3.place(x=133,y=159,width=65,height=56)
        
        btn_min=Button(cal_Frame,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold"))
        btn_min.place(x=200,y=159,width=65,height=56)
        
        
        btn_0=Button(cal_Frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold"))
        btn_0.place(x=0,y=215,width=65,height=56)
        
        btn_dot=Button(cal_Frame,text='C',command=clear_cal,font=("times new roman",15,"bold"))
        btn_dot.place(x=67,y=215,width=65,height=56)
        
        btn_sum=Button(cal_Frame,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold"))
        btn_sum.place(x=133,y=215,width=65,height=56)
        
        btn_equal=Button(cal_Frame,text='=',command=result,font=("times new roman",15,"bold"))
        btn_equal.place(x=200,y=215,width=65,height=56)
        
        sal_frame=Frame(Frame4,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=280,y=200,width=435,height=280)
        
        
        title_sal=Label(sal_frame,text="Salary Reciept",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10)
        title_sal.place(x=0,y=0,relwidth=1)
        
        sal_frame2=Frame(sal_frame,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=38,width=430,height=230)
        
        sample=f'''\t Company Name: xyz\n\tAddress: Xyz,
...............................................................................

Employee ID\t\t:
salary on\t\t:  MM-YYYY  
Generated on\t\t:  DD-MM-YYYY  

...............................................................................

Total Days\t\t:  DD  
Total Present\t\t:  DD  
Total Absent\t\t:  Rs,----  
convence\t\t:  Rs,----
Medical\t\t:  Rs,---     
Gross Payment\t\t:  Rs,---
Net Salary\t\t:  Rs,---

...............................................................................

This is computer slip, not
required any signature
'''  
        #self.txt_salary_reciept.delete('1.0',END)
        #self.txt_salary_reciept.insert(END,new_sample)
           
        
        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL,width=25)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        
        self.txt_salary_reciept=Text(sal_frame2,font=("times new roman",15),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,sample)
        
    
       
        #self.txt_salary_reciept.delete('1.0',END)
        #self.txt_salary_reciept.insert(END,sample)
        
        
        
        #self.txt_salary_reciept=Text(sal_frame2,font=("times new roman",15),bg="lightyellow",yscrollcommand=scroll_y.set)
        #self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        #scroll_y.config(command=self.txt_salary_reciept.yview)
        #self.txt_salary_reciept.insert(END,new_sample)
        
        
        #self.check_connection()
        #scroll_y=Scrollbar(sal_frame2,orient=VERTICAL,width=25)
        #scroll_y.pack(fill=Y,side=RIGHT)
    
    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='':
            messagebox.showerror('Error','All field are required')
        else:
            per_day=int(self.var_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal-deduct+addition
            self.var_net_salary.set(str(round(net_sal,2)))
            
            new_sample=f'''\t Company Name: xyz\n\tAddress: Xyz,
...............................................................................

Employee ID\t\t:  {self.var_emp_code.get()}
salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}  
Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
 

...............................................................................

Total Days\t\t:  {self.var_t_days.get()} 
Total Present\t\t:  {str(int(self.var_t_days.get())-int(self.var_absent.get()))} 
Total Absent\t\t:  {self.var_absent.get()}  
convence\t\t:  Rs,{self.var_convence.get()}
Medical\t\t:  Rs,{self.var_medical.get()}     
Gross Payment\t\t:  Rs,{self.var_salary.get()}
Net Salary\t\t:  Rs,{self.var_net_salary.get()}

...............................................................................

This is computer slip, not
required any signature
'''             
            self.txt_salary_reciept.delete('1.0',END)
            self.txt_salary_reciept.insert(END,new_sample)           
    
    def add5(self): 
        if self.var_emp_code.get()=='':
            messagebox.showerror("ERROR","Employee proof id is required")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                
                
                if rows!=None:
                    messagebox.showerror("Error","This proof id has already available in our record,try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    ( 
                        self.var_emp_code.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        
                    )
                    )
                    
                    
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Added Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    
    def delete5(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error"," employee Employee id must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","Invalide proof id ,try again with another no",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.delete5()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    def clear5(self):
        self.var_emp_code.set('')
        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        #self.var_salary.set(''),
    
    
    def update5(self): 
        if self.var_emp_code.get()=='':
            messagebox.showerror("ERROR","Employee ID  is quired")
            
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee')
                cur=con.cursor()
                cur.execute("select  * from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                
                if rows==None:
                    messagebox.showerror("Error","This Employee ID is invalid ,try again with another ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `month`=%s,`year`=%s,`salary`=%s,`total_days`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s WHERE `emp_code`=%s",
                    (
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_code.get()
                        
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Record Updated Successfully")
                
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                
                
   
    
    
    
           
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()
