from pathlib import Path 
import csv
#create a file to csv file 
fp = Path.cwd()/"csv_reports"/"overheads_day.csv"

#define the overhead function
def overhead_function():
    """
    - Function is to calculate which is the highest overhead category and by how many %
    """
    #read the csv file to append catergory and overheads
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        #skip the header
        next(reader)
        # make output equal to an empty string 
        Output = ""
        # make the highest category an empty string
        highest_category= ""
        #equate the highest overhead to 0
        highest_overhead = 0 
        #looping columns in reader 
        for row in reader:
            #assigning the category to row 0
            category = row[0]
            # assigning overhead to row one in the excel sheet, and turning it into a float 
            overhead = float(row[1])
            #if the overhead is higher than the highest overhead 
            if overhead > highest_overhead:
                # equate the highest overhead to be equal to overhead 
                highest_overhead = overhead
                #equate the highest category to be equal to category
                highest_category = category
            #if the value of the highest overhead is equals to 0
            if highest_overhead != 0:
                #return the highest category and the highest overhead
                return(f"[HIGHEST OVERHEAD] {highest_category}:{highest_overhead}%\n")
            #return the output 
            return(Output)


    
    
     
