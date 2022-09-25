import pickle
import os

def writerecord():
    with open("emp.dat","ab") as f:

        enono = int(input("Enter no: "))
        ename = input("Enter name: ")
        esal = int(input("Enter salary: "))

        emp =[enono,ename,esal] 
        pickle.dump(emp,f)

def display():
    with open("emp.dat", "rb") as f:
        try:
            while True:
                emp = pickle.load(f)
                empcode = emp[0]
                name = emp[1]
                salary = emp[2]

                print(empcode, name, salary)
        except EOFError:
            pass

def remove():
    f = open("emp.dat","rb")
    new_f = open("emp_backup.dat","wb")

    try:
        eno= int(input("Enter employee number to delete: "))
        while True:
            emp = pickle.load(f)
            if emp[0] == eno:
                continue
            pickle.dump(emp,new_f)
    except EOFError:
        pass

    f.close()
    new_f.close()
    os.remove("emp.dat")
    os.rename("emp_backup.dat","emp.dat")

	
while True:
    ch = input("Enter choice:\n1. Add record\n2. Remove record\n3. Display record: ")
    if ch == "1":
        writerecord()
    elif ch == "2":
        remove()
    elif ch == "3":
        display()
	
