from SubPackage import MySubscript
from SubPackage import income_func



tax_period = MySubscript.tax_period_func()

pension_percentage = MySubscript.pension_func()

personal_allowance = MySubscript.tax_code_function()

overtime_pension = MySubscript.overtime_pension_func()

basic_income = MySubscript.wages_function()

overtime_income = MySubscript.overtime_amount()
 
income_func.income_calculator(tax_period, personal_allowance,pension_percentage,basic_income,overtime_income, overtime_pension)