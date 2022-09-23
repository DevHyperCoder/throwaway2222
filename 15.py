import csv

def search_record():
    with open("emp.csv", "r") as f:
        csv_r = csv.reader(f)
        ecode = int(input("Enter ecode: "))
        found = False
        for i in csv_r:
            if int(i[0]) == ecode:
                found = True
                ecode = i[0]
                ename = i[1]
                esal = i[2]
                print(ecode,ename,esal)
        if not found:
            print("Not found")

def write_records():
    with open("emp.csv", "a") as f:
        csv_w = csv.writer(f)

        n = int(input("Enter number of employees to add: "))

        for i in range(n):
            empcode = int(input("Enter employee code: "))
            name = input("Enter employee name: ")
            salary = int(input("Enter employee salary: "))

            emp = [empcode,name,salary]
            csv_w.writerow(emp)


while True:
    ch = input("Enter choice:\n1. Search record\n2. Write record: ")
    if ch == "1":
        search_record()
    elif ch == "2":
        write_records()
    else:
        print("Invalid choice")
