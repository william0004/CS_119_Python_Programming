# ============================================================
# Author: Yaowei Lei
# Date:    10/18/2021
# Purpose: CS119-PJ2: Compute and print a professional investment report.


# MAIN PROGRAM :
n = 1  # line number for each separator line for readability of the output
print ("Welcome to the Investment Report Tool of Yaowei Lei!")   # must use your name!
print(n,"======================================================."); n+=1;

# Accept the inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the rate as a %: "))
print(n,"======================================================."); n+=1;

# Convert the rate to a decimal number
rate = rate / 100
# Initialize the accumulator for the interest
totalInterest = 0.0
# Display the header for the table
print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending balance"))
# Compute and display the results for each year
for year in range(1, years + 1):
	interest = startBalance * rate
	endBalance = startBalance + interest
	print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
	startBalance = endBalance
	totalInterest += interest
print(n,"======================================================."); n+=1;

# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)


print(n,"======================================================."); n+=1;
print("Thank you for using the Investment Report Tool of Yaowei Lei! ")  # must use your name!
print(n,"======================================================."); n+=1;
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then Enter to exit: ")
# End of MAIN PROGRAM


