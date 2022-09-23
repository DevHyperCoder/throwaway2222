s = []

def push():
	emid = int(input("Enter id: "))
	emname = input("Enter name: ")
	emsal = int(input("Enter salary: "))
	emp = [emid,emname,emsal]
	s.append(emp)

def pop():
    if len(s) == 0:
        print("Underflow")
        return

    emp = s.pop()
    emid = emp[0]
    emname = emp[1]
    emsal =  emp[2]

    print("The employee to be popped is: ")
    print("Id: ",emid)
    print("Name: ",emname)
    print("Salary: ",emsal)

while True:
    ch = input("Menu:\n1. Push\n2. Pop: ")
    if ch == "1":
        push()
    elif ch == "2":
        pop()
    else:
        print("invalid input")
