#!/usr/bin/python

# this script can be used to generate plots from csv files

import numpy as np
import matplotlib.pyplot as plt

nplots=4

file_name=[0.02,0.01,0.005,0.0025,0.00125]
resolution=[0.02,0.01,0.005,0.0025,0.00125]
CFL=['1']

data = []
for i in range(0,len(CFL)):
	for j in range(0,len(file_name)):
		data.append(np.genfromtxt('log-'+ str(file_name[j]) + '.txt.csv',delimiter=',', dtype = float))

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
fig, ax = plt.subplots(1,3)
fig.tight_layout(pad=2.0, w_pad=2.0)
plt.subplots_adjust(top=0.9, bottom=0.2)

# define colors
colors=['w','k','c','g','y','k','m']
linestyles = ['x', '--', ':', '-']
label=['','Error']

sr = 0
er = len(resolution)-1

ax[0].plot(resolution,porosity,linestyles[0]+colors[1], mew=1.5, ms=6)
ax[1].plot(resolution,pressure,linestyles[0]+colors[1], mew=1.5, ms=6)
ax[2].plot(resolution,speed,linestyles[0]+colors[1], mew=1.5, ms=6)

for j in range(0,3):
	ax[j].set_xlabel('Wave amplitude')
	ax[j].set_yscale('log')
	ax[j].set_xscale('log')
	ax[j].set_xlim(0.001,0.022)

# add labels, legend and use logarithmic scale
ax[0].set_ylim(0.01,0.3)
ax[1].set_ylim(0.01,0.5)
ax[2].set_ylim(5e-4,4e-2)

ax[0].set_ylabel('Porosity error')
ax[1].set_ylabel('Pressure error')
ax[2].set_ylabel('Phase speed error')

#ax[0].set_title('Error after t= 6 x 10^6  years')
fig.set_size_inches(10,3)

fig.savefig('porosity_error',dpi=200)

# plt.show()
