import pickle

def add():
    with open("emp.dat","ab") as f:
        eidno = int(input("Enter employee number: "))
        ename = input("Enter employee name: ")
        esal = int(input("Enter employee salary: "))
        emp = [eidno,ename,esal]
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

def updateesal():
	with open("emp.dat","rb+") as f:
		try:
			found = False
			eid= int(input("Enter eid to update: "))
			while True:
				orig = f.tell()
				emp = pickle.load(f)
				if emp[0] == eid:
					f.seek(orig)
					emp[2] = int(input("Enter new salary: "))
					found= True
					pickle.dump(emp,f)
		except EOFError:
			pass
		if not found:
			print("Not found")
		

	
while True:
    ch = input("Enter choice:\n1. Add record\n2. Update record\n3. Display record: ")
    if ch == "1":
        add()
    elif ch == "2":
        updateesal()
    elif ch == "3":
        display()
