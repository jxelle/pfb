from pathlib import Path 
import csv

# define the profit loss function
def profit_loss_function():
    """
    - This function compute the difference in the net profit coloumn if the net profit on the current day is lower than the previous day.
    """
    
    # creating a file path to the csv file
    fp = Path.cwd()/"csv_reports"/"profit_and_loss.csv"
   
    # read the csv file to append day and net profit
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
     
        # create a reader to read the csv
        reader = csv.reader(file)
       
        # skipping the header
        next(reader)

        # equate the previous net profit to 0
        previous_net_profit = 0

        # make the output equals to an empty string 
        Output = ""

        # set the check value to 0
        check = 0
       
        # assign true to the variable called true_false_check
        true_false_check = True  
       
        # creating a for loop for column in reader
        for column in reader:
        
            # equating current net profit to column 4 in the excel sheet and changing it to a float 
            current_net_profit = float(column[4])
            
            # setting the condition if previous_net_profit is less than previous net profit
            if previous_net_profit > current_net_profit :
                
                # difference equals to previous net profit minus current net profit 
                difference = previous_net_profit - current_net_profit

                # increasing the check value by 1
                check += 1

                # assigning the previous_net_profit to the current_net_profit variable
                previous_net_profit = current_net_profit

                # seting the true_false_check to false
                true_false_check = False

                # making the output show the day and difference for net profit 
                Output += (f"[PROFIT DEFICIT] DAY:{column[0]}, AMOUNT: USD{difference}\n")
            
            # setting the next condition if the previous_net_profit is less than current_net_profit
            elif previous_net_profit < current_net_profit:
           
                # setting the check value to 0
                check = 0

                # setting the previous_net_profit to the current_net_profit
                previous_net_profit = current_net_profit
     
        # setting the last condition if true_false_check is true
        if true_false_check == True:
          
            # this statement will be printed if the condition is met 
            Output += ("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
     
        # return the output generated 
        return(Output)
