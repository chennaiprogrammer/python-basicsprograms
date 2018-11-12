"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""
#tax = 5%
#tip= 18%
Tax_rate = 0.05
Tip_rate = 0.018

cost = int(input("enter the cost of meal:"))

tax = cost*Tax_rate
tip = cost*Tip_rate
Total_cost = tip + tax + cost

print("tax is %.2f and tip is %.2f and total cost of meal is %.2f "%(tax,tip,Total_cost))