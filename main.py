# collect necessary inputs: loan amount, APR, years
# calculate monthly payment
# show the user

def main():
    print("Monthly payment loan calculator")
    print("")

    principal = float(input("Input the loam amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interst_rate = apr / 1200
    months = years * 12
    monthly_payment = principal * monthly_interst_rate / (1 - (1 + monthly_interst_rate) ** (- months))

    print("The monthly payment for this loan is: £%.2f " % monthly_payment)


main()
