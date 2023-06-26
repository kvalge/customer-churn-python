"""
Comparison of customer churn by socio-demographic characteristics
"""

from data.config import data

import matplotlib.pyplot as plt
import numpy as np

file = open("../text_output/churn_by_socio_dem.txt", "w")

# A bar chart and data written to the file of churn count
churn = data.groupby(["Churn"]).size()
churn.plot(kind='bar',
           stacked=True,
           title="Churn",
           xlabel="Opted out",
           fontsize=13)
plt.show()

file.write("{}\n".format(churn) + "\n")

# Writes to the file a share of opted out customers
churn_yes = np.array(churn)[1]
sum_churn = np.sum(np.array(churn))
share_of_churn_yes = round((churn_yes / sum_churn) * 100)
file.write("A share of opted out customers: {}%\n".format(share_of_churn_yes) + "\n")

# A stacked bar chart and data written to the file of churn by age group
churn_by_age_group = data.groupby(["Churn", "Senior_Citizen"]).size().unstack()
churn_by_age_group.plot(kind='bar',
                        stacked=True,
                        title="Count of churn by age group",
                        xlabel="Opted out",
                        fontsize=13)
plt.legend(title="Age of over 65")
plt.show()

file.write("A churn by age group: \n{}\n".format(churn_by_age_group) + "\n")

# Writes to the file a share of opted out customers of age of over 65
age_array = np.array(churn_by_age_group)
sum_age_array = np.sum(age_array)
share_of_churn_senior_no = round((np.array(churn_by_age_group)[1][0] / sum_age_array) * 100)
share_of_churn_senior = round((np.array(churn_by_age_group)[1][1] / sum_age_array) * 100)
file.write("A share of opted out customers of age of under 65: {}%\n".format(share_of_churn_senior_no))
file.write("A share of opted out customers of age of over 65: {}%\n".format(share_of_churn_senior) + "\n")

# A stacked bar chart and data written to the file of churn by having partner
churn_by_partner = data.groupby(["Churn", "Partner"]).size().unstack()
churn_by_partner.plot(kind='bar',
                      stacked=True,
                      title="Count of churn by having partner",
                      xlabel="Opted out",
                      fontsize=13)
plt.show()

file.write("A churn by having partner: \n{}\n".format(churn_by_partner) + "\n")

# Writes to the file a share of opted out customers having partner
partner_array = np.array(churn_by_partner)
sum_partner_array = np.sum(partner_array)
share_of_churn_partner_no = round((np.array(churn_by_partner)[1][0] / sum_partner_array) * 100)
share_of_churn_partner = round((np.array(churn_by_partner)[1][1] / sum_partner_array) * 100)
file.write("A share of opted out customers not having a partner: {}%\n".format(share_of_churn_partner_no))
file.write("A share of opted out customers having a partner: {}%\n".format(share_of_churn_partner) + "\n")

# A stacked bar chart and data written to the file of churn by having partner
churn_by_dependents = data.groupby(["Churn", "Dependents"]).size().unstack()
churn_by_dependents.plot(kind='bar',
                         stacked=True,
                         title="Count of churn by having dependents",
                         xlabel="Opted out",
                         fontsize=13)
plt.show()

file.write("A churn by having dependents: \n{}\n".format(churn_by_dependents) + "\n")

# Writes to the file a share of opted out customers having dependents
dependents_array = np.array(churn_by_dependents)
sum_dependents_array = np.sum(dependents_array)
share_of_churn_dependents_no = round((np.array(churn_by_dependents)[1][0] / sum_dependents_array) * 100)
share_of_churn_dependents = round((np.array(churn_by_dependents)[1][1] / sum_dependents_array) * 100)
file.write("A share of opted out customers having dependents: {}%\n".format(share_of_churn_dependents_no))
file.write("A share of opted out customers having dependents: {}%\n".format(share_of_churn_dependents) + "\n")
