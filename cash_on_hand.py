from pathlib import Path 
import csv


def cash_on_hand_function():
    """
    - This function will compute the difference in Cash-on-Hand if the current day is lower than the previous day.
    """
    # create file path to COH csv file in current working folder
    fp = Path.cwd()/"csv_reports"/"cash_on_hand.csv"
    # read csv file to append day and net profit
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        # create reader variable to read file
        reader = csv.reader(file)
        # skip past header
        next(reader)
        # set prev COH value to 0
        previous_cash_on_hand = 0
        # set output variable equal to empty string
        Output = ""
        # set check value to 0
        check = 0
        # assign true value to true_false variable
        true_false = True
        # create for loop to loop through columns in reader
        for column in reader:
            # assign float to current COH which is column 2 on csv file
            current_cash_on_hand = float(column[1])
            # create if conditional for when prev COH is more than current COH
            if previous_cash_on_hand > current_cash_on_hand:
                # assign difference variable to value of current COH subtracted from prev COH
                difference = previous_cash_on_hand - current_cash_on_hand 
                # increase check value by 1 through the loop
                check += 1
                # reassign current COH variable to prev COH to return value
                previous_cash_on_hand = current_cash_on_hand
                # assign false value to true_false variable
                true_false = False
                # print output by showing day and difference of COH
                Output += (f"[CASH DEFICIT] DAY:{column[0]}, AMOUNT: USD{difference}\n")
            # create else if variable for when prev COH is less than current COH
            elif previous_cash_on_hand < current_cash_on_hand:
                # set check value to 0
                check = 0
                # reassign current COH variable to prev COH to return variable
                previous_cash_on_hand = current_cash_on_hand
        # create if loop for when true_false variable is true
        if true_false == True: 
            # print output for cash surplus
            Output += ('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.')
        # return output generated
        return(Output)




