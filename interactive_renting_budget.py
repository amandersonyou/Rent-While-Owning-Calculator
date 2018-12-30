# Amanda Anderson-You
# Budget calculator for homeowners considering renting out their houses and
# renting a place to live themselves.
# December 2018

print("""Welcome! Please begin by entering your MONTHLY owner payments.
For all entries, enter an integer amount, no $ signs or letters.
if N/A just enter 0. \n""")

# Input user information for current MONTHLY estimated expenditure for property owned.
while True:
    try:
        mortgage = int((input("Enter monthly mortgage amount: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        hoa = int((input('Enter monthly HOA amount. Note, if parking is additional, \
please include in combination with HOA here: ')))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        utilities = int((input("""Enter estimated monthly total utilities amount.
Includes gas, electric, internet, cable, water, sewage, etc.
If you plan to pass some of these payments onto the renter only include
what you'll continue paying as a landlord: """)))
        break
    except:
        print("Please enter a total estimated numerical amount.")
        continue

total_monthly_owners_payments = mortgage + hoa + utilities
print('Total monthly-type homeowners expenditure is: ' + str(total_monthly_owners_payments))
print('\n')

# Input user information for current ANNUAL estimated expenditure for property owned.


print('Now we will input ANNUAL homeowner costs.')

while True:
    try:
        property_tax = int((input("Enter annual property tax amount: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        hsa = int((input("Enter HSA insurance amount. If N/A enter 0: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        property_insurance = int((input("Enter annual property insurance amount: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue


total_annual_owners_payments = property_tax + hsa + property_insurance
print('Total annual-type homeowners expenditure is: ' + str(total_annual_owners_payments))
print('\n')
homeowner_monthly_annual_total = (total_monthly_owners_payments * 12) + total_annual_owners_payments
print('Total all encompassing homeowners expenditure over the course of a year \
amounts to: ' + str(homeowner_monthly_annual_total))
print('\n')


# Input user information for estimated monthly rental expenditures for renting their own place to live.
print('------------------------------')
print('''Now let's find out how much you'll spend renting a place to live yourself.''' + '\n')

while True:
    try:
        rent = int((input("Enter monthly rent amount: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        rental_utilities = int((input('''Enter estimated monthly rental utilities amount
NOT paid for by the homeowner: ''')))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        rental_parking = int((input("Enter monthly parking amount: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        rental_insurance = int((input("Enter annual rental insurance amount: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

while True:
    try:
        gym_membership = int((input("Enter monthly gym membership amount: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

total_monthly_rental_cost = rent + rental_utilities + rental_parking + gym_membership
print('Total monthly rental expenditure, not including insurance, is: ' + str(total_monthly_rental_cost))

total_annual_rental_cost = (total_monthly_rental_cost * 12) + rental_insurance
print('\n')
print('Total annual rental expenditure is: ' + str(total_annual_rental_cost))


# Input user information for estimated monthly rental income for renting their place out.
print('\n')
print('------------------------------')
print('''Let's now look at how much additional income renting your property can bring in
then compare this amount to the money spent renting elsewhere.''')
print('\n')

# Determine how much income the homeowner anticipates taking in from renting their property.

while True:
    try:
        rental_income = int((input("Enter monthly amount you plan to rent your place \
for, include parking: ")))
        break
    except:
        print("Please enter a numerical amount.")
        continue

annual_rental_income = rental_income * 12
print('Annually, you will bring in a rental income of: ' + str(annual_rental_income))
print('\n')


# Summary: Compare amount of money spent renting with amount earned being a landlord.

print('''To summarize, you will always need to pay the costs of home ownership, taking that amount
into consideration, can you afford the additional cost monthly and annually of renting?
Or will you end up making more money renting out the place you own than you are spending?''')
print('\n')

print('Total homeowners expenditure over the course of a year amounts \
to: ' + str(homeowner_monthly_annual_total))
print('Total annual rental expenditure is: ' + str(total_annual_rental_cost))
print('Annually, you will bring in a rental income of: ' + str(annual_rental_income))
print('\n')

rental_difference = annual_rental_income - total_annual_rental_cost
print('''Amount remaining after subtracting annual rental expenditure
from annual rental income: ''' + str(rental_difference))
print('Monthly, that is ' + str(rental_difference / 12) + ' dollars a month.')

print('\n')
print('End!')





