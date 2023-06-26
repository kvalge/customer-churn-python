"""
Comparison of customer churn by consumed services
"""

from data.config import data

import matplotlib.pyplot as plt
import numpy as np

file = open("../text_output/churn_by_services.txt", "w")

# A pie chart and data written to the file of churn count
churn = data.groupby(["Churn"]).size()

colors = ["steelblue", "orange"]
churn.plot(kind="pie",
           autopct="%1.0f%%",
           colors=colors,
           title="Churn",
           fontsize=13)
plt.show()

file.write("{}\n".format(churn) + "\n")

# Writes to the file a share of opted out customers
churn_yes = np.array(churn)[1]
sum_churn = np.sum(np.array(churn))
share_of_churn_yes = round((churn_yes / sum_churn) * 100)
file.write("A share of opted out customers: {}%\n".format(share_of_churn_yes) + "\n")

# A pie chart and data written to the file of phone service count
phone = data.groupby(["Phone_Service"]).size()

colors = ["steelblue", "orange"]
phone.plot(kind="pie",
           autopct="%1.0f%%",
           colors=colors,
           title="Phone service",
           fontsize=13)
plt.show()

file.write("{}\n".format(phone) + "\n")

# Writes to the file a share of phone service
phone_no = np.array(phone)[0]
phone_yes = np.array(phone)[1]
sum_phone = np.sum(np.array(phone))
share_of_phone_no = round((phone_no / sum_phone) * 100)
share_of_phone_yes = round((phone_yes / sum_phone) * 100)
file.write("A share of customers not having phone service: {}%\n".format(share_of_phone_no))
file.write("A share of customers having phone service: {}%\n".format(share_of_phone_yes) + "\n")

# A stacked bar chart and data written to the file of churn by phone service
churn_by_phone_service = data.groupby(["Churn", "Phone_Service"]).size().unstack()

churn_by_phone_service.plot(kind='bar',
                            title="Count of churn by phone service",
                            xlabel="Opted out",
                            stacked=True,
                            fontsize=13)
plt.legend(title="Phone service")
plt.show()

file.write("A churn by phone service: \n{}\n".format(churn_by_phone_service) + "\n")

# Writes to the file a share of opted out customers by phone service
phone_array = np.array(churn_by_phone_service)
share_of_churn_no_phone = round((np.array(churn_by_phone_service)[1][0] / phone_no) * 100)
share_of_churn_phone = round((np.array(churn_by_phone_service)[1][1] / phone_yes) * 100)
file.write("A share of opted out customers not having a phone service: {}%\n".format(share_of_churn_no_phone))
file.write("A share of opted out customers having a phone service: {}%\n".format(share_of_churn_phone) + "\n")

# A pie chart and data written to the file of multiple lines count
multiple_lines = data.groupby(["Multiple_Lines"]).size()

colors = ["steelblue", "orange", "silver"]
labels = ["No multiple lines", "No phone service", "Multiple lines"]
multiple_lines.plot(kind="pie",
                         autopct="%1.0f%%",
                         colors=colors,
                         labels=labels,
                         title="Multiple lines",
                         fontsize=13)
plt.show()

file.write("{}\n".format(multiple_lines) + "\n")

# Writes to the file a share of multiple lines
multiple_lines_no = np.array(multiple_lines)[0]
phone_service_no = np.array(multiple_lines)[1]
multiple_lines_yes = np.array(multiple_lines)[2]
sum_phone = np.sum(np.array(multiple_lines))
share_of_multiple_lines_no = round((multiple_lines_no / sum_phone) * 100)
share_of_phone_service_no = round((phone_service_no / sum_phone) * 100)
share_of_multiple_lines_yes = round((multiple_lines_yes / sum_phone) * 100)
file.write("A share of customers not having multiple lines services: {}%\n".format(share_of_multiple_lines_no))
file.write("A share of customers not having phone service: {}%\n".format(share_of_phone_service_no))
file.write("A share of customers having multiple lines services: {}%\n".format(share_of_multiple_lines_yes) + "\n")

# A stacked bar chart and data written to the file of churn by multiple lines service
churn_by_multiple_lines = data.groupby(["Churn", "Multiple_Lines"]).size().unstack()

colors = ["steelblue", "orange", "silver"]
ax = churn_by_multiple_lines.plot(kind='bar',
                                  title="Count of churn by multiple lines",
                                  xlabel="Opted out",
                                  color=colors,
                                  stacked=True,
                                  fontsize=13)
ax.bar_label(ax.containers[0], size=10)
ax.bar_label(ax.containers[1], size=10)
ax.bar_label(ax.containers[2], size=10)
ax.legend(["No multiple lines", "No phone service", "Multiple lines"])
plt.show()

file.write("A churn by multiple lines: \n{}\n".format(churn_by_multiple_lines) + "\n")

# Writes to the file a share of opted out customers by multiple lines
multiple_lines_array = np.array(churn_by_multiple_lines)
share_of_churn_no_multiple_lines = round((np.array(churn_by_multiple_lines)[1][0] / multiple_lines_no) * 100)
share_of_churn_no_phone_service = round((np.array(churn_by_multiple_lines)[1][1] / phone_service_no) * 100)
share_of_churn_multiple_lines = round((np.array(churn_by_multiple_lines)[1][2] / multiple_lines_yes) * 100)

file.write("A share of opted out customers not having multiple lines: {}%\n"
           .format(share_of_churn_no_multiple_lines))
file.write("A share of opted out customers not having phone service: {}%\n"
           .format(share_of_churn_no_phone_service))
file.write("A share of opted out customers having multiple lines: {}%\n"
           .format(share_of_churn_multiple_lines) + "\n")

# A pie chart and data written to the file of internet service count
internet_service = data.groupby(["Internet_Service"]).size()

colors = ["steelblue", "orange", "silver"]
labels = ["DSL", "Fiber optic", "No"]
internet_service.plot(kind="pie",
                      autopct="%1.0f%%",
                      colors=colors,
                      labels=labels,
                      title="Internet service",
                      fontsize=13)
plt.show()

file.write("{}\n".format(internet_service) + "\n")

# Writes to the file a share of internet service
internet_dsl = np.array(internet_service)[0]
internet_fiber = np.array(internet_service)[1]
internet_no = np.array(internet_service)[2]
sum_internet = np.sum(np.array(internet_service))
share_of_internet_dsl = round((internet_dsl / sum_internet) * 100)
share_of_internet_fiber = round((internet_fiber / sum_internet) * 100)
share_of_internet_no = round((internet_no / sum_internet) * 100)
file.write("A share of customers having dsl internet: {}%\n".format(share_of_internet_dsl))
file.write("A share of customers having fiber internet: {}%\n".format(share_of_internet_fiber))
file.write("A share of customers not having internet service: {}%\n".format(share_of_internet_no) + "\n")

# A stacked bar chart and data written to the file of churn by internet service
churn_by_internet_service = data.groupby(["Churn", "Internet_Service"]).size().unstack()

colors = ["steelblue", "orange", "silver"]
ax = churn_by_internet_service.plot(kind='bar',
                                    title="Count of churn by internet service",
                                    xlabel="Opted out",
                                    color=colors,
                                    stacked=True,
                                    fontsize=13)
ax.bar_label(ax.containers[0], size=10)
ax.bar_label(ax.containers[1], size=10)
ax.bar_label(ax.containers[2], size=10)
ax.legend(["DSL", "Fiber optic", "No"])
plt.show()

file.write("A churn by internet service: \n{}\n".format(churn_by_internet_service) + "\n")

# Writes to the file a share of opted out customers by internet service
internet_service_array = np.array(churn_by_internet_service)
share_of_churn_internet_dsl = round((np.array(churn_by_internet_service)[1][0] / internet_dsl) * 100)
share_of_churn_internet_fiber = round((np.array(churn_by_internet_service)[1][1] / internet_fiber) * 100)
share_of_churn_internet_no = round((np.array(churn_by_internet_service)[1][2] / internet_no) * 100)

file.write("A share of opted out customers having dsl internet: {}%\n"
           .format(share_of_churn_internet_dsl))
file.write("A share of opted out customers having fiber internet: {}%\n"
           .format(share_of_churn_internet_fiber))
file.write("A share of opted out customers not having internet: {}%\n"
           .format(share_of_churn_internet_no) + "\n")

# A pie chart and data written to the file of online security service count
online_security = data.groupby(["Online_Security"]).size()

colors = ["steelblue", "orange", "silver"]
labels = ["No", "No internet service", "Yes"]
online_security.plot(kind="pie",
                     autopct="%1.0f%%",
                     colors=colors,
                     labels=labels,
                     title="Online security",
                     fontsize=13)
plt.show()

file.write("{}\n".format(online_security) + "\n")

# Writes to the file a share of online security service
security_no = np.array(online_security)[0]
internet_service_no = np.array(online_security)[1]
security_yes = np.array(online_security)[2]
sum_security = np.sum(np.array(online_security))
share_of_security_no = round((security_no / sum_security) * 100)
share_of_internet_service_no = round((internet_service_no / sum_security) * 100)
share_of_security_yes = round((security_yes / sum_security) * 100)
file.write("A share of customers not having online security service: {}%\n".format(share_of_security_no))
file.write("A share of customers not having internet service: {}%\n".format(share_of_internet_service_no))
file.write("A share of customers having online security service: {}%\n".format(share_of_security_yes) + "\n")

# A stacked bar chart and data written to the file of churn by online security service
churn_by_security = data.groupby(["Churn", "Online_Security"]).size().unstack()

colors = ["steelblue", "orange", "silver"]
ax = churn_by_security.plot(kind='bar',
                            title="Count of churn by online security",
                            xlabel="Opted out",
                            color=colors,
                            stacked=True,
                            fontsize=13)
ax.bar_label(ax.containers[0], size=10)
ax.bar_label(ax.containers[1], size=10)
ax.bar_label(ax.containers[2], size=10)
ax.legend(["No", "No internet service", "Yes"])
plt.show()

file.write("A churn by online security service: \n{}\n".format(churn_by_security) + "\n")

# Writes to the file a share of opted out customers by internet service
security_array = np.array(churn_by_security)
share_of_churn_security_no = round((np.array(churn_by_security)[1][0] / security_no) * 100)
share_of_churn_no_internet_service = round((np.array(churn_by_security)[1][1] / internet_service_no) * 100)
share_of_churn_security_yes = round((np.array(churn_by_security)[1][2] / security_yes) * 100)

file.write("A share of opted out customers not having online security: {}%\n"
           .format(share_of_churn_security_no))
file.write("A share of opted out customers not having internet service: {}%\n"
           .format(share_of_churn_no_internet_service))
file.write("A share of opted out customers having online security service: {}%\n"
           .format(share_of_churn_security_yes) + "\n")
