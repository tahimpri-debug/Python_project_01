students = {}

def add_student(name , marks):
    students[name] = marks

def show_student():
    print(students)

def hights_marks ():
    top = max(students, key= students.get)
    print(top, ":" , students[top]) 

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Hights Marks")
    print("4. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        name = input("Name : ")
        marks = int(input("Marks :"))
        add_student (name, marks)
    elif choice == 2:
        show_student()
    elif choice == 3:
        hights_marks()
    elif choice == 4:
        break