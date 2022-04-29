from math import exp
from math import log
import matplotlib.pyplot as plt

def new_loan(principal, interest, compounding):
    loan_card = {}
    
    loan_card["Principal"] = principal
    loan_card["Interest rate"] = interest
    loan_card["Compounding"] = compounding
    
    return loan_card

def new_loan_cts(principal, interest):
    loan_card = {}
    interest = interest
    
    loan_card["Principal"] = principal
    loan_card["Interest rate"] = interest
    
    return loan_card

def loan_value(principal, interest_rate, compounding, time):
    z_var = (1 + interest_rate/compounding)**compounding
    exponent = time
    return principal*(z_var**exponent)
    
def loan_value_cts(principal, interest_rate, time):
    return principal*exp(interest_rate*time)
    
def loan_value_repayments(principal, interest_rate, compounding, time, repayments):
    z_var = (1 + interest_rate/compounding)**compounding

    loan_val = loan_value(principal, interest_rate, compounding, time)
    repay_val = repayments*(1 - z_var**time)/(1-z_var)

    val = loan_val - repay_val

    if val > 0:
        return val
    return 0

def loan_value_repayments_cts(principal, interest_rate, time, repayments):
    loan_val = loan_value_cts(principal, interest_rate, time)
    repay_val = repayments*(1 - exp(interest_rate*time))/(1 - exp(interest_rate))
    val = loan_val - repay_val
    if val > 0:
        return val
    return 0

def criticalLevelLoan(principal, interest_rate, compounding):
    z_factor = (1 + interest_rate/compounding)**compounding
    return (z_factor-1)*principal

def loan_lifetime(principal, interest_rate, compounding, repayment):
    critical = criticalLevelLoan(principal, interest_rate, compounding)
    z_factor = (1 + interest_rate/compounding)**compounding

    if repayment <= critical:
        return "infinitely many"
    return (1/log(z_factor))*(log(repayment) - log((1-z_factor)*principal + repayment))

def criticalLevelLoan_cts(principal, interest_rate):
    return (exp(interest_rate) - 1)*principal

def loan_lifetime_cts(principal, interest_rate, repayment):
    critical = criticalLevelLoan_cts(principal, interest_rate)

    if repayment <= critical:
        return "infinitely many"
    return (1/interest_rate)*(log(repayment) - log((1-exp(interest_rate))*principal + repayment))

def desired_repayments(principal, interest_rate, compounding, time):
    z_factor = (1 + interest_rate/compounding)**compounding
    return principal*(z_factor**time)*(1-z_factor)/(1 - z_factor**time)

def desired_repayments_cts(principal, interest_rate, time):
    return principal*exp(interest_rate*time)*(1 - exp(interest_rate))/(1 - exp(interest_rate*time))

# VISUALIZATION
def generate_plot(loan, repayment, time):
    time_in_months = time*12
    time_in_months = int(time_in_months)
    x_data = [t for t in range(time_in_months + 1)]
    y_data = []
    for t in range(time_in_months+1): 
        if loan['Type'] == 'Continuously compounded':
            loan_val = loan_value_repayments_cts(loan['Principal'], loan['Interest rate'], t/12, repayment)
            y_data.append(loan_val)
        if loan['Type'] == 'Discrete compounding':
            loan_val = loan_value_repayments(loan['Principal'], loan['Interest rate'], loan['Compounding'], t/12, repayment)
            y_data.append(loan_val)

    plt.plot(x_data, y_data, color='blue', linewidth=1, linestyle='dotted') 

    plt.title("Loan value over time")
    plt.xlabel("Time elapsed (in months)")
    plt.ylabel("Loan value")

    plt.show()
    return 






