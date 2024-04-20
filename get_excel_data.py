import pandas as pd

df = pd.read_excel('Book1.xlsx')
coulumn = 'RVs'

number_of_elements = df[coulumn].count()
print(number_of_elements)