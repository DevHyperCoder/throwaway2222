import pickle

def read_records():
    with open("emp.dat", "rb") as f:
        try:
            while True:
                emp = pickle.load(f)
                empcode = emp[0]
                name = emp[1]
                place = emp[2]
                salary = emp[3]

                print(empcode, name,place, salary)
        except EOFError:
            pass

def write_records():
    with open("emp.dat","ab") as f:
        n = int(input("Enter number of employees to be entered: "))
        for i in range(n):
            empcode = int(input("Enter employee code: "))
            name = input("Enter employee name: ")
            place = input("Enter employee place: ")
            salary = int(input("Enter employee salary: "))

            emp = [empcode,name,place,salary]
            pickle.dump(emp,f)

while True:
    ch = input("Enter choice:\n1. Read record\n2. Write record: ")
    if ch == "1":
        read_records()
    elif ch == "2":
        write_records()
    else:
        print("Invalid choice")

