"""
Comparison of customer churn by tenure
"""

from data.config import data

import matplotlib.pyplot as plt

# Tenure histogram
data.hist('Tenure')
plt.show()

# A stacked bar chart of churn by tenure
data.sort_values(by="Tenure", inplace=True)
churn_by_tenure = data.groupby(["Tenure", "Churn"]).size().unstack()

churn_by_tenure.plot(kind='bar',
                     title="Churn by tenure",
                     xlabel="Tenure",
                     stacked=True,
                     figsize=(12, 7),
                     width=1,
                     fontsize=10)
plt.legend(title="Tenure")
plt.show()



