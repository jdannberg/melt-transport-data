#!/usr/bin/python

# this script can be used to generate plots from csv files

import numpy as np
import matplotlib.pyplot as plt

nplots=4

file_name=[2,3,4,5]
resolution=[2.5,1.25,0.63,0.31]
CFL=['1']

data = []
for i in range(0,len(CFL)):
	for j in range(0,len(file_name)):
		data.append(np.genfromtxt('log-'+ str(file_name[j]) + '.txt.last-step.csv',delimiter=',', dtype = float))

porosity=[]
pressure=[]
speed=[]
phase_shift=[]

# data to plot
for j in range(0,len(resolution)):
	for i in range(0,len(CFL)):
		porosity.append(abs(data[j*len(CFL)+i][0]))
		pressure.append(abs(data[j*len(CFL)+i][1]))
		speed.append(abs(data[j*len(CFL)+i][2]))
		phase_shift.append(abs(data[j*len(CFL)+i][3]))

print porosity

# Six subplots, the axes array is 1-d
fig, ax = plt.subplots(1)
fig.tight_layout(pad=2.0, w_pad=2.0, h_pad=20.0)
plt.subplots_adjust(top=0.9, bottom=0.2, left=0.2)

# define colors
colors=['w','k','c','g','y','k','m']
linestyles = ['x', '--', ':', '-']
label=['','Error']

sr = 0
er = len(resolution)-1

ax.plot(resolution,porosity,linestyles[0]+colors[1], mew=1.5, ms=6)
ax.plot(resolution,pressure,linestyles[0]+colors[1], mew=1.5, ms=6)
ax.plot(resolution,speed,linestyles[0]+colors[1], mew=1.5, ms=6)

# add labels, legend and use logarithmic scale
ax.set_xlabel('Resolution in m')
ax.set_ylabel('Error')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(3, 0.25)
ax.set_ylim(4e-3,0.4)

#ax[0].set_title('Error after t= 6 x 10^6  years')
fig.set_size_inches(3.5,3)

fig.savefig('solitary_wave_error',dpi=200)

# plt.show()
