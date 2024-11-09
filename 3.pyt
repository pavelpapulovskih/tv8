import numpy as np
import scipy.stats as stats
# Данные
sigma = 5 # Стандартное отклонение (корень из дисперсии)
n = 27
mean_sample = 174.2
# Уровень значимости
alpha = 0.05
# Критическое значение Z для 95% доверительного интервала
z_crit = stats.norm.ppf(1 - alpha / 2)
# Доверительный интервал
margin_of_error = z_crit * (sigma / np.sqrt(n))
confidence_interval = (mean_sample - margin_of_error, mean_sample +
margin_of_error)
print(f"Доверительный интервал для среднего роста:{confidence_interval}")