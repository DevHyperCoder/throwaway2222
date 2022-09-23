import pickle

def add():
    with open("stu.dat","ab") as f:
        rollno = int(input("Enter roll: "))
        name = input("Enter name: ")
        mark = int(input("Enter marks: "))
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

def updatemark():
	with open("stu.dat","rb+") as f:
		try:
			found = False
			roll= int(input("Enter roll to update: "))
			while True:
				orig = f.tell()
				stu = pickle.load(f)
				if stu[0] == roll:
					f.seek(orig)
					stu[2] = int(input("Enter new mark: "))
					found= True
					pickle.dump(stu,f)
		except EOFError:
			pass
		if not found:
			print("Not found")
		

	
while True:
    ch = input("Enter choice:\n1. Add record\n2. Update record\n3. Display record: ")
    if ch == "1":
        add()
    elif ch == "2":
        updatemark()
    elif ch == "3":
        display()
        
