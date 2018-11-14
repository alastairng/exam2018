class Employee:
    """
    the base class
    """
    _id = 0

    def __init__(self, name):
        self.name = name
        self.id = self._id; self._id += 1

    def get_name(self):
        return self.name 

    def weekly_pay(self, hours_worked):
        self.hours_worked = hours_worked
        return self.hours_worked 


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        if hours_worked > 40:
            return (self.hourly_rate * 40) + ((hours_worked - 40 ) * self.hourly_rate * 1.5)
        else:
            return self.hourly_rate * hours_worked



class Exempt_Employee(Employee):

    def __init__(self, name, annual_salary):
        self.name = name
        self.annual_salary = annual_salary

    def weekly_pay(self, annual_salary):
        return self.annual_salary/52
        

class Manager(Exempt_Employee):
    
    def __init__(self, name, annual_salary, bonus):
        self.name = name
        self.annual_salary = annual_salary
        self.bonus = bonus

    
    def weekly_pay(self, bonus):
        return (self.annual_salary + self.bonus)/52



def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)


if __name__ == '__main__':
    main()
