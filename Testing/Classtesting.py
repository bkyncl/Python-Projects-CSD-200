
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

       
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay *  self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees =None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--', emp.fullname())


dev_1 = Developer('Corey', 'Smith', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

manager_1 = Manager('Bob', 'John', 80000, [dev_1])
manager_2 = Manager('Test2', 'Manager', 90000)

manager_1.add_employee(dev_2)
manager_1.remove_employee(dev_1)
manager_1.print_emps()
print(dev_1)
