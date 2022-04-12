from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    @abstractmethod
    def compute_salary(self):
        pass


class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super(FulltimeEmployee, self).__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def compute_salary(self):
        return self.salary + 200

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, value):
        super(HourlyEmployee, self).__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.value = value

    def get_worked_hours(self):
        return self.worked_hours
    def set_worked_hours(self, new_worked_hours):
        self.worked_hours = new_worked_hours

    def get_value(self):
        return self.value
    def set_value(self, new_value):
        self.value = new_value

    def compute_salary(self):
        return self.worked_hours * self.value

class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def get_employee_list(self):
        return self.employee_list

    def print_payroll(self):
        for e in self.employee_list:
            print(f"Nome: {e.full_name()}\nSalário: {e.compute_salary()}")

if __name__ == '__main__':
    #Employee1 = Employee("Joao", "Lucca") <- não posso criar um objeto direto da classe abstrata
    employeer1 = FulltimeEmployee("Joao", "Silva", 2000)
    print("Primeiro nome:", employeer1.first_name)
    print("Nome completo:", employeer1.full_name())
    print("Salário fixo:", employeer1.get_salary())
    print("Salário total:", employeer1.compute_salary())
    employeer2 = HourlyEmployee("Marcelo", "Ribeiro", 6, 150)
    print("Primeiro nome:", employeer2.first_name)
    print("Nome completo:", employeer2.full_name())
    print("Saláriooooo:", employeer2.compute_salary())
    payroll = Payroll()
    payroll.add(employeer1)
    payroll.add(employeer2)
    payroll.print_payroll()
    print(payroll.get_employee_list())
