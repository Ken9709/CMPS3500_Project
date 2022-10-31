#*****************************************************************/
# NAME: Hunberto Pascual
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: c_project.py
# DATE:10/29/22
#*****************************************************************/

# import the pandas library
import pandas as pd

# load the csv file into a data frame
airline_data = pd.read_csv('Airline_data.csv')

mode = int(input("Press 1 for data exploration, 2 for Description"))

if mode == 1:
    # removes the index column
    blankIndex = [''] * len(airline_data)
    airline_data.index = blankIndex

    # Lists all columns in the dataset
    print("The columns are: \n")
    print(airline_data.columns.values)

    # Prompt user to drop columns
    column_to_drop = input("\nEnter the name of the Column you'd like to drop: ")
    airline_data.drop(column_to_drop, axis =1,inplace =True)

    # print updated columns
    print("\n Updated Columns :\n")
    print(airline_data.columns.values)

    # prompt user for column to count distint values
    col_to_count= input("\nFor which Column would you like to know the count of Distinct Values: ")
    distinct_val_count = len(pd.unique(airline_data[col_to_count]))
    print("\nNo. of unique values in %s: %d" % (col_to_count,distinct_val_count))

    # prompt user for which column to sort (Ascending or descending)
    col_to_sort = input("\nEnter the column you'd like to be sorted: ")
    sorting_method = int(input("Enter 1 for Ascending or 2 for descending "))
    if sorting_method == 1:
        a_sorted_col = airline_data.sort_values(by = col_to_sort)
        print(a_sorted_col)
    elif sorting_method == 2:
        d_sorted_col = airline_data.sort_values(by = col_to_sort,ascending = False)
        print(d_sorted_col)


if mode == 2:
    col_to_mean = input("\nEnter the column you'd like to be be averaged: ")
    meanSum = 0
    values = airline_data[col_to_mean].tolist()
    for i in values:
        meanSum += i

    print(meanSum/len(airline_data.axes[0]))
     