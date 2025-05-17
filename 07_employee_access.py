class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = name


#test
emp = Employee("John", 50000, "123-45-6789")

print(emp.name)            # Accessible
print(emp._salary)         # Accessible but discouraged    
print(emp._Employee__ssn)  # Correct way to access private 