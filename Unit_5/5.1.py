class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12 
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def annual_salary(self):
        return (self.salary * 12) + self.bonus
    
class Developer(Employee):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects

    def annual_salary(self):
        base_salary = self.salary * 12
        return base_salary + (self.projects * 1000)
Manager = Manager("Alice", 6000, 5000)
Developer = Developer("Bob", 5000, 3)

total_annual_salary = Manager.annual_salary() + Developer.annual_salary()
print(total_annual_salary)