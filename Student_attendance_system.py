attendance = {}

def mark_attendance(name, status):
    attendance[name] = status

def show_attendance():
    if not attendance:
        print("No attendance data")
    else:
        for name, status in attendance.items():
            print(name, ":", status)

def count_present():
    count = 0
    for status in attendance.values():
        if status == "Present":
            count += 1
    print("Total Present Students:", count)

print("---- STUDENT ATTENDANCE SYSTEM ----")

while True:
    print("\n1. Mark Attendance")
    print("2. Show Attendance")
    print("3. Count Present Students")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Student Name: ")
        status = input("Enter Present or Absent: ")
        mark_attendance(name, status)

    elif choice == 2:
        show_attendance()

    elif choice == 3:
        count_present()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
