from employee import Employee

class LeadDeveloper(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        return base_pay + self.bonus
