from employee import Employee

class JuniorDeveloper(Employee):
    def __init__(self, name, salary, overtime_hours):
        super().__init__(name, salary)
        self.overtime_hours = overtime_hours

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        #overtime_pay = overtime_pay for self.overtime_hours * (self.salary / 160) * 1.5 else 
        overtime_pay = self.overtime_hours * (self.salary / 160) * 1.5
        return base_pay + overtime_pay
