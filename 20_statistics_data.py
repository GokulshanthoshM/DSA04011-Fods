import numpy as np
from scipy import stats

conversion_rate_design_A = np.array([20,39,48,58,48,38,58,49,39,69,59,68,79,96,83])
conversion_rate_design_B = np.array([90,80,90,89,79,69,80,70,80,80,80,70,90,70,80])

n_A = len(conversion_rate_design_A)
n_B = len(conversion_rate_design_B)

mean_A = np.mean(conversion_rate_design_A)
    std_A = np.std(conversion_rate_design_A, ddof=1)  

mean_B = np.mean(conversion_rate_design_B)
std_B = np.std(conversion_rate_design_B, ddof=1)

pooled_std = np.sqrt(((n_A - 1) * std_A*2 + (n_B - 1) * std_B*2) / (n_A + n_B - 2))

t_statistic = (mean_A - mean_B) / (pooled_std * np.sqrt(1/n_A + 1/n_B))

df = n_A + n_B - 2

alpha = 0.05
critical_t = stats.t.ppf(1 - alpha/2, df)

p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), df))

if p_value < alpha:
    print("There is a statistically significant difference between the mean conversion rates.")
else:
    print("There is no statistically significant difference between the mean conversion rates.")
    
print("t-statistic:", t_statistic)
print("p-value:", p_value)
print("Critical t-value:", critical_t)