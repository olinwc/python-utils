import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Points in Time
t = [3.6000000E+03, 7.2000000E+03, 1.4400000E+04, 2.1600000E+04, 8.6400000E+04, 1.7280000E+05, 2.5920000E+05, 3.4560000E+05, 4.3200000E+05, 8.6400000E+05, 1.7280000E+06, 2.5920000E+06, 3.4560000E+06, 4.3200000E+06, 8.6400000E+06, 1.2960000E+07, 1.7280000E+07, 2.1600000E+07, 2.5920000E+07, 3.0240000E+07, 3.4560000E+07, 3.8880000E+07, 4.3200000E+07, 4.3200001E+07, 4.3200010E+07, 4.3200060E+07, 4.3203600E+07, 4.3207200E+07, 4.3236000E+07, 4.3286400E+07, 4.3372800E+07, 4.3459200E+07, 4.3545600E+07, 4.3632000E+07, 4.4064000E+07, 4.4928000E+07, 4.5792000E+07, 4.6656000E+07, 4.7520000E+07, 5.1840000E+07]

# Absolute relative diff of Total XS
total_xs_diff = [2.76E-06, 3.77E-06, 5.28E-06, 6.40E-06, 9.32E-06, 9.09E-06, 8.50E-06, 7.95E-06, 7.49E-06, 6.21E-06, 6.08E-06, 6.76E-06, 7.41E-06, 7.89E-06, 8.31E-06, 6.97E-06, 4.96E-06, 2.89E-06, 1.14E-06, 1.51E-08, 2.56E-07, 5.52E-07, 2.66E-06, 2.66E-06, 2.63E-06, 2.47E-06, 4.46E-07, 1.95E-06, 7.33E-06, 8.58E-06, 7.08E-06, 5.45E-06, 4.21E-06, 3.33E-06, 1.55E-06, 1.86E-06, 3.15E-06, 4.49E-06, 5.70E-06, 9.94E-06]

# Absolute relative diff of Fission XS
fission_xs_diff = [4.87E-12, 7.53E-12, 1.10E-11, 1.30E-11, 2.59E-11, 2.09E-10, 5.02E-10, 8.73E-10, 1.30E-09, 3.72E-09, 8.13E-09, 1.12E-08, 1.32E-08, 1.41E-08, 6.05E-09, 2.14E-08, 6.90E-08, 1.36E-07, 2.19E-07, 3.11E-07, 4.01E-07, 4.82E-07, 5.47E-07, 5.47E-07, 5.46E-07, 5.43E-07, 3.19E-07, 9.48E-08, 1.25E-06, 2.39E-06, 2.95E-06, 3.05E-06, 3.07E-06, 3.07E-06, 3.07E-06, 3.07E-06, 3.07E-06, 3.06E-06, 3.06E-06, 3.03E-06]

# Shifted values for decay region
t_2 = [1.0000E+00, 1.0000E+01, 6.0000E+01, 3.6000E+03, 7.2000E+03, 3.6000E+04, 8.6400E+04, 1.7280E+05, 2.5920E+05, 3.4560E+05, 4.3200E+05, 8.6400E+05, 1.7280E+06, 2.5920E+06, 3.4560E+06, 4.3200E+06, 8.6400E+06]
total_2 = [2.66E-06, 2.63E-06, 2.47E-06, 4.46E-07, 1.95E-06, 7.33E-06, 8.58E-06, 7.08E-06, 5.45E-06, 4.21E-06, 3.33E-06, 1.55E-06, 1.86E-06, 3.15E-06, 4.49E-06, 5.70E-06, 9.94E-06]
fission_2 = [5.47E-07, 5.46E-07, 5.43E-07, 3.19E-07, 9.48E-08, 1.25E-06, 2.39E-06, 2.95E-06, 3.05E-06, 3.07E-06, 3.07E-06, 3.07E-06, 3.07E-06, 3.07E-06, 3.06E-06, 3.06E-06, 3.03E-06]

total_xs_diff = pd.Series(total_2)
fission_xs_diff = pd.Series(fission_2)

fig, ax = plt.subplots()
font_size = 16
ax.scatter(t_2, total_xs_diff,  s=10,  label='Total',  c='k',  marker='.')
ax.scatter(t_2, fission_xs_diff,  s=10,  label='Fission',  c='k',  marker='^')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(bbox_to_anchor=(1.02,1.03), loc='upper left', prop={'size': font_size})
ax.set_xlabel("Time (t - 500 days) [s]")
ax.set_ylabel("Absolute Relative Difference [-]")
xticks = [1e-1, 1e1, 1e3, 1e5, 1e7]
ax.set_xticks(xticks)
yticks = [1e-7, 1e-6, 1e-5]
ax.set_yticks(yticks)
plt.xlim([1e-1, 1e7])
plt.ylim([5e-8, 2e-5])
ax.xaxis.label.set_fontsize(font_size)
ax.yaxis.label.set_fontsize(font_size)
# changes exponent size
temp = ax.xaxis.get_offset_text()
temp.set_size(font_size-2)
for item in ax.get_xticklabels() + ax.get_yticklabels():
    item.set_fontsize(font_size-2)
#plt.ylim([0.0, 0.05])
#plt.locator_params(axis='|', numticks=5)
plt.subplots_adjust(right=0.76)
plt.show()

fig.savefig("no_de_initial_xs_2.pdf", format='PDF', bbox_inches='tight')
