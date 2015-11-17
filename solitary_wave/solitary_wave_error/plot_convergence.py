#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import colors

figsize=(7,5)
prop={'size':12}
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = '\usepackage{relsize}'
plt.rc('font', family='sanserif')
figure=plt.figure(dpi=100,figsize=figsize)

# ndofs,u,p,p_f,p_c,phi,u_f
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

plt.loglog(resolution,porosity,color=colors.color(4), marker=colors.marker(1),label='$e_\phi$')
plt.loglog(resolution,pressure,color=colors.color(5), marker=colors.marker(1),label='$e_p$')
plt.loglog(resolution,speed,color=colors.color(6), marker=colors.marker(1),label='$e_c$')

plt.xlim([3, 0.25])
plt.ylim([4e-3,0.4])
plt.xlabel("Resolution in m")
plt.ylabel("Relative errors")
plt.grid(True, which='both')
 

plt.legend(loc = "center left",prop=prop)
plt.savefig('solitary_wave_error.pdf', #bbox_extra_artists=(legend,), 
            bbox_inches='tight',dpi=200)

