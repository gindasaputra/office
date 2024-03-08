class Employee:
    def __init__(self, name, position, email):
        self.name = name
        self.position = position
        self.email = email

class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        print(f"List of Employees at {self.name}:")
        for employee in self.employees:
            print(f"Name: {employee.name}, Position: {employee.position}, Email: {employee.email}")

def main():
    office_name = input("Enter the name of your office: ")
    office = Office(office_name)

    while True:
        print("\n1. Add Employee")
        print("2. List Employees")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            email = input("Enter employee email: ")
            employee = Employee(name, position, email)
            office.add_employee(employee)
            print("Employee added successfully!")
        elif choice == "2":
            office.list_employees()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
