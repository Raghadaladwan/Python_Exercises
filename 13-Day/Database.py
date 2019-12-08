import sqlite3
from tkinter import Toplevel, Label, Entry, scrolledtext, Menu, Button, StringVar, mainloop, Tk

conn = sqlite3.connect('OrgDB.db')

c = conn.cursor()


# c.execute('''CREATE TABLE employees
#          (EmployeeNumber int,EmployeeName text,EmployeeGender text,EmployeeNationality text,EmployeeDateofBirth text,EmployeeAddress text,EmployeeDepartment text,EmployeeSalary text)''')
#
# conn.commit()

# --------------------------------------------


def Add_Employee():
    newChild = Toplevel(root)
    newChild.geometry("1000x700")

    def add_new_emp():
        c.execute("INSERT INTO employees VALUES (?,?,?,?,?,?,?,?)",
                  (int(input_Employee_Number.get()), input_Employee_Name.get(), input_Employee_Gender.get(),
                   input_Employee_Natoiality.get(), input_Employee_DateofBirth.get(),
                   input_Employee_Address.get(), input_Employee_Department.get(), input_Employee_Salary.get()))

    label_Employee_Number = Label(newChild, text="Employee_Number")
    label_Employee_Number.grid(row=0, column=0)

    input_Employee_Number = StringVar()
    input_Employee_Number = Entry(newChild, textvariable=input_Employee_Number)
    input_Employee_Number.grid(row=0, column=1)
    # ------------------
    label_Employee_Name = Label(newChild, text="Employee_Name")
    label_Employee_Name.grid(row=1, column=0)

    input_Employee_Name = StringVar()
    input_Employee_Name = Entry(newChild, textvariable=input_Employee_Name)
    input_Employee_Name.grid(row=1, column=1)
    # ------------------

    label_Employee_Gender = Label(newChild, text="Employee_Gender")
    label_Employee_Gender.grid(row=2, column=0)

    input_Employee_Gender = StringVar()
    input_Employee_Gender = Entry(newChild, textvariable=input_Employee_Gender)
    input_Employee_Gender.grid(row=2, column=1)
    # ------------------
    label_Employee_Natoiality = Label(newChild, text="Employee_Natoiality")
    label_Employee_Natoiality.grid(row=3, column=0)

    input_Employee_Natoiality = StringVar()
    input_Employee_Natoiality = Entry(newChild, textvariable=input_Employee_Natoiality)
    input_Employee_Natoiality.grid(row=3, column=1)
    # ------------------

    label_Employee_DateofBirth = Label(newChild, text="Employee_DateofBirth")
    label_Employee_DateofBirth.grid(row=4, column=0)

    input_Employee_DateofBirth = StringVar()
    input_Employee_DateofBirth = Entry(newChild, textvariable=input_Employee_DateofBirth)
    input_Employee_DateofBirth.grid(row=4, column=1)
    # ------------------
    label_Employee_Address = Label(newChild, text="Employee_Address")
    label_Employee_Address.grid(row=5, column=0)

    input_Employee_Address = StringVar()
    input_Employee_Address = Entry(newChild, textvariable=input_Employee_Address)
    input_Employee_Address.grid(row=5, column=1)

    # ------------------
    label_Employee_Department = Label(newChild, text="Employee_Department")
    label_Employee_Department.grid(row=6, column=0)

    input_Employee_Department = StringVar()
    input_Employee_Department = Entry(newChild, textvariable=input_Employee_Department)
    input_Employee_Department.grid(row=6, column=1)

    # ------------------
    label_Employee_Salary = Label(newChild, text="Employee_Salary")
    label_Employee_Salary.grid(row=7, column=0)

    input_Employee_Salary = StringVar()
    input_Employee_Salary = Entry(newChild, textvariable=input_Employee_Salary)
    input_Employee_Salary.grid(row=7, column=1)

    btn = Button(newChild, text="Save", command=add_new_emp)
    btn.grid(row=8, column=0)


# ---------------------
def View_Employee():
    print("View")

    newChild = Toplevel(root)
    newChild.geometry("1000x700")

    st = scrolledtext.ScrolledText(newChild)
    st.pack()
    fmt = '{:<8}{:<20}{}'


"""
    for i, (Name, Address , Salary , Jop) in enumerate(zip(Employee_Name, Employee_Address , Employee_Salary , Employee_Jop)):

        st.insert(INSERT, 'Number : '+str(i)+"  Name : "+ Name + '  Address : '+Address + ' Salary : '+Salary+ ' Jop : '+ Jop +"\n" )
"""

root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.geometry("1000x700")

Employees_menu = Menu(menu)
menu.add_cascade(label="Employees", menu=Employees_menu)
Employees_menu.add_command(label="Add", command=Add_Employee)
Employees_menu.add_command(label="View", command=View_Employee)

conn.commit()

mainloop()



def View_Employee():
    print("View")
    newChild = Toplevel(root)
    newChild.geometry("1000x700")
    list=c.execute("SELECT * FROM employees")
    for row in list:
        print(row)
    r=0
    for m in list:
         Label(text=m).grid(row=r,column=0)
         r = r + 1

conn.close()
