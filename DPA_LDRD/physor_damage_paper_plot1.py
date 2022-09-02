import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2, loglaplace
from labellines import labelLine, labelLines

fluence = [1e19, 5e19, 1e20, 5e20, 1e21, 5e21, 1e22, 5e22, 1e23, 5e23, 1e24]
ni_58 = [6.829686171860570E-01, 6.828429625210690E-01, 6.826859266995030E-01, 6.814309395366290E-01, 6.798654493794970E-01, 6.674703100985240E-01, 6.522936930917990E-01, 5.426664778933900E-01, 4.311667516384240E-01, 6.847679371809340E-02, 6.865404160020330E-03]
ni_59 = [3.140283135426700E-05, 1.567112179771040E-04, 3.126671803814050E-04, 1.533539286569930E-03, 2.994610568656570E-03, 1.243702939263600E-02, 2.000553548926880E-02, 2.820005651228220E-02, 2.268935482755220E-02, 3.604041774636440E-03, 3.613370610537190E-04]
ni_60 = [3.169999781609230E-01, 3.170002807780940E-01, 3.170012244811000E-01, 3.170310380741070E-01, 3.171222910909940E-01, 3.197027120121040E-01, 3.263515393726600E-01, 4.149948938476750E-01, 5.172518330471400E-01, 8.508902220281040E-01, 9.075670609350650E-01]
he_4 = [1.821657464604730E-09, 4.548284144429530E-08, 1.816389968791890E-07, 4.483102664593880E-06, 1.764896082265470E-05, 3.899484967046360E-04, 1.349232046237440E-03, 1.413857174661280E-02, 2.889206048683440E-02, 7.702894247911260E-02, 8.520619784379850E-02]
dpa_err = [-0.009017583, -0.008831059, -0.008807226, -0.008260575, -0.006047231, -0.021926635, -0.023632103, -0.022672706, -0.024240248, -0.016795413, -0.002188093]

fig, ax = plt.subplots()

plt.plot(fluence, ni_58, label='Ni-58', color='black', linestyle='solid')
plt.plot(fluence, ni_59, label='Ni-59', color='black', linestyle='dotted')
plt.plot(fluence, ni_60, label='Ni-60', color='black', linestyle='dashed')
plt.plot(fluence, he_4, label='He-4 & Fe-56', color='black', linestyle='dashdot')
labelLines(plt.gca().get_lines(), xvals=[2e19, 2e19, 2e20, 2e19])
plt.scatter(fluence, ni_58, s=16, label='Ni-58', marker='D', color='black')
plt.scatter(fluence, ni_59, s=16, label='Ni-59', marker='X', color='black')
plt.scatter(fluence, ni_60, s=16, label='Ni-60', marker='s', color='black')
plt.scatter(fluence, he_4, s=16, label='He-4 & Fe-56', marker='o', color='black')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Neutron Fluence [n/cm^2]")
ax.set_ylabel("Number Fraction [-]")
plt.show()

fig.savefig("num_fractions.svg", format='SVG', bbox_inches='tight')
