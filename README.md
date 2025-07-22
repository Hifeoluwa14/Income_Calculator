# Income Calculator
This is a Python-based tool to estimate take-home pay by calculating deductions such as income tax, pension, and national insurance based on earnings and tax code.
## Table of Content
-[Overview](overview)
-[Research Phase](reseacrh-phase)
-[Features](features-of-income-calculator-python-tool)
-[Development Phase](development-phase)
-[Examples](examples)



## Overview
Many individuals struggle with budgeting due to uncertainty about their take-home pay before receiving their payslip. This tool was created to solve that problem by giving users a clear breakdown of their income and deductions for any given period.

## Research Phase

Before diving into the coding, I conducted thorough research into the UK tax system. This included understanding:

- Tax-free personal allowances,

- Various tax codes such as BR, which do not include a personal allowance,

- National Insurance contributions and how they vary based on income levels,

- Pension contributions and their treatment by different employers (e.g., whether they apply to overtime pay).

## Features of Income Calculator Python tool
- Calculates income tax based on personal tax code

- Computes pension contributions (with custom percentage)

- Accounts for optional pension deduction on overtime pay

- Determines national insurance contributions

- Provides a detailed summary of take-home pay per pay cycle

- Supports different pay periods (weekly, monthly, etc.)


## Development Phase

The tool is broken into modular functions that guide the user through the calculation process:

1. **tax_period_function**: Prompts the user to specify the pay period (e.g., weekly, monthly) for which the calculations will apply.

2. **pension_func**: Asks the user what percentage of their income is contributed to a pension. It validates the input to ensure it can be converted to an integer. 

3. **overtime_pension_func**: Determines whether pension deductions also apply to overtime pay. Since not all employers deduct pension from overtime, this function ensures valid input (limited to two options) and loops until an acceptable response is provided.

4. **wage_function**: Requests the user’s basic income before deductions and ensures the input is a valid float to avoid calculation errors.

5. **overtime_amount**: Gathers the expected overtime earnings. This helps in cases where the overtime pay rate differs from the base rate and also supports pension calculations when overtime is exempt.

6. **tax_code_function**: Asks the user if they know their tax code and determines the appropriate personal allowance based on the code to accurately calculate income tax.
  
8. **income_calculator**: This is the core function that pulls data from all the above functions to compute deductions for **pension**, **national insurance**, and **income tax**. It then provides the user with their estimated **take-home pay** for the selected period.


### Examples

- Enter your pay period (weekly/monthly): monthly
- Enter your basic monthly wage: 3000
- Enter pension contribution percentage: 5
- Is pension deducted from overtime? (yes/no): yes
- Enter expected overtime earnings: 500
- Choose your tax code? : 1257L

Gross Income: £3500.00

Pension Contribution: £175.00

Income Tax: £456.00

National Insurance: £182.16

Take-Home Pay: £2687.34

Below is the Picture representaion of code output in Command Prompt as the example above
![Tax Calculator](https://github.com/user-attachments/assets/4273d26d-5043-4ec3-ad40-9752ceadd695)
