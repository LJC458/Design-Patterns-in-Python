import Manager_Paystrat,Standard_Paystrat,CEO_PayStrat,Employeeclass,EmployeePayCalcStrat


# Test CEO_Pay

Employee = Employeeclass.Employee()
strategy = CEO_PayStrat.CEO_Pay()
Pay_calulator = EmployeePayCalcStrat.EmployeePayCalc(strategy)
Pay = Pay_calulator.Employee_Calc(Employee)
print( Pay == 3.0 )

# Test Manager_Pay

Employee = Employeeclass.Employee()
strategy = Manager_Paystrat.Manager_Pay()
Pay_calulator = EmployeePayCalcStrat.EmployeePayCalc(strategy)
Pay = Pay_calulator.Employee_Calc(Employee)
print( Pay == 2.0 )

Employee = Employeeclass.Employee()
strategy = Standard_Paystrat.standard_Pay()
Pay_calulator = EmployeePayCalcStrat.EmployeePayCalc(strategy)
Pay = Pay_calulator.Employee_Calc(Employee)
print( Pay == 1.0 )