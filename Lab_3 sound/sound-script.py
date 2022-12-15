from math import sqrt

# Постоянные
X_H20 = 0.247  # Влажность воздуха
R = 8.31  # Универсальная газовая постоянная
T = 22.6 + 273  # Температура воздуха
m_a = 29 / 1e3  # Молярная масса воздуха
# Молярные массы
m_N2_O2_Ar = 28.97 / 1e3
m_H20 = 18.01 / 1e3
m_CO2 = 44.01 / 1e3
# Теплоёмкость при постоянном давлении
Cp_N2_O2_Ar = 1.0036
Cp_H2O = 1.863
Cp_CO2 = 0.838
# Теплоёмкость при постоянном объёме
Cv_N2_O2_Ar = 0.7166
Cv_H2O = 1.403
Cv_CO2 = 0.646
# Концентрации
X_N2_O2_Ar = (1 - X_H20) * (0.7808 + 0.2095 + 0.009)
X_CO2 = (1 - X_H20) * 0.03
# Показатель адиабаты
y = (m_N2_O2_Ar * Cp_N2_O2_Ar * X_N2_O2_Ar + m_H20 * Cp_H2O * X_H20 + m_CO2 * Cp_CO2 * X_CO2) / (m_N2_O2_Ar * Cv_N2_O2_Ar * X_N2_O2_Ar 
                                                                                                 + m_H20 * Cv_H2O * X_H20 + m_CO2 * Cv_CO2 * X_CO2)
print('Показатель адиабаты ' + str(y))

a = sqrt( y * R / m_a * T)
print('Скорость звука ' + str(a))

#  Строим функцию sqrt(b * (c * X_H20 + d * X_CO2 + e * (1 - X_H20 - X_CO2) / (f * X_H20 + g * X_CO2 + h * (1 - X_H20 - X_CO2)) 
b = R / m_a * T 
print('b = ' + str(round(b, 3)))
c = m_H20 * Cp_H2O
print('c = ' + str(round(c, 3)))
d = m_CO2 * Cp_CO2
print('d = ' + str(round(d, 3)))
e = m_N2_O2_Ar * Cp_N2_O2_Ar
print('e = ' + str(round(e, 3)))
f = m_H20 * Cv_H2O
print('f = ' + str(round(f, 3)))
g = m_CO2 * Cv_CO2
print('g = ' + str(round(g, 3)))
i = e = m_N2_O2_Ar * Cv_N2_O2_Ar
print('i = ' + str(round(i, 3)))

