#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import colors

for file in ['cont','cont3']:
    figsize=(7,5)
    prop={'size':12}
    plt.rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = '\usepackage{relsize}'
    plt.rc('font', family='sanserif')
    figure=plt.figure(dpi=100,figsize=figsize)

    # ndofs,u,p,p_f,p_c,phi,u_f
    data=np.genfromtxt(file+'.dat', usecols=(2,4,6,8,10,12,14), dtype = float)
    print data

    plt.loglog(data[:,0],data[:,1],color=colors.color(1), marker=colors.marker(1),label='$u$')
    plt.loglog(data[:,0],data[:,2],color=colors.color(2), marker=colors.marker(1),label='$p$')
    plt.loglog(data[:,0],data[:,3],color=colors.color(3), marker=colors.marker(1),label='$p_f$')
    plt.loglog(data[:,0],data[:,4],color=colors.color(4), marker=colors.marker(1),label='$p_c$')
    plt.loglog(data[:,0],data[:,5],color=colors.color(5), marker=colors.marker(1),label='$\phi$')
    plt.loglog(data[:,0],data[:,6],color=colors.color(6), marker=colors.marker(1),label='$u_f$')

    plt.loglog(data[:,0],data[:,0]**(-1./2.),linestyle=':', color='black', label='linear')
    plt.loglog(data[:,0],data[:,0]**(-2./2.),linestyle='--', color='black', label='quadratic')
    plt.loglog(data[:,0],data[:,0]**(-3./2.),linestyle='-.', color='black', label='cubic')


    plt.xlim([5e1, 8e5])
    plt.ylim([5e-11, 5e-1])
    plt.xlabel("\# DoFs")
    plt.ylabel("L2 errors")


    plt.legend(loc = "lower left",prop=prop)
    plt.savefig(file+'_error.pdf', #bbox_extra_artists=(legend,), 
                bbox_inches='tight',dpi=200)

plt.show()

