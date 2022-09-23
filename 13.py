import pickle

def search_records():
    with open("emp.dat", "rb") as f:
        found = False
        try:
            ecode = int(input("Enter employee code to search: "))
            while True:
                emp = pickle.load(f)
                if emp["ecode"] == ecode:
                    empcode = emp["ecode"]
                    name = emp["ename"]
                    place = emp["eplace"]
                    salary = emp["esal"]
                    found = True
                    print(empcode, name,place, salary)
        except EOFError:
            pass
        if not found:
            print("Not Found")

def write_records():
    with open("emp.dat","ab") as f:
        n = int(input("Enter number of employees to be entered: "))
        for i in range(n):
            empcode = int(input("Enter employee code: "))
            name = input("Enter employee name: ")
            place = input("Enter employee place: ")
            salary = int(input("Enter employee salary: "))

            emp = {}
            emp["ecode"] = empcode
            emp["ename"] = name
            emp["eplace"] = place
            emp["esal"] = salary
            pickle.dump(emp,f)

while True:
    ch = input("Enter choice:\n1. Search record\n2. Write record: ")
    if ch == "1":
        search_records()
    elif ch == "2":
        write_records()
    else:
        print("Invalid choice")
