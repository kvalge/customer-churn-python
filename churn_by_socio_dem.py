"""
Comparison of customer churn by socio-demographic characteristics
"""

import pandas as pd
import matplotlib.pyplot as plt

file = open("text_output/churn_by_socio_dem.txt", "w")

data = pd.read_excel("data/customer_churn.xlsx")

# A stacked bar chart of churn by age group
churn_by_age_group = data.groupby(["Churn", "Senior_Citizen"]).size().unstack()
churn_by_age_group.plot(kind='bar',
                        stacked=True,
                        title="Count of churn by age group",
                        xlabel="Opted out",
                        fontsize=13)
plt.legend(title="Age of over 65")
plt.show()

file.write("A churn by age group: \n{}\n".format(churn_by_age_group) + "\n")


# A stacked bar chart of churn by having partner
churn_by_partner = data.groupby(["Churn", "Partner"]).size().unstack()
churn_by_partner.plot(kind='bar',
                      stacked=True,
                      title="Count of churn by having partner",
                      xlabel="Opted out",
                      fontsize=13)
plt.show()

file.write("A churn by having partner: \n{}\n".format(churn_by_partner) + "\n")


# A stacked bar chart of churn by having partner
churn_by_dependents = data.groupby(["Churn", "Dependents"]).size().unstack()
churn_by_dependents.plot(kind='bar',
                         stacked=True,
                         title="Count of churn by having dependents",
                         xlabel="Opted out",
                         fontsize=13)
plt.show()

file.write("A churn by having dependents: \n{}\n".format(churn_by_dependents) + "\n")


