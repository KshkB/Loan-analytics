# Loan analytics

This repository contains a simple program for calculating the value of a loan. On running `loan_analytics` the user is prompted to specify initial parameters defining a loan. These include:

- the principal value;
- the interest rate (per annum);
- whether the loan is continuously compounded or not.

Is the loan is not continuously compounded, it is *discretely compounded*. Accordingly, the user will be prompted to specify the number of compounding periods. Note, all time units are expressed in terms of *years*.

With these inputs established, the user can then choose among the following options:

- calculate the value of the loan after some elapsed time;
- calculate the value of the loan after some elapsed time, taking into account a yearly repayment amount;
- calculate the lifetime of the loan with a specified, yearly repayment amount;
- calculate the desired yearly repayment amount in order to pay off the loan after a specified time.

For derivations of formulae used in the implementation of this program, see the online article hosted at the link below:
