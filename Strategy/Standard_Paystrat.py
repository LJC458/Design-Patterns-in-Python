from Strategy_interface import IStrategy

class standard_Pay(IStrategy):
    def calculate(self, Employee):
        return 1.00