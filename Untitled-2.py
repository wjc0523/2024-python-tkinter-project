import tkinter as tk
from tkinter import *
from string import *
from time import *

#SETTING UP WINDOW
self=tk.Tk()
self.title("SENIORITIS TEST")
self.geometry("400x460+300+300")
self.resizable(True,True)



    

#GLOBAL VARIABLES

avg_gpa=0.0
cnt=0
score=0.0
#INPUT VARIABLES
name_var=StringVar()
class_of_var=IntVar()
classes_var=IntVar()
gpa_multi_var=DoubleVar()
academic_status=BooleanVar()


#SENIOR(USER) CLASS
class senior:
    
    global avg_gpa
    global score
    
    def __init__(self,name,class_of,classes,gpa):
        self.name=name
        self.class_of=class_of
        self.classes=classes
        self.gpa=gpa
    def edit_name(self,name):
        self.name=name
    def return_name(self):
        return self.name
    def edit_class_of(self,class_of):
        self.class_of=class_of
    def edit_classes(self,classes):
        self.classes=classes
    def edit_gpa(self):
        self.gpa=avg_gpa/self.classes
    def score_calculate(self):
        score=0.0
        score=score+self.gpa
        if self.classes>4:
            score=score+10
        if self.gpa<3.0:
            score=score-20
        
    
class graduate(senior):
    
    global avg_gpa
    global score
    
    def __init__(self,name,class_of,classes,gpa,academic_status):
        super().__init__(name,class_of,classes,gpa)
        self.academic_status=academic_status
    def gscore_calculate(self):
        score=0.0
        score=score+self.gpa
        if self.academic_status==False:
            score=score-20.0
        if self.classes>4:
            score=score+10
        if self.gpa<3.0:
            score=score-20
        

def gpa_entry_func():
    
    
    global avg_gpa
    global cnt
    global self
    number_confirm.pack_forget()
    cnt=cnt+1
    if cnt>classes_var.get():
        if class_of_var.get()<=2024:
            ge_text=Label(self,text="DID YOU GRADUATE? TYPE ""True"" or ""False"" ",font=("Mono Lisa",10),relief="flat")
            ge_text.place(x=90,y=330)
            graduate_entry=Entry(self,textvariable = academic_status,font=('Mona Lisa',8,'normal'),width=8)
            graduate_entry.place(x=140,y=360)
        register=Button(self,text="Test Now",fg="Black",bg="White",command=submit)
        register.place(x=140,y=400)
        return
    c_label=Label(self,text="ENTER YOUR GPA FOR CLASS "+str(cnt)+"\n (IN DECIMALS)",font=("Mono Lisa",10),relief="flat")
    c_label.place(x=80,y=280)
    gp_entry=Entry(self,textvariable = gpa_multi_var,font=('Mona Lisa',8,'normal'),width=8)
    gp_entry.place(x=140,y=310)
   
    r_class.place(x=190,y=310)
    avg_gpa=avg_gpa+gpa_multi_var.get()
    
#GPA Entry functions

r_class=Button(self,text="NEXT",fg="Black",bg="White",command=gpa_entry_func)

def pop_up():
    #POP-UP WINDOW
    pu=Tk()
    if score <13.0 and class_of_var.get()>2024:
        ge1_text=Label(pu,text=s.return_name()+" IS SENIORITIS",font=("Mono Lisa",15),fg="Red",relief="flat")
        ge1_text.place(x=0,y=30)
    elif score >13.0 and class_of_var.get()>2024 :
        ge2_text=Label(pu,text=s.return_name()+" ISN'T SENIORITIS",font=("Mono Lisa",15),fg="Green",relief="flat")
        ge2_text.place(x=0,y=30)
    elif score <13.0 and class_of_var.get()<2024 :
        ge3_text=Label(pu,text=g.return_name()+" IS SENIORITIS",font=("Mono Lisa",15),fg="Red",relief="flat")
        ge3_text.place(x=0,y=30)
    elif score >13.0 and class_of_var.get()<2024 :
        ge4_text=Label(pu,text=g.return_name()+" ISN'T SENIORITIS",font=("Mono Lisa",15),fg="Green",relief="flat")
        ge4_text.place(x=0,y=30)
    pu.mainloop()
        
        
#Submit function
def submit():
    if class_of_var.get()>2024:
       
        s.edit_name(name_var.get())
        s.edit_class_of(class_of_var.get())
        s.edit_classes(classes_var.get())
        s.edit_gpa()
        s.score_calculate()
    else:
       
        g.edit_name(name_var.get())
        g.edit_class_of(class_of_var.get())
        g.edit_classes(classes_var.get())
        g.edit_gpa()
        g.gscore_calculate()

    pop_up()
    


#SENIOR MANAGEMENT
s=senior("SENIOR",2024,8,4.0)
#GRADUATE MANAGEMENT
g=graduate("GRADUATE",2024,3,4.0,False)

    
#Main title grid
title=Label(self,text="SENIORITIS TEST",font=("Mono Lisa",20),relief="flat")
title.grid(column=0,row=0) 
title.pack() 

name_label=Label(self,text="NAME",font=("Mono Lisa",10),relief="flat")
name_label.place(x=140,y=80) 
class_of_label=Label(self,text="CLASS OF",font=("Mono Lisa",10),relief="flat")
class_of_label.place(x=140,y=120)
classes_label=Label(self,text="NUMBER OF CLASSES",font=("Mono Lisa",10),relief="flat")
classes_label.place(x=140,y=160)  



name_entry=Entry(self,textvariable = name_var, font=('Mona Lisa',8,'normal'),width=15)
class_of_entry=Entry(self,textvariable = class_of_var,font=('Mona Lisa',8,'normal'),width=15)
classes_entry=Entry(self,textvariable = classes_var,font=('Mona Lisa',8,'normal'),width=15)
repeat=classes_var.get()

#Test now interface
number_confirm=Button(self,text="Enter",fg="Black",bg="White",command=gpa_entry_func)
name_entry.place(x=140,y=100)
class_of_entry.place(x=140,y=140)
classes_entry.place(x=140,y=180)
number_confirm.place(x=240,y=180)


#Run
self.mainloop()

        


        




        





        
    
        
        

        
    



    