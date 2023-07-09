# Customer Churn Analysis
Analysis of the customer base of a telecommunications company: which customers abandon the consumption of
the company's service.  

The goal is to find differences between customers who have abandoned the company's service in the past month and those
who have not, based on socio-demographic characteristics and consumed services. The hypothesis is that
customers who have opted out of the service and those who have not are significantly differentiated according to either
age group, type of family, or the volume, choice, service life expectancy or other indicators of the service consumption.
Analysis involves also finding the most profitable customers by mean of monthly charges and its relation to churn.  

At the moment, the analysis includes only part of the services.  

Libraries used for analysis: Panda, Matplotlib.  

Used IDE: IntelliJ IDEA Community Edition 2023.1.1.  

### Project Setup

Installed openpyxl.  

### Project Structure and Functionalities  

basic_data_insight.py - writes basic data insight to basic_insight.txt file.  
charges_by_socio_dem.py - creates charts and writes info to charges_by_socio_dem.txt file about analysis of the most
profitable customers by monthly charges.  
churn_by_socio_dem.py - creates charts and writes info to churn_by_socio_dem.txt file to analyse churn by socio-dem
characteristics.  
churn_by_services.py - creates charts and writes info to churn_by_services_dem.txt file to analyse churn by service
characteristics.

### Dataset

A fictional telco company's customer churn data provided by IBM.  

The object of the data are customers who are or were consumers of the company's services. The data consists of 
a unique CustomerID column, which is an anonymous identifier that distinguishes customers, socio-demographic 
identifiers and purchased services, and information about whether the customer has terminated the contract with 
the company within the past month.  

