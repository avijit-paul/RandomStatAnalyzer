# import libraries
import random
import statistics
import pandas as pd



# define function
def generate_random_variables(num_of_variables, minimum_value, maximum_value, for_integer=False):
    random_variables = []
    if for_integer:  # variables that generate integer
        for _ in range(num_of_variables):
            random_variables.append(random.randint(minimum_value, maximum_value))
    else:
        for _ in range(num_of_variables):  # for float type(short range)
            random_variables.append(round(random.uniform(minimum_value, maximum_value), 2))
    return random_variables


# define number of RVs and set the range
num_of_random_variables = 50
minimum_value = 45
maximum_value = 47

# generate RV's and store in a variable
random_numbers_int = generate_random_variables(num_of_random_variables, minimum_value, maximum_value, for_integer=True)
random_numbers_float = generate_random_variables(num_of_random_variables, minimum_value, maximum_value)

# calculate std deviation, variance and avg from float values
average = statistics.mean(random_numbers_float)
std_deviation = statistics.stdev(random_numbers_float)
variance = statistics.variance(random_numbers_float)

# print values
# print("Random Variables_int type:\n", random_variables_int)
print("Random Variables_float type:\n", random_numbers_float)
print("Average:", average)
print("Standard Deviation:", std_deviation)
print("Variance:", variance)
print('\n')

# create data frame and assign to the column
data_frame = pd.DataFrame(columns=["", "", "", "RVs"])
data_frame["RVs"] = random_numbers_float

# write to Excel sheet
excel_file_name = "Book1.xlsx"
data_frame.to_excel(excel_file_name, index=False)

