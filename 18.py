import pickle
import os

def writerecord():
    rollno = int(input("Enter roll: "))
    name = input("Enter name: ")
    mark = int(input("Enter marks: "))

    with open("stu.dat","ab") as f:
        stu = [rollno,name,mark]
        pickle.dump(stu,f)

def display():
    with open("stu.dat", "rb") as f:
        try:
            while True:
                stu = pickle.load(f)
                rollno = stu[0]
                name = stu[1]
                mark = stu[2]

                print(rollno, name, mark)
        except EOFError:
            pass

def remove():
    f = open("stu.dat","rb")
    new_f = open("stu_backup.dat","wb")
	
    try:
        roll= int(input("Enter roll to delete: "))
        while True:
            stu = pickle.load(f)
            if stu[0] == roll:
                continue
            pickle.dump(stu,new_f)
    except EOFError:
        pass
	
    f.close()
    new_f.close()

    os.remove("stu.dat")
    os.rename("stu_backup.dat","stu.dat")

	
while True:
    ch = input("Enter choice:\n1. Add record\n2. Remove record\n3. Display record: ")
    if ch == "1":
        writerecord()
    elif ch == "2":
        remove()
    elif ch == "3":
        display()

