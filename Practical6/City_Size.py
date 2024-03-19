uk_cities=[0.56,0.62,0.04,9.7]
cn_cities=[0.58,8.4,29.9,22.2]
uk_cities.sort()
cn_cities.sort()
print("sorted population of uk_cities is ")
print(uk_cities)
print("sorted population of cn_cities is ")
print(cn_cities)

import matplotlib.pyplot as plt
uk_cities=[0.56,0.62,0.04,9.7]
cn_cities=[0.58,8.4,29.9,22.2]
ind_uk=["Edinburgh", "Glasgow", "Stirling","London"]
ind_cn=["Haining","Hangzhou","Shanghai","Beijing"]

plt.figure()
plt.ylabel("pupulation(millions)")
plt.xlabel("uk_cities")
plt.bar(ind_uk,uk_cities)
plt.show()
plt.clf()

plt.figure()
plt.ylabel("pupulation(millions)")
plt.xlabel("cn_cities")
plt.bar(ind_cn,cn_cities)
plt.show()
plt.clf()