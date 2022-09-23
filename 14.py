import csv

def read_record():
    with open("emp.csv", "r") as f:

        csv_r = csv.reader(f)
        for i in csv_r:
            ecode = i[0]
            ename = i[1]
            esal = i[2]
            print(ecode,ename,esal)

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
    ch = input("Enter choice:\n1. Read record\n2. Write record: ")
    if ch == "1":
        read_record()
    elif ch == "2":
        write_records()
    else:
        print("Invalid choice")
