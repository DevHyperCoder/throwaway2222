s = []

def push():
	bid = int(input("Enter id: "))
	bname = input("Enter name: ")
	bauthor = input("Enter author: ")
	book =[bid,bname,bauthor]
	s.append(book)


def pop():
    if len(s) == 0:
        print("Underflow")
        return

    bp = s.pop()
    bid = bp[0]
    bname = bp[1]
    bauthor =  bp[2]

    print('The book to be popped is: ')
    print("Id: ",bid)
    print("Name: ",bname)
    print("Author: ",bauthor)

while True:
    ch = input("Menu:\n1. Push\n2. Pop: ")
    if ch == "1":
        push()
    elif ch == "2":
        pop()
    else:
        print("invalid input")
