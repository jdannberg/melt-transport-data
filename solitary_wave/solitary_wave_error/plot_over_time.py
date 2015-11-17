#!/usr/bin/python

# this script can be used to generate plots from csv files

import numpy as np
import matplotlib.pyplot as plt

prop={'size':12}
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = '\usepackage{relsize}'
plt.rc('font', family='sanserif')
nplots=3

resolution=[3,10,50]
CFL=['1']
res_label=['1.25m','1.25m, CFL=10','1.25m, CFL=0.5']
CFL_label=['1','0.5','0.25','0.125']

data = []
for j in range(0,len(resolution)):
	for i in range(0,len(CFL)):
		data.append(np.genfromtxt('log-'+ str(resolution[j]) + '.txt.csv',delimiter=',', dtype = float, skip_footer=1))

time=[]
porosity=[]
pressure=[]
speed=[]
phase_shift=[]

# data to plot
for i in range(0,len(resolution)):
	time.append([row[0] for row in data[i]])
	porosity.append([row[1] for row in data[i]])
	pressure.append([row[2] for row in data[i]])
	speed.append([abs(row[3]) for row in data[i]])

# Four subplots, the axes array is 1-d
fig, ax = plt.subplots(nplots, sharex=True)

# define colors
colors=['LimeGreen','k','w','YellowGreen','SeaGreen','DarkGreen','Aqua','DeepSkyBlue','RoyalBlue','MidnightBlue','Salmon','r','FireBrick','Maroon','k','k','k','k']
linestyles = ['-','--', ':', '--', ':','-', '--', '', '','-', '-', '--', ':']

for j in range(0,len(resolution)):
	ax[0].plot(time[j],porosity[j],ls=linestyles[j],color=colors[j],label=res_label[j],lw=2.0)
	ax[0].set_ylim([0.01,0.5])
	ax[1].plot(time[j],pressure[j],ls=linestyles[j],color=colors[j],label=res_label[j],lw=2.0)
	ax[1].set_ylim([0.01,0.5])
	ax[2].plot(time[j],speed[j],ls=linestyles[j],color=colors[j],label=res_label[j],lw=2.0)
#	ax[2].set_ylim([0.001,0.1])

# ad labels, legend and use logarithmic scale
ax[2].set_xlabel('Time in years')
ax[0].set_ylabel('Porosity error')
ax[1].set_ylabel('Pressure error')
ax[2].set_ylabel('Phase speed error')

legend=range(0,nplots)
frame=range(0,nplots)

for i in range (0,nplots):
	ax[i].set_yscale('log')
legend = ax[0].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., labelspacing=0.)
legend.set_title('Resolution')
t = legend.get_title()
t.set_fontsize(10)  #set the font size

frame = legend.get_frame()
frame.set_facecolor('0.80')
# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize(10)
for label in legend.get_lines():
    label.set_linewidth(1.3)  # the legend line width

ax[0].set_title('Solitary wave benchmark: Relative errors')
fig.set_size_inches(10,5)
fig.savefig('solitary_wave_convergence.pdf', bbox_extra_artists=(legend,), bbox_inches='tight',dpi=200)

# plt.show()
