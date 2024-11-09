import numpy as np
import scipy.stats as stats
# Данные
IQ = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
n = len(IQ)
mean_IQ = np.mean(IQ)
std_IQ = np.std(IQ, ddof=1)
# Уровень значимости
alpha = 0.05
# Критическое значение t для 95% доверительного интервала
t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
# Доверительный интервал
margin_of_error = t_crit * (std_IQ / np.sqrt(n))
confidence_interval = (mean_IQ - margin_of_error, mean_IQ +
margin_of_error)
print(f"Доверительный интервал для среднего IQ:{confidence_interval}")