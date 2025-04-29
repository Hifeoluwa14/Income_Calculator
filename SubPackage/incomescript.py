
# Calculated how much is paid to pension, tax, national insurance and take home for specific period.
def income_calculator(tax_period, personal_allowance, pension_percentage, basic_income, overtime_income, overtime_pension):
    
    pension = 0
    income = 0
    national_insurance = 0
    income_tax = 0

    # Calculate for weekly
    if tax_period == '1':
        
         # Calculate how much is paid to pension
        if overtime_pension == '1': 
            income = basic_income + overtime_income
            pension = income * pension_percentage / 100
            
        else:
            pension = basic_income * pension_percentage / 100
            income = basic_income + overtime_income
        
        # Calculate how much National Insurance is paid
        total_income = income - pension
        if 242 < total_income <= 967:
            national_insurance = 0.08 * (total_income - 242)
         
        elif total_income > 967:
            national_insurance = (0.08 * (967 - 242)) + (0.02 * (total_income - 967))
        
            
        # Calculate how much is paid to income tax based on tax-coode
        if personal_allowance == 'BR':
            income_tax = total_income * 0.2 
            
        elif personal_allowance == 'D0':
                income_tax = total_income * 0.4
            
        elif personal_allowance == 'D1':
            income_tax = total_income * 0.45
            
        else:
            
            #Personal allowance is divided by 52 because it is a weekly calculation
            personal_allowance = personal_allowance / 52 
            
            if total_income > personal_allowance:
                if total_income <= 967 :
                    income_tax = (total_income - personal_allowance) * 0.2
                    
                elif total_income <= 1923:
                    income_tax = ((967 - personal_allowance) * 0.2 + (total_income - 967) * 0.4)
                    
                elif total_income <= 2406:
                    excess = total_income - 1923
                    new_allowance = max(0, personal_allowance - (excess * 0.5))
                    income_tax = ((967 - new_allowance) * 0.2 + (total_income - 967) * 0.4)
                    
                else:
                    income_tax =(967 * 0.2 +(2406 - 967) * 0.4 + (total_income - 2406) * 0.45)
                    
    # Calcultate for Monthly
    elif tax_period == '2':
        
        # Calculate how much is paid to pension
        if overtime_pension == '1': 
            income = basic_income + overtime_income
            pension = income * pension_percentage / 100
            
        else:
            pension = basic_income * pension_percentage / 100
            income = basic_income + overtime_income
            
        # Calculate how much National Insurance is paid
        total_income = income - pension
        if total_income > 1048 and total_income <= 4189:
            national_insurance = 0.08 * (total_income - 1048)
         
        elif total_income > 4189:
            national_insurance = (0.08 * (4189 - 1048)) + (0.02 * (total_income - 4189))
            
        # Calculate how much is paid to income tax based on tax-coode
        if personal_allowance == 'BR':
            income_tax = total_income * 0.2 
                
        elif personal_allowance == 'D0':
            income_tax = total_income * 0.4
            
        elif personal_allowance == 'D1':
            income_tax = total_income * 0.45
            
        else:
            
            # Personal allowance is divided by 12 because it is a monthly calculation
            personal_allowance = personal_allowance / 12 
            if total_income > personal_allowance:
                if total_income <= 4189 :
                    income_tax = (total_income - personal_allowance) * 0.2
                    
                elif total_income <= 8333.33:
                    income_tax = ((4189 - personal_allowance) * 0.2 + (total_income - 4189) * 0.4)
                    
                elif total_income <= 10428.33:
                    excess = total_income - 8333.33
                    new_allowance = max(0, personal_allowance - (excess * 0.5))
                    income_tax = ((4189 - new_allowance) * 0.2 + (total_income - 4189) * 0.4)
                    
                else:
                    income_tax =(4189 * 0.2 +(10428.33 - 4189) * 0.4 + (total_income - 10428.33) * 0.45)
                    
    # Calculate for yearly    
    elif tax_period == '3':
        
        # Calculate how much is paid to pension
        if overtime_pension == '1': 
            income = basic_income + overtime_income
            pension = income * pension_percentage / 100
            
        else:
            pension = basic_income * pension_percentage / 100
            income = basic_income + overtime_income
            
        # Calculate how much National Insurance is paid
        total_income = income - pension
        if total_income > 12570 and total_income <= 50270:
            national_insurance = 0.08 * (total_income - 12570)
         
        elif total_income > 50270:
            national_insurance = (0.08 * (50270 - 12570)) + (0.02 * (total_income - 50270))
            
        # Calculate how much is paid to income tax based on tax-coode
        if personal_allowance == 'BR':
            income_tax = total_income * 0.2 
            
            
        elif personal_allowance == 'D0':
            
            income_tax = total_income * 0.4
        elif personal_allowance == 'D1':
            income_tax = total_income * 0.45
            
        else:
            
            #Personal allowance remains the same because it is based on yearly calculation
            if total_income > personal_allowance:
                if total_income <= 50270:
                    income_tax = (total_income - personal_allowance) * 0.2
                    
                elif total_income <= 100000:
                    income_tax = ((50270 - personal_allowance) * 0.2 + (total_income - 50270) * 0.4)
                    
                elif total_income <= 125140:
                    excess = total_income - 100000
                    new_allowance = max(0, personal_allowance - (excess * 0.5))
                    income_tax = ((50270 - new_allowance) * 0.2 + (total_income - 50270) * 0.4)
                    
                else:
                    income_tax =(50270 * 0.2 +(125140 - 50270) * 0.4 + (total_income - 125140) * 0.45)
                    
    print(f'Pension for this period is - {round(pension,2)}') 
    print(f'National Insurance paid for this period is - {round(national_insurance,2)}')
    take_home = round(income - pension - income_tax - national_insurance,2)
    print(f'Your Take Home Income is {take_home}')   