"""
Comparison of customer churn by contract, invoicing and payment type.
"""

from data.config import data

import matplotlib.pyplot as plt
import numpy as np

file = open("../text_output/churn_by_invoicing.txt", "w")

# A pie chart and data written to the file of contract types count
contract = data.groupby(["Contract"]).size()

colors = ["steelblue", "orange", "silver"]
labels = ["Month to month", "One year", "Two years"]
contract.plot(kind="pie",
              autopct="%1.0f%%",
              colors=colors,
              labels=labels,
              title="Contract",
              fontsize=13)
plt.show()

file.write("{}\n".format(contract) + "\n")

# Writes to the file a share of contract types
month_to_month_contract = np.array(contract)[0]
one_year_contract = np.array(contract)[1]
two_years_contract = np.array(contract)[2]
sum_contract = np.sum(np.array(contract))
share_of_month_to_month = round((month_to_month_contract / sum_contract) * 100)
share_of_one_year = round((one_year_contract / sum_contract) * 100)
share_of_two_years = round((two_years_contract / sum_contract) * 100)
file.write("A share of customers with the month to month contract: {}%\n".format(share_of_month_to_month))
file.write("A share of customers with the one year contract: {}%\n".format(share_of_one_year))
file.write("A share of customers with the two years contract: {}%\n".format(share_of_two_years) + "\n")

# A stacked bar chart and data written to the file of churn by contract type
churn_by_contract = data.groupby(["Churn", "Contract"]).size().unstack()

colors = ["steelblue", "orange", "silver"]
ax = churn_by_contract.plot(kind='bar',
                            title="Count of churn by contract",
                            xlabel="Opted out",
                            color=colors,
                            stacked=True,
                            fontsize=13)
ax.bar_label(ax.containers[0], size=10)
ax.bar_label(ax.containers[1], size=10)
ax.bar_label(ax.containers[2], size=10)
ax.legend(["Month to month", "One year", "Two years"])
plt.show()

file.write("A churn by contract: \n{}\n".format(churn_by_contract) + "\n")

# Writes to the file a share of opted out customers by multiple lines
contract_array = np.array(churn_by_contract)
share_of_churn_month_to_month = round((np.array(churn_by_contract)[1][0] / month_to_month_contract) * 100)
share_of_churn_one_year = round((np.array(churn_by_contract)[1][1] / one_year_contract) * 100)
share_of_churn_two_years = round((np.array(churn_by_contract)[1][2] / two_years_contract) * 100)

file.write("A share of opted out customers having a month to month contract: {}%\n"
           .format(share_of_churn_month_to_month))
file.write("A share of opted out customers having a one year contract: {}%\n"
           .format(share_of_churn_one_year))
file.write("A share of opted out customers having a two years contract: {}%\n"
           .format(share_of_churn_two_years) + "\n")