def calculate_finances(monthly_income: float, tax_rate: float, currency: str, monthly_expenses: float) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_expenses: float = monthly_expenses * 12
    year_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = year_salary - yearly_tax - yearly_expenses

    print('--------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly Expenses: {currency}{monthly_expenses:,.2f}')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{year_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly expenses: {currency}{yearly_expenses:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('--------------------------')

def main() -> None:
    monthly_income: float = float(input('Enter Your Monthly Salary: '))
    currency: str = input('Enter Your Currency e.g NGN, USD: ')
    tax_rate: float = float(input('Enter Your Tax Rate(%): '))

    total_expenses: float = 0.0

    while True:
        expense: str = input('Do You Have Expenses for the Month (y/n): ').lower()
        if expense == 'y':
            expenses_name: str = input('Input the name of the Expense: ')
            expenses_price: float = float(input(f'Input {expenses_name} price: '))
            total_expenses += expenses_price
        elif expense == 'n':
            break
        else:
            print('Invalid input. Please enter "y" or "n".')

    calculate_finances(monthly_income, tax_rate, currency, total_expenses)

if __name__ == '__main__':
    main()
