class EmployeePayCalc(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def Employee_Calc(self, Employee):
        return self._strategy.calculate(Employee)