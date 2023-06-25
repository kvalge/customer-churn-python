"""
Comparison of customers mean of monthly charges by socio-demographic characteristics
"""

import pandas as pd
import matplotlib.pyplot as plt

file = open("text_output/charges_by_socio_dem.txt", "w")

data = pd.read_excel("data/customer_churn.xlsx")

# A histogram of share of monthly charges
data.hist("Monthly_Charges")
plt.title("Monthly charges")
plt.show()

# A bar chart of mean of monthly charges by age group
monthly_charges_by_age_group = data.groupby(["Senior_Citizen"])["Monthly_Charges"].mean()

ax = monthly_charges_by_age_group.plot(kind="bar", figsize=(10, 6), fontsize=13);
ax.set_alpha(0.8)
ax.set_title("Mean of monthly charges by age group", fontsize=22)
ax.set_xlabel("Age of over 65")
ax.set_ylabel("Monthly charges mean")
plt.show()

file.write("Mean of monthly charges by age group: \n{}\n"
           .format(monthly_charges_by_age_group) + "\n")

# A bar chart of mean of monthly charges by having partner
monthly_charges_by_having_partner = data.groupby(["Partner"])["Monthly_Charges"].mean()

ax = monthly_charges_by_having_partner.plot(kind="bar", figsize=(10, 6), fontsize=13);
ax.set_alpha(0.8)
ax.set_title("Mean of monthly charges by having a partner", fontsize=22)
ax.set_xlabel("Partner")
ax.set_ylabel("Monthly charges mean")
plt.show()

file.write("Mean of monthly charges by having partner: \n{}\n"
           .format(monthly_charges_by_having_partner) + "\n")

# A bar chart of mean of monthly charges by having dependents
monthly_charges_by_having_dependents = data.groupby(["Dependents"])["Monthly_Charges"].mean()

ax = monthly_charges_by_having_dependents.plot(kind="bar", figsize=(10, 6), fontsize=13);
ax.set_alpha(0.8)
ax.set_title("Mean of monthly charges by having a dependents", fontsize=22)
ax.set_xlabel("Dependents")
ax.set_ylabel("Monthly charges mean")
plt.show()

file.write("Mean of monthly charges by having dependents: \n{}\n"
           .format(monthly_charges_by_having_dependents) + "\n")

# A plot chart of mean of monthly charges by age group having partner or not
monthly_mean_by_age_and_partner = data.groupby(["Senior_Citizen", "Partner"])["Monthly_Charges"].mean().unstack()
monthly_mean_by_age_and_partner.plot(
    title="Mean of monthly charges by age group having partner or not",
    xlabel="Age of over 65", ylabel="Mean of monthly charges", figsize=(10, 6), fontsize=13)
plt.show()

file.write("Mean of monthly charges by age group and by having partner or not: \n{}\n"
           .format(monthly_mean_by_age_and_partner) + "\n")

# A plot chart of mean of monthly charges by age group having dependents or not
monthly_mean_by_age_and_dependents = data.groupby(["Senior_Citizen", "Dependents"])["Monthly_Charges"].mean().unstack()
monthly_mean_by_age_and_dependents.plot(
    title="Mean of monthly charges by age group having Dependents or not",
    xlabel="Age of over 65", ylabel="Mean of monthly charges", figsize=(10, 6), fontsize=13)
plt.show()

file.write("Mean of monthly charges by age group and by having dependents or not: \n{}\n"
           .format(monthly_mean_by_age_and_dependents) + "\n")

# A bar chart of mean of monthly charges by churn
monthly_charges_by_churn = data.groupby(["Churn"])["Monthly_Charges"].mean()

ax = monthly_charges_by_churn.plot(kind="bar", figsize=(10, 6), fontsize=13);
ax.set_alpha(0.8)
ax.set_title("Mean of monthly charges by churn", fontsize=22)
ax.set_xlabel("Opted out")
ax.set_ylabel("Monthly charges mean")
plt.show()

file.write("Mean of monthly charges by churn: \n{}\n"
           .format(monthly_charges_by_churn) + "\n")

# A plot chart of mean of monthly charges by age group and by churn
monthly_mean_by_age_and_churn = data.groupby(["Churn", "Senior_Citizen"])["Monthly_Charges"].mean().unstack()
monthly_mean_by_age_and_churn.plot(
    title="Mean of monthly charges by age group opted out of the service or not",
    xlabel="Opted out", ylabel="Mean of monthly charges", figsize=(10, 6), fontsize=13)
plt.legend(title="Age of over 65")
plt.show()

file.write("Mean of monthly charges by age group opted out of the service or not: \n{}\n"
           .format(monthly_mean_by_age_and_churn) + "\n")

# A plot chart of mean of monthly charges by having partner and by churn
monthly_mean_by_partner_and_churn = data.groupby(["Churn", "Partner"])["Monthly_Charges"].mean().unstack()
monthly_mean_by_partner_and_churn.plot(
    title="Mean of monthly charges by having partner opted out of the service or not",
    xlabel="Opted out", ylabel="Mean of monthly charges", figsize=(10, 6), fontsize=13)
plt.show()

file.write("Mean of monthly charges by having partner opted out of the service or not: \n{}\n"
           .format(monthly_mean_by_partner_and_churn) + "\n")

# A plot chart of mean of monthly charges by having dependents and by churn
monthly_mean_by_dependents_and_churn = data.groupby(["Churn", "Dependents"])["Monthly_Charges"].mean().unstack()
monthly_mean_by_dependents_and_churn.plot(
    title="Mean of monthly charges by having dependent opted out of the service or not",
    xlabel="Opted out", ylabel="Mean of monthly charges", figsize=(10, 6), fontsize=13)
plt.show()

file.write("Mean of monthly charges by having dependent opted out of the service or not: \n{}\n"
           .format(monthly_mean_by_dependents_and_churn) + "\n")
