# Determine which tax period to be calculated
def tax_period_func() :
    a = 'k' 
    while a not in ['1','2','3']:
        print('Enter 1 for weekly tax_period')
        print('Enter 2 for monthly tax_period')
        print('Enter 3 for yearly tax_period')
        a= input('Choose a tax period: ')
        if a == '1':
            return a
        if a == '2':
            return a
        if a == '3':
            return a
    

# Accept input to determine how much is paid towards pension 
def pension_func():
    value = 'a'
    while True :
        print('How many percent of your salary is paid to pension?')
        
        try:
            value= int(input('Enter pension percentage or 0 if you optioned out of pension'))
            if int(value) >= 0 <= 100:
                break
            else:
                print('\n Enter a Valid Number between 0-100')
                value=  'a'
        except:
            print('\n Enter numeric value')
            pass
    return int(value)




# Determine if pension is deducted from overtime
def overtime_pension_func() :
    a = 0
    while a not in ['1','2']:
        print('Does your company Deduct pension from Overtime')
        a = input('Enter "1" for Yes or Not Sure, "2" for No.')
        if a == '1':
            return a
        if a == '2':
            return a


# Accept input for basic salary earning for the specific period
def wages_function():
    while True:
        value = input('Enter basic income excluding overtime for the specific period: ')
        try:
            value = float(value)
            if value >= 0:
                return value
            else:
                print('Please enter a non-negative number.')
        except ValueError:
            print('Enter a valid amount (e.g., 1500.00).')



# Accept input for how much is paid as overtime for the specific period
def overtime_amount():
    while True:
        value = input('Enter overtime income for the specific period- ')
        try:
            value = float(value)
            if value >= 0:
                return value
            else:
                print('Please enter a non-negative number.')
        except ValueError:
            print('Enter a valid amount (e.g., 1500.00).')


# Helps determine tax code to assign tax-free allowance
def tax_code_function():
    v = '0'
    while v not in ['1','2','3','4','5','6','7','8']:
        print('For tax_code 1257L, Enter 1')
        print('For tax_code 1257M, Enter 2')
        print('For tax_code 1257N, Enter 3')
        print('For tax_code BR, Enter 4')
        print('For tax_code DO, Enter 5')
        print('For tax_code D1, Enter 6 ')
        print('For tax_code X, Enter 7')
        print('If you do not know your tax_code, Enter  8')
        
        v = input('Choose a tax code')
        if v == '1' or v == '8':
            return 12570
        elif v == '2':
            return 13830
        elif v =='3':
            return 11310
        elif v == '4' or v == '7':
            print('Taxed at 20%')
            return 'BR'
        elif v == '5':
            print('Taxed at 40% with no Personal Allowance')
            return 'D0'
        elif v == '6':
            print('Taxed at 45% with no Personal Allowance ')
            return 'D1'             
    return v


