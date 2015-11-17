#!/usr/bin/python

# this script can be used to generate plots from csv files

import numpy as np
import matplotlib.pyplot as plt
import csv as csv

nplots=2

amplitude=[0.02,0.01,0.005,0.0025,'analytical']
label=['Amplitude 0.02','Amplitude 0.01','Amplitude 0.005','Amplitude 0.0025','analytical']

data = []
for i in range(0,len(amplitude)):
	data.append(np.genfromtxt('amplitude-' + str(amplitude[i]) + '.csv',delimiter=',', dtype = float, names = True))

distance=[]
porosity=[]
pressure=[]

# data to plot
for i in range(0,len(amplitude)):
	distance.append(data[i]['arc_length'])
	porosity.append(data[i]['Result'])
	pressure.append(data[i]['p_c'])


# Two subplots, the axes array is 1-d
fig, ax = plt.subplots(1,nplots)
fig.set_size_inches(12,5)

# define colors
colors=['YellowGreen','LimeGreen','SeaGreen','DarkGreen','k']
linestyles = ['', '--', ':', '-']

for i in range(0,len(amplitude)):
	ax[0].plot(distance[i],porosity[i],colors[i],label=str(label[i]),lw=0.7)
	ax[0].set_ylim([0.000,0.0105])
	ax[1].plot(distance[i],pressure[i],colors[i],label=str(label[i]),lw=0.7)


# add labels and legend
ax[0].set_xlabel('Distance in m')
ax[1].set_xlabel('Distance in m')
ax[0].set_ylabel('Porosity')
ax[1].set_ylabel('Compaction pressure [1e5 Pa]')

ax[1].yaxis.get_major_formatter().set_powerlimits((0, 1))

legend=range(0,nplots)
frame=range(0,nplots)

legend = ax[1].legend(loc=1, borderaxespad=0., labelspacing=0.)

frame = legend.get_frame()
frame.set_facecolor('1.0')
# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize(10)
for label in legend.get_lines():
    label.set_linewidth(1.3)  # the legend line width

ax[0].set_title('Solitary wave benchmark: Wave shape')

fig.savefig('solitary_wave_shape', bbox_extra_artists=(legend,), bbox_inches='tight',dpi=200)

# plt.show()
