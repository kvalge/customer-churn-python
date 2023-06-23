import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('customer_churn.xlsx')

print(data.shape)
print(data.columns)
print(data.head())

# creating a basic histogram
data.hist('Monthly_Charges')
plt.show()
