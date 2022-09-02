import numpy as np
import matplotlib.pyplot as plt

time_1 =        [5.184e+7]

diff_1 =        [3.3677e+6]

cumul_diff_1 =  [3.3677e+6]

time_2 =        [2.592e+7, 5.184e+7]

diff_2 =        [3.1393e+6, -0.0459]

cumul_diff_2 =  [3.1393e+6,  0.8489]

time_4 =        [1.296e+7, 2.592e+7, 3.888e+7, 5.184e+7]

diff_4 =        [2.8624e+6, -0.0141, 0.0029, 0.0119]

cumul_diff_4 =  [2.8624e+6,  0.8602, 0.4302, 0.2894]

time_8 =        [6.48e+6, 1.296e+7, 1.944e+7, 2.592e+7, 3.24e+7, 3.888e+7, 4.536e+7, 5.184e+7]

diff_8 =        [2.5645e+6, 0.0152, 0.0069, 0.0058, 0.0062, 0.0072, 0.0084, 0.0095]

cumul_diff_8 =  [2.5645e+6, 0.8685, 0.4278, 0.2830, 0.2115, 0.1692, 0.1414, 0.1218]

time_16 = [3.2400E+06, 6.4800E+06, 9.7200E+06, 1.2960E+07, 1.6200E+07, 1.9440E+07, 2.2680E+07, 2.5920E+07, 2.9160E+07, 3.2400E+07, 3.5640E+07, 3.8880E+07, 4.2120E+07, 4.5360E+07, 4.8600E+07, 5.1840E+07]

diff_16 =       [2.2404e+6, 0.0401, 0.0149, 0.0096, 0.0073, 0.0060, 0.0053, 0.0049, 0.0048, 0.0048, 0.0049, 0.0051, 0.0053, 0.0055, 0.0057, 0.0059]

cumul_diff_16 = [2.2404e+6, 0.8619, 0.4224, 0.2782, 0.2070, 0.1646, 0.1366, 0.1167, 0.1020, 0.0906, 0.0815, 0.0742, 0.0681, 0.0630, 0.0587, 0.0550]

time_32 = [1.6200E+06, 3.2400E+06, 4.8600E+06, 6.4800E+06, 8.1000E+06, 9.7200E+06, 1.1340E+07, 1.2960E+07, 1.4580E+07, 1.6200E+07, 1.7820E+07, 1.9440E+07, 2.1060E+07, 2.2680E+07, 2.4300E+07, 2.5920E+07, 2.7540E+07, 2.9160E+07, 3.0780E+07, 3.2400E+07, 3.4020E+07, 3.5640E+07, 3.7260E+07, 3.8880E+07, 4.0500E+07, 4.2120E+07, 4.3740E+07, 4.5360E+07, 4.6980E+07, 4.8600E+07, 5.0220E+07, 5.1840E+07]

diff_32 =       [1883297.3573, 0.0639, 0.0258, 0.0149, 0.0104, 0.0082, 0.0069, 0.0060, 0.0053, 0.0048, 0.0044, 0.0041, 0.0039, 0.0037, 0.0036, 0.0035, 0.0034, 0.0034, 0.0034, 0.0034, 0.0034, 0.0034, 0.0034, 0.0034, 0.0034, 0.0035, 0.0035, 0.0036, 0.0036, 0.0036, 0.0037, 0.0037]

cumul_diff_32 = [1883297.3573, 0.8417, 0.4116, 0.2703, 0.2006, 0.1593, 0.1320, 0.1126, 0.0982, 0.0870, 0.0782, 0.0709, 0.0649, 0.0599, 0.0556, 0.0519, 0.0486, 0.0458, 0.0433, 0.0410, 0.0390, 0.0372, 0.0356, 0.0341, 0.0327, 0.0314, 0.0303, 0.0292, 0.0283, 0.0274, 0.0265, 0.0257]

time_64 = [810000, 1620000, 2430000, 3240000, 4050000, 4860000, 5670000, 6480000, 7290000, 8100000, 8910000, 9720000, 10530000, 11340000, 12150000, 12960000, 13770000, 14580000, 15390000, 16200000, 17010000, 17820000, 18630000, 19440000, 20250000, 21060000, 21870000, 22680000, 23490000, 24300000, 25110000, 25920000, 26730000, 27540000, 28350000, 29160000, 29970000, 30780000, 31590000, 32400000, 33210000, 34020000, 34830000, 35640000, 36450000, 37260000, 38070000, 38880000, 39690000, 40500000, 41310000, 42120000, 42930000, 43740000, 44550000, 45360000, 46170000, 46980000, 47790000, 48600000, 49410000, 50220000, 51030000, 51840000]

diff_64 =       [1491510.3195, 0.0972, 0.0376, 0.0226, 0.0157, 0.0117, 0.0093, 0.0078, 0.0067, 0.0060, 0.0054, 0.0050, 0.0047, 0.0044, 0.0041, 0.0039, 0.0037, 0.0036, 0.0034, 0.0033, 0.0032, 0.0031, 0.0030, 0.0029, 0.0029, 0.0028, 0.0028, 0.0027, 0.0027, 0.0027, 0.0026, 0.0026, 0.0026, 0.0026, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0026, 0.0026, 0.0026, 0.0026, 0.0026, 0.0026, 0.0026, 0.0026]

cumul_diff_64 = [1491510.3195, 0.8187, 0.3981, 0.2610, 0.1934, 0.1532, 0.1267, 0.1080, 0.0940, 0.0833, 0.0747, 0.0678, 0.0620, 0.0572, 0.0530, 0.0494, 0.0463, 0.0436, 0.0411, 0.0390, 0.0370, 0.0353, 0.0337, 0.0322, 0.0309, 0.0297, 0.0286, 0.0275, 0.0266, 0.0257, 0.0248, 0.0241, 0.0233, 0.0227, 0.0220, 0.0214, 0.0209, 0.0203, 0.0198, 0.0193, 0.0189, 0.0185, 0.0180, 0.0177, 0.0173, 0.0169, 0.0166, 0.0163, 0.0160, 0.0157, 0.0154, 0.0151, 0.0149, 0.0146, 0.0144, 0.0141, 0.0139, 0.0137, 0.0135, 0.0133, 0.0131, 0.0129, 0.0127, 0.0126]

time_128 = [405000, 810000, 1215000, 1620000, 2025000, 2430000, 2835000, 3240000, 3645000, 4050000, 4455000, 4860000, 5265000, 5670000, 6075000, 6480000, 6885000, 7290000, 7695000, 8100000, 8505000, 8910000, 9315000, 9720000, 10125000, 10530000, 10935000, 11340000, 11745000, 12150000, 12555000, 12960000, 13365000, 13770000, 14175000, 14580000, 14985000, 15390000, 15795000, 16200000, 16605000, 17010000, 17415000, 17820000, 18225000, 18630000, 19035000, 19440000, 19845000, 20250000, 20655000, 21060000, 21465000, 21870000, 22275000, 22680000, 23085000, 23490000, 23895000, 24300000, 24705000, 25110000, 25515000, 25920000, 26325000, 26730000, 27135000, 27540000, 27945000, 28350000, 28755000, 29160000, 29565000, 29970000, 30375000, 30780000, 31185000, 31590000, 31995000, 32400000, 32805000, 33210000, 33615000, 34020000, 34425000, 34830000, 35235000, 35640000, 36045000, 36450000, 36855000, 37260000, 37665000, 38070000, 38475000, 38880000, 39285000, 39690000, 40095000, 40500000, 40905000, 41310000, 41715000, 42120000, 42525000, 42930000, 43335000, 43740000, 44145000, 44550000, 44955000, 45360000, 45765000, 46170000, 46575000, 46980000, 47385000, 47790000, 48195000, 48600000, 49005000, 49410000, 49815000, 50220000, 50625000, 51030000, 51435000, 51840000]

diff_128 =       [1102535.042675, 0.154992, 0.057380, 0.031535, 0.021435, 0.016255, 0.013055, 0.010851, 0.009242, 0.008029, 0.007094, 0.006363, 0.005783, 0.005318, 0.004940, 0.004629, 0.004371, 0.004154, 0.003969, 0.003809, 0.003670, 0.003548, 0.003439, 0.003342, 0.003253, 0.003173, 0.003099, 0.003031, 0.002969, 0.002910, 0.002856, 0.002805, 0.002758, 0.002713, 0.002671, 0.002632, 0.002595, 0.002560, 0.002527, 0.002497, 0.002467, 0.002440, 0.002414, 0.002390, 0.002367, 0.002345, 0.002324, 0.002305, 0.002287, 0.002270, 0.002254, 0.002239, 0.002224, 0.002211, 0.002199, 0.002187, 0.002176, 0.002165, 0.002156, 0.002146, 0.002138, 0.002130, 0.002122, 0.002116, 0.002109, 0.002103, 0.002097, 0.002092, 0.002087, 0.002083, 0.002079, 0.002075, 0.002072, 0.002068, 0.002065, 0.002063, 0.002060, 0.002058, 0.002056, 0.002054, 0.002053, 0.002052, 0.002050, 0.002049, 0.002048, 0.002048, 0.002047, 0.002047, 0.002046, 0.002046, 0.002046, 0.002046, 0.002046, 0.002046, 0.002046, 0.002047, 0.002047, 0.002048, 0.002048, 0.002049, 0.002049, 0.002050, 0.002051, 0.002052, 0.002053, 0.002053, 0.002054, 0.002055, 0.002056, 0.002057, 0.002058, 0.002059, 0.002061, 0.002062, 0.002063, 0.002064, 0.002065, 0.002066, 0.002067, 0.002069, 0.002070, 0.002071, 0.002072, 0.002073, 0.002074, 0.002076, 0.002077, 0.002078]

cumul_diff_128 = [1102535.042675, 0.832818, 0.399093, 0.258897, 0.190666, 0.150577, 0.124272, 0.105712, 0.091929, 0.081299, 0.072857, 0.065996, 0.060314, 0.055534, 0.051459, 0.047946, 0.044887, 0.042200, 0.039823, 0.037704, 0.035805, 0.034092, 0.032541, 0.031129, 0.029839, 0.028655, 0.027566, 0.026559, 0.025627, 0.024761, 0.023954, 0.023201, 0.022496, 0.021835, 0.021214, 0.020630, 0.020079, 0.019558, 0.019065, 0.018599, 0.018156, 0.017736, 0.017336, 0.016955, 0.016592, 0.016245, 0.015914, 0.015598, 0.015295, 0.015004, 0.014726, 0.014459, 0.014202, 0.013955, 0.013718, 0.013489, 0.013269, 0.013057, 0.012853, 0.012655, 0.012465, 0.012281, 0.012103, 0.011930, 0.011764, 0.011602, 0.011446, 0.011295, 0.011148, 0.011005, 0.010867, 0.010733, 0.010603, 0.010476, 0.010353, 0.010233, 0.010117, 0.010004, 0.009893, 0.009786, 0.009681, 0.009580, 0.009480, 0.009384, 0.009289, 0.009197, 0.009107, 0.009020, 0.008934, 0.008850, 0.008769, 0.008689, 0.008611, 0.008535, 0.008460, 0.008387, 0.008316, 0.008246, 0.008178, 0.008111, 0.008046, 0.007981, 0.007919, 0.007857, 0.007797, 0.007738, 0.007680, 0.007623, 0.007567, 0.007513, 0.007459, 0.007407, 0.007355, 0.007305, 0.007255, 0.007206, 0.007158, 0.007111, 0.007065, 0.007020, 0.006975, 0.006931, 0.006888, 0.006846, 0.006804, 0.006763, 0.006723, 0.006684]

fig, ax = plt.subplots()
font_size = 16

#ax.scatter(time_1,   diff_1,          s=10,  label='1 ID',   c='grey',  marker='.')
#ax.scatter(time_1,   cumul_diff_1,    s=10,  label='1 CD',   c='k',     marker='.')
#ax.scatter(time_2,   diff_2,          s=10,  label='2 ID',   c='grey',  marker=10)
#ax.scatter(time_2,   cumul_diff_2,    s=10,  label='2 CD',   c='k',     marker=10)
#ax.scatter(time_4,   diff_4,          s=10,  label='4 ID',   c='grey',  marker=8)
#ax.scatter(time_4,   cumul_diff_4,    s=10,  label='4 CD',   c='k',     marker=8)
#ax.scatter(time_8,   diff_8,          s=10,  label='8 ID',   c='grey',  marker=9)
#ax.scatter(time_8,   cumul_diff_8,    s=10,  label='8 CD',   c='k',     marker=9)
#ax.scatter(time_16,  diff_16,         s=10,  label='16 ID',  c='grey',  marker=11)
#ax.scatter(time_16,  cumul_diff_16,   s=10,  label='16 CD',  c='k',     marker=11)
ax.scatter(time_32,  diff_32,         s=10,  label='32 ID',  c='grey',  marker=10)
ax.scatter(time_32,  cumul_diff_32,   s=10,  label='32 CD',  c='k',     marker=10)
ax.scatter(time_64,  diff_64,         s=10,  label='64 ID',  c='grey',  marker='_')
ax.scatter(time_64,  cumul_diff_64,   s=10,  label='64 CD',  c='k',     marker='_')
ax.scatter(time_128, diff_128,        s=10,  label='128 ID', c='grey',  marker='|')
ax.scatter(time_128, cumul_diff_128,  s=10,  label='128 CD', c='k',     marker='|')
#ax.scatter(fluence, dpa_err, s=16, label='DPA Difference')
ax.set_xscale('linear')
ax.set_yscale('linear')
ax.legend(bbox_to_anchor=(1.02,1.03), loc='upper left', prop={'size': font_size})
ax.set_xlabel("Time [s]")
ax.set_ylabel("Relative Difference [-]")
xticks = [0, 1e+7, 2e+7, 3e+7, 4e+7, 5e+7]
ax.set_xticks(xticks)
yticks = [0.0, 0.3, 0.6, 0.9]
#yticks = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05]
ax.set_yticks(yticks)
plt.xlim([0, 5.3e+7])
plt.ylim([0, 0.9])
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

fig.savefig("quarter_pin_decay_energy_diff_2.pdf", format='PDF', bbox_inches='tight')
