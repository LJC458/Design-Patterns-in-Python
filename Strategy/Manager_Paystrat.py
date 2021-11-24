from Strategy_interface import IStrategy

class Manager_Pay(IStrategy):
    def calculate(self, Employee):
        return 2.00