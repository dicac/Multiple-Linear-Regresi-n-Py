# Multiple Linear Regression - Python

### Incidence of education and income level on labor force participation

#### 1. Model specification
##### 1.1 Empirical basis
h1 = Positive relationship of the educational level, the higher the educational level, the greater the possibility of being part of the economically active population in the labor market.

h2 = Positive relationship of income level, indicating that the higher the income level there is a greater possibility of being part of the economically active population in the labor market.
##### 1.2 Variables

	“periodicity”, quarterly.
	“occ_ratem”, independent variable: quarterly occupancy rate.
	“avg_edu”, average employed population according to educational level. 
	“income_am”, average monthly labor income.
  
#### 2. Exploratory Data Analysis

#### 3. Fitted Model
### Using Scikit-learn

The first model corresponding to the female case is defined as follows  

	occ_ratef ~ avg_eduf + income_amf
	𝑜𝑐𝑢𝑝𝑎𝑡𝑖𝑜𝑛𝑟𝑎𝑛𝑔𝑒𝑓 = 79.11−6.13∗𝑎𝑣𝑔𝑒𝑑𝑢𝑚 + 0.000040∗𝑖𝑛𝑐𝑜𝑚𝑒𝑎𝑚𝑚

### Using Statsmodels

# SUMMARY

# Verifying the assumptions

# Linearity

The inspection of the plots shows that the linearity assumption is not satisfied.

