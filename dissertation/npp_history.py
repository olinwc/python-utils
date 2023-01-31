import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from scipy.stats import chi2, loglaplace
from labellines import labelLine, labelLines

# CRAM-DMI-48 Number Densities t=10 days
dates = ['01/01/1954','01/01/1955','01/01/1956','01/01/1957','01/01/1958','01/01/1959',
         '01/01/1960','01/01/1961','01/01/1962','01/01/1963','01/01/1964','01/01/1965','01/01/1966','01/01/1967','01/01/1968','01/01/1969',
         '01/01/1970','01/01/1971','01/01/1972','01/01/1973','01/01/1974','01/01/1975','01/01/1976','01/01/1977','01/01/1978','01/01/1979',
         '01/01/1980','01/01/1981','01/01/1982','01/01/1983','01/01/1984','01/01/1985','01/01/1986','01/01/1987','01/01/1988','01/01/1989',
         '01/01/1990','01/01/1991','01/01/1992','01/01/1993','01/01/1994','01/01/1995','01/01/1996','01/01/1997','01/01/1998','01/01/1999',
         '01/01/2000','01/01/2001','01/01/2002','01/01/2003','01/01/2004','01/01/2005','01/01/2006','01/01/2007','01/01/2008','01/01/2009',
         '01/01/2010','01/01/2011','01/01/2012','01/01/2013','01/01/2014','01/01/2015','01/01/2016','01/01/2017','01/01/2018','01/01/2019',
         '01/01/2020','01/01/2021','01/01/2022']

x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

reactors = [0,1,1,2,5,7,11,13,15,24,29,37,44,53,57,60,70,78,87,104,117,135,158,171,184,199,217,230,254,265,285,313,348,374,393,409,421,417,416,416,426,430,437,439,437,435,435,440,442,446,443,439,443,438,442,441,438,442,434,434,430,437,440,444,443,446,441,437,434]

mwe = [0.0,5.0,5.0,54.0,134.5,243.5,436.5,681.5,851.5,1685.5,2047.5,3152.0,4642.0,5827.0,7620.0,8268.0,11217.0,14924.0,20735.0,29978.0,38540.0,54052.0,70351.0,79218.0,93225.0,105706.0,120086.0,130442.0,150493.0,160353.0,178541.0,205180.0,243512.0,269462.0,292057.0,313822.0,326826.0,331889.0,335672.0,336086.0,344943.0,350075.0,355279.0,358029.0,359114.0,357170.0,357906.0,361055.0,363280.0,371231.0,372877.0,373016.0,377854.0,378167.0,380999.0,380591.0,378078.0,380928.0,372694.0,374289.0,371334.0,378394.0,383972.0,389504.0,389044.0,395522.0,392308.0,389141.0,387369.0]

fig, ax = plt.subplots()

ax_2 = ax.twinx()

#ax.plot(x, reactors, label='Reactors', color='black', linestyle='solid')
#ax_2.plot(x, mwe, label='MWe', color='black', linestyle='dashed')
#labelLines(plt.gca().get_lines())
ax.scatter(x, reactors, s=7, label='Operational Reactors', c='red', marker='.')
ax_2.scatter(x, mwe,    s=7, label='Nameplate Capacity [MWe]', c='blue', marker='^')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
ax.xaxis.set_major_locator(mdates.DayLocator())
ax_2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
ax_2.xaxis.set_major_locator(mdates.DayLocator())

#ax.scatter(fluence, dpa_err, s=16, label='DPA Difference')
ax.set_xscale('linear')
ax.set_yscale('linear')
#ax.legend(bbox_to_anchor=(1.02,1.03), loc='upper left')
ax.set_xlabel("Date")
ax.set_ylabel("# Reactors")
ax_2.set_ylabel("MWe")
ax_2.set_yscale('linear')
#xticks = [1e-16, 1e-12, 1e-8, 1e-4, 1e0]
#xticks = [1e-10, 1e-8, 1e-6, 1e-4, 1e-2, 1e0]
#ax.set_xticks(xticks)
#yticks = [1e-15, 1e-10, 1e-5, 1e0, 1e3]
#yticks = [1e-4, 1e-3, 1e-2, 1e-1, 1e0]
#ax.set_yticks(yticks)
#plt.xlim([1e-16, 1e0])
#plt.xlim([1e-10, 1e0])
#plt.ylim([1e-15, 1e3])
#plt.ylim([1e-4, 2e0])
#plt.locator_params(axis='x', numticks=10)
plt.subplots_adjust(right=0.76)
plt.show()

#fig.savefig("0037_cram_dmi.pdf", format='PDF', bbox_inches='tight')
fig.autofmt_xdate()
fig.savefig("npp_history.pdf", format='PDF', bbox_inches='tight')
