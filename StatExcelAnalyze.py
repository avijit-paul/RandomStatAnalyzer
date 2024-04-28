# define function
import pandas as pd


def calculate_stat(excel_file, sheet_number, column_name):
    df = pd.read_excel(excel_file, sheet_name=sheet_number)

    column_data = df[column_name]

    average = column_data.mean()
    print("Average is :", average)
    standard_deviation = column_data.std()
    print("Standard deviation is :", standard_deviation)
    variance = column_data.var()
    print("Variance is :", variance)

    return average, standard_deviation, variance

# enter data

excel_file = "excel2.xlsx"
sheet_number = "Sheet1"
column_name = "RVs"

# call the function
calculate_stat(excel_file, sheet_number, column_name)