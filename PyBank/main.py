#Import Dependencies

import os
import csv 

#Read CSV File/Provide Path

csvpath =  os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as data_file:
    data_reader = csv.reader(data_file, delimiter=',')
    print(data_reader)
    data_header = next(data_reader)
    
#Declare Variables Needed For Assignment
    months = []
    profit = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {data_header}")               

#Loop Through Data to Get Totals
    
    for row in data_reader:

#Append totals to list by index

        months.append(row[0])
        profit.append(row[1])
    
    print(len(months))
 
 #Calculate actual revenue of all rows by  summing all profits

    profit_as_integer = map(int, profit)
    
    total_profit = (sum(profit_as_integer))
    
    print(total_profit)


 #Find Monthly Change and from there get average change

    i = 0
    for i in range(len(profit) - 1):
        difference_in_month = int(profit[i+1]) - int(profit[i])
 
 # Append each month difference to monthly_change list

        monthly_change.append(difference_in_month)
   
    Total = sum(monthly_change)
    
    
# Find average  of monthly_changes and print
    
    average_monthly_change = Total / len(monthly_change)
    print(average_monthly_change)
    
    
#Greatest Increase and Greatest Decrease Amount 
    
    max_profit_increase = max(monthly_change)
    print(max_profit_increase)

    min_profit_increase = min(monthly_change)
    print(min_profit_increase)

#Corresponding months for those values (need to find indexes first, then call that month)

    max_profit_month_index = monthly_change.index(max_profit_increase) + 1
    min_profit_month_index = monthly_change.index(min_profit_increase) + 1

    
    print(max_profit_month_index)
    print(min_profit_month_index)

    max_profit_month = {months[max_profit_month_index]}
    min_profit_month = {months[min_profit_month_index]}

    print(max_profit_month)
    print(min_profit_month)




#Print Statements

print("----------------")

print("Financial Analysis")

print("Total Months: " + str(len(months)))

print("Total Profit: $ " + str(total_profit))
      
print("Average Monthly Change : $" + str(average_monthly_change))

print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit_increase})")

print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit_increase})")


#Output Analysis to text file

output_file = "financial_summary.txt"

with open(output_file, 'w', newline="") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("Total Months: " + str(len(months)))
    file.write("\n")
    file.write(("Total Profit: $ " + str(total_profit)))
    file.write("\n")
    file.write("Average Monthly Change : $" + str(average_monthly_change))
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit_increase})")
