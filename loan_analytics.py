import os
import main
import sys

def choose_options(loan):
    os.system('clear')
    print("Details of the loan are:\n")
    for key in loan:
        print(f"{key}: {loan[key]}")

    options_dict = {
        1:"Calculate the value of the loan after some time.",
        2:"Calculate the value of the loan after some time whilst making regular repayments.",
        3:"Calculate the lifetime of the loan.",
        4:"Calculate the required repayment per year so as to pay off the loan after a given time",
        5:"Investigate another loan",
        6:"Stop doing this. Thinking about loans is boring!"
    }
    print("\nWhat would you like to do? Below are your options.\n")
    for key in options_dict:
        print(f"{key}: {options_dict[key]}")

    ans = int(input().strip())

    if ans == 6:
        print("Yeah, I get it bro.\nSee ya, mate!\n")
        sys.exit(0)

    if ans == 1:
        print("Please enter the elapsed time (in years):")
        elapsed_time = float(input().strip())
        if loan['Type'] == 'Continuously compounded':
            val = main.loan_value_cts(loan['Principal'], loan['Interest rate'], elapsed_time)
        if loan['Type'] == 'Discrete compounding':
            val = main.loan_value(loan['Principal'], loan['Interest rate'], loan['Compounding'], elapsed_time)
        print(f"The value of the loan after {elapsed_time} years is {round(val, 2)}")

        print("\nWould you like to try another option? (Y or N)")
        ans2 = str(input().strip())
        if ans2 == 'Y':
            return choose_options(loan)
        return

    if ans == 2:
        print("Please enter the value of repayments made each year:")
        repayments = float(input().strip())
        print("Please enter the elapsed time (in years):")
        elapsed_time = float(input().strip())

        if loan['Type'] == 'Continuously compounded':
            val = main.loan_value_repayments_cts(loan['Principal'], loan['Interest rate'], elapsed_time, repayments)

        if loan['Type'] == 'Discrete compounding':
            val = main.loan_value_repayments(loan['Principal'], loan['Interest rate'], loan['Compounding'], elapsed_time, repayments)

        print(f"The value of the loan after {elapsed_time} years with {repayments} repaid each year is {round(val, 2)}.")
        
        print("\nWould you like to see a plot of how the loan value changes over the specified elapsed time? (Y or N):")
        ans2 = str(input().strip())
        if ans2 == 'Y':
            main.generate_plot(loan, repayments, elapsed_time)

        print("\nWould you like to try another option? (Y or N)")
        ans2 = str(input().strip())
        if ans2 == 'Y':
            return choose_options(loan)
        return

    if ans == 3:
        print("Please enter the value of repayments made each year:")
        repayments = float(input().strip())

        if loan['Type'] == 'Continuously compounded':
            life_time = main.loan_lifetime_cts(loan['Principal'], loan['Interest rate'], repayments)
        
        if loan['Type'] == 'Discrete compounding':
            life_time = main.loan_lifetime(loan['Principal'], loan['Interest rate'], loan['Compounding'], repayments)

        try:
            print(f"The life time of the loan is around {round(life_time, 2)} years.")
            print("\nWould you like to see a plot of how the loan value changes over its lifetime? (Y or N):")
            ans2 = str(input().strip())
            if ans2 == 'Y':
                main.generate_plot(loan, repayments, life_time)
            print("\nWould you like to try another option? (Y or N)")
            ans2 = str(input().strip())
            if ans2 == 'Y':
                return choose_options(loan)
            return
        except TypeError:
            print("The life time of the loan is infinitely many years.")
            print("\nWould you like to try another option? (Y or N)")
            ans2 = str(input().strip())
            if ans2 == 'Y':
                return choose_options(loan)
            return

    if ans == 4:
        print("Please enter the number of years after which the loan should be paid off:")
        time_total = float(input().strip())

        if loan['Type'] == 'Continuously compounded':
            desired_repayment = main.desired_repayments_cts(loan['Principal'], loan['Interest rate'], time_total)
        
        if loan['Type'] == 'Discrete compounding':
            desired_repayment = main.desired_repayments(loan['Principal'], loan['Interest rate'], loan['Compounding'], time_total)

        print(f"In order to repay the loan after {time_total} year(s), you need to pay {round(desired_repayment, 2)} each year.")

        print("\nWould you like to try another option? (Y or N)")
        ans2 = str(input().strip())
        if ans2 == 'Y':
            return choose_options(loan)
        return

    if ans == 5:
        return

def LoanProgram():
    os.system('clear')
    print("Details of the loan.\nPlease enter the principal value on the loan:")
    principal = float(input().strip())

    print("Please enter the interest rate (percentage per year):")
    interest = float(input().strip())
    interest = interest/100

    print("Is the loan continuously compounded? (Y or N):")
    ans1 = str(input().strip())

    if ans1 == 'Y':
        loan = main.new_loan_cts(principal, interest)
        loan['Type'] = "Continuously compounded"

    if ans1 == 'N':
        print("Enter the number of times the loan is compounded over the year:")
        ans2 = float(input().strip())
        loan = main.new_loan(principal, interest, ans2)
        loan['Type'] = "Discrete compounding"

    elif ans1 != 'Y' and ans1 != 'N':
        print("Key error!")
        sys.exit(0)

    if loan['Type'] == "Continuously compounded":
        loan['Critical repayment level'] = round(main.criticalLevelLoan_cts(loan['Principal'], loan['Interest rate']), 2)
    if loan['Type'] == 'Discrete compounding':
        loan['Critical repayment level'] = round(main.criticalLevelLoan(loan['Principal'], loan['Interest rate'], loan['Compounding']), 2)
    os.system('clear')
    return choose_options(loan)

if __name__ == '__main__':
    os.system('clear')
    LoanProgram()

    print("Would you like to look at a new loan? (Y or N)")
    ans = str(input().strip())
    if ans == 'Y':
        LoanProgram()
    sys.exit(0)