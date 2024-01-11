##### Tips Calculator  ######

charge_of_food = float(input("Enter charge for the food: "))

# Tips Constant
TIP_PERCENT =  18
# Sales Tax Constant
SALES_TAX = 7

tip = (TIP_PERCENT / 100) * charge_of_food      # Tip Calculation
salestax = (SALES_TAX / 100) * charge_of_food   # Sales Tax Calculation
grandtotal = charge_of_food + salestax + tip    # Grand Total Calculation

# Output
print(f"Tip ({TIP_PERCENT}%): ${tip:.2f}")
print(f"Sales Tax ({SALES_TAX}%): ${salestax:,.2f}")
print(f"Grand Total: ${grandtotal:.2f}")
