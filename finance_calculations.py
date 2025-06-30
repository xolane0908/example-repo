import math

# The choice of calculation the user can choose 
print("Investment - the amount of interest you'll gain from an investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# Ask the user which calculatio they will pick 
decision_time = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

# To display the words in uppercase 
decision_time = decision_time.lower()

# The users inputs for investments
if decision_time == "investment":  
    
 deposit = float(input("Enter the amount you are going deposit :"))
 
 interest_rate = float(input("Enter the interest rate as a percentage : "))

 num_of_years = int(input("Enter the number of years you want to invest : "))
 
 interest_type = input("Choose 'simple' or 'compound, interest:").lower()
 
 interest = interest_rate / 100
 
 
 if interest_type == "simple":
     total = deposit * (1 + interest * num_of_years)
     
 elif interest_type == "compound":
     total = deposit * math.pow((1 + interest), num_of_years)
     
 else:
     print("Error: Please enter 'simple' or 'compound'")
     
     exit()
     
 print(f"\nAfter {num_of_years} years, your investment will be worth: R{total:.2f}")
 
 
# The user inputs for bond
elif decision_time == "bond":
    
     value_of_the_house = float(input("Enter the current value of the house."))
    
     interest_rate = float(input("Enter the interest rate as a percentage"))
    
     num_of_months = int(input("Enter the number of months you plan to repay the bond"))
    
     rate = (interest_rate / 100) / 12
    
     bond_repayment = (rate * value_of_the_house)/(1 - (1 + rate)**(-num_of_months))
    
     print(bond_repayment)
     
else:
    print("Error: Please enter 'investment' or 'bond'")
    
    
    
    
    






