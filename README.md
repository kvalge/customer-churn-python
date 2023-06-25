# Customer Churn Analysis
Analysis of the customer base of a telecommunications company: which customers abandon the consumption of
the company's service.  

The goal is to find differences between customers who have abandoned the company's service in the past month and those
who have not, based on socio-demographic characteristics and consumed services. The hypothesis is that
customers who have opted out of the service and those who have not are significantly differentiated according to either
age group, type of family, or the volume, choice, service life expectancy or other indicators of the service consumption.
Analysis involves also finding the most profitable customers by mean of monthly charges and its relation to churn.  
  

Libraries used for analysis: Panda, Matplotlib.  

Used IDE: IntelliJ IDEA Community Edition 2023.1.1.  

### Project Setup

Installed openpyxl.  

### Project Structure and Functionalities  

basic_data_insight.py - writes basic data insight to basic_insight.txt file.  
charges_by_socio_dem.py - creates charts and writes data to charges_by_socio_dem.txt file about analysis of the most
profitable customers by monthly charges.  

### Dataset

A fictional telco company's customer churn data provided by IBM.  

The object of the data are customers who are or were consumers of the company's services. The data consists of 
a unique CustomerID column, which is an anonymous identifier that distinguishes customers, socio-demographic 
identifiers and purchased services, and information about whether the customer has terminated the contract with 
the company within the past month.  

Description of columns:  
LoyaltyID.  
Customer_ID: A unique ID that identifies each customer.  
Senior_Citizen: Indicates if the customer is up to 65 or older: Yes, No.  
Partner: Indicates if the customer has partner: Yes, No.  
Dependents: Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents,
grandparents, etc.  
Tenure: Indicates the total amount of months that the customer has been with the company by the end of the
quarter specified above.  
Phone_Service: Indicates if the customer subscribes to home phone service with the company: Yes, No.  
Multiple_Lines: Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No.  
Internet_Service: Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic.  
Online_Security: Indicates if the customer subscribes to an additional online security service provided by
the company: Yes, No.  
Online_Backup: Indicates if the customer subscribes to an additional online backup service provided by the company:
Yes, No.  
Device_Protection: Indicates if the customer subscribes to an additional device protection plan for their
Internet equipment provided by the company: Yes, No.  
Tech_Support: Indicates if the customer subscribes to an additional technical support plan from the company with
reduced wait times: Yes, No.  
Streaming_TV: Indicates if the customer uses their Internet service to stream television programing from a third
party provider: Yes, No. The company does not charge an additional fee for this service.  
Streaming_Movies: Indicates if the customer uses their Internet service to stream movies from a third party
provider: Yes, No. The company does not charge an additional fee for this service.  
Contract: Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year.  
Paperless_Billing: Indicates if the customer has chosen paperless billing: Yes, No.  
Payment_Method: Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check.  
Monthly_Charges: Indicates the customer’s current total monthly charge for all their services from the company.  
Total_Charges: Indicates the customer’s total charges, calculated to the end of the quarter specified above.  
Churn: Yes = the customer left the company within last month. No = the customer remained with the company.  
