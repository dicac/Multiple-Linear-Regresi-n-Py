# Multiple Linear Regression 
### Female Model
import pandas as pd 
import numpy as np 
regresion = pd.read_csv('linearregression/data.csv', delimiter = ';')

## Exploratory data analysis
data_f = regresion[['occ_ratef', 'avg_eduf', 'income_amf']]

### Heatmap
model_fcor = data_f.corr(method = "pearson")
model_fcor

import seaborn as sns
import matplotlib.pylab as plt

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))

sns.heatmap(model_fcor, annot = True, annot_kws = {"size": 12},
           xticklabels= model_fcor.columns,
           yticklabels= model_fcor.columns,
           cmap = 'pink_r')

ax.set_yticklabels(ax.get_xticklabels(), 
                   rotation = 0,
                   horizontalalignment = 'right')

### Dispersion and normality
x = sns.pairplot(data_f, diag_kind = "kde", height = 3, 
                 diag_kws= {'color': 'salmon'}, plot_kws={'color':'indianred'})
x.fig.suptitle("Female Model", y = 1.07, size = 18)

## Fit Linear Model
### Using scikit-learn
from sklearn.linear_model import LinearRegression

lmf = LinearRegression() 
predictors_f = regresion[['avg_eduf', 'income_amf']]
lmf.fit(predictors_f, regresion['occ_ratef'])
y_pred = lmf.predict(predictors_f)
print('Intercept:', lmf.intercept_)
print('Betas:', lmf.coef_)

### Confidence intervals
interv_ci = model_f.conf_int(alpha=0.05)
intervs_ci.columns = ['2.5%', '97.5%']
inter_ci

# # Y vs Ypredict
ax1 = sns.kdeplot(regresion['occ_ratef'], color = 'gray')
sns.kdeplot(y_pred[0], color = 'indianred')
plt.title('Current values vs fitted values for occupancy')
plt.xlabel('Occupancy (Rate)')
plt.ylabel('Proportion')

## Using statsmodels
from statsmodels.formula.api import ols

model_f = ols('occ_ratef ~ avg_eduf + income_amf', data = regresion).fit()
print(model_f.summary())

## Assumptions
regresion['regresion_pred'] = model_f.predict(predictors_f)
regresion['residuals'] = model_f.resid

### Linearity and homoscedasticity
def lin_hom_test(model, y):

    fitted_vals = model_f.predict()
    resids = model_f.resid

    fig, ax = plt.subplots(1,2)
    
    sns.regplot(x = fitted_vals, y = y, lowess = False, ax = ax[0], color = 'indianred', line_kws = {'color': 'indianred'})
    ax[0].set_title('Observed vs. Predicted Values', fontsize = 13)
    ax[0].set(xlabel = 'Predicted', ylabel='Observed')

    sns.regplot(x = fitted_vals, y = resids, lowess = False, color = 'indianred',ax = ax[1], line_kws = {'color': 'indianred'})
    ax[1].set_title('Residuals vs. Predicted Values', fontsize = 13)
    ax[1].set(xlabel = 'Predicted', ylabel ='Residuals')
    
lin_hom(model_f, regresion.occ_ratef)

#### Test Breush Pagan
import statsmodels.stats.diagnostic as smd
from statsmodels.compat import lzip

test_bp_modm = smd.het_breuschpagan(model_f.resid, model_f.model.exog)
print(test_bp_modm)

### Normality 
#### Q-Q Plot
import statsmodels.api as sm
import scipy.stats as stats

fig, ax = plt.subplots(1, figsize=(6, 4))

sm.qqplot(model_f.resid, stats.t, fit = True, line ='45', color='g', ax=ax)
ax.set_title('Q-Q',fontsize = 15)
ax.get_lines()[1].set_color("indianred")

#### Test Shapiro Wilk
from scipy.stats import shapiro
p_value = shapiro(x = model_f.resid)[1]
 
### No Multicollinearity
#### VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor
from patsy import dmatrices

y, X = dmatrices('occ_ratef ~ avg_eduf + income_amf', data = regresion, return_type='dataframe')

vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif['variable'] = X.columns

### No Autocorrelation
#### Test Durbin Watson
import statsmodels.stats.stattools as sm_tools
print(sm_tools.durbin_watson(model_f.resid)) 

#### Test Breusch Godfrey
import statsmodels.stats.diagnostic as smd
test_bg_modef = smd.acorr_breusch_godfrey(model_f, nlags = 2)

### Male Model
## Exploratory data analysis
data_m = regresion[['occ_ratem', 'avg_edum', 'income_amm']]
...

### Outlier identification
plt.boxplot(data_m['avg_edum'], vert=False)

Q1 = data_m['avg_edum'].quantile(0.25)
Q3 = data_m['avg_edum'].quantile(0.75)
IQR = Q3 - Q1

median = data_m['avg_edum'].median()
print("Median", median)

Min = data_m['avg_edum'].min()
Max = data_m['avg_edum'].max()

BI_cal = (Q1 - 1.5* IQR)
BS_cal = (Q3 + 1.5* IQR)

plt.boxplot(data_m['avg_edum'], vert=False)
