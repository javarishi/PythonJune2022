class Employee:

    def __init__(self, empId=999, empName="Dummy Emp", empLocation="Dummy Location"):
        print("This is Employee Constructor")
        self.emp_id = empId
        self.emp_name = empName
        self.emp_location = empLocation

    # methods - functions
    def hr_function(self):
        print("Emp HR Function ", self.emp_id)

# instanceName = Classname()
emp_101 = Employee(101, "Richard", "Remote")
emp_1010 = Employee(101, "Richard", "Remote")


emp_201 = Employee(201, "Brian", "WFO")
emp_201.hr_function()

emp_301 = Employee(empLocation="Atlanta", empId=301, empName="Paul")

emp_999 = Employee()
print(emp_101.emp_id, emp_101.emp_name, emp_101.emp_location)
print(emp_301.emp_id, emp_301.emp_name, emp_301.emp_location)
print(emp_201.emp_id, emp_201.emp_name, emp_201.emp_location)
print(emp_999.emp_id, emp_999.emp_name, emp_999.emp_location)
emp1020 = emp_101
print("emp_101" , type(emp_101), id(emp_101))
print("emp_1010" , type(emp_1010), id(emp_1010))
print("emp1020" , type(emp1020), id(emp1020))
# <class 'method'> - function in class is instance of method class
print(type(emp_101.hr_function))

if emp_101 == emp1020:
    print("Emp are same")
else:
    print("Emp are different")
