#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import colors

for part in [1,2]:#,'cont3']:
    figsize=(7,4.5)
    prop={'size':11}
    plt.rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = '\usepackage{relsize}'
    plt.rc('font', family='sanserif')
    figure=plt.figure(dpi=100,figsize=figsize)

    # ndofs,u,p,p_f,p_c,phi,u_f
    data=np.genfromtxt('cont.dat', usecols=(2,4,6,8,10,12,14), dtype = float)
    print data

    if part==1:
        plt.loglog(data[:,0],data[:,6],color=colors.color(6), marker=colors.marker(1),label='$u_f$ ($k=2$)')
        plt.loglog(data[:,0],data[:,1],color=colors.color(1), marker=colors.marker(1),label='$u$ ($k=2$)')
        plt.loglog(data[:,0],data[:,5],color=colors.color(5), marker=colors.marker(1),label='$\phi$ ($k=2$)')
    else:
        plt.loglog(data[:,0],data[:,2],color=colors.color(2), marker=colors.marker(1),label='$p$ ($k=1$)')
        plt.loglog(data[:,0],data[:,4],color=colors.color(4), marker=colors.marker(1),label='$p_c$ ($k=1$)')
        plt.loglog(data[:,0],data[:,3],color=colors.color(3), marker=colors.marker(1),label='$p_f$ ($k=1$)')

    slopedata=[min(data[:,0]), max(data[:,0])]

    # ndofs,u,p,p_f,p_c,phi,u_f
    data=np.genfromtxt('cont3.dat', usecols=(2,4,6,8,10,12,14), dtype = float)
    print data

    m=3
    if part==1:
        plt.loglog(data[:,0],data[:,6],color=colors.color(6), linestyle='--', marker=colors.marker(3),label='$u_f$ ($k=3$)')
        plt.loglog(data[:,0],data[:,1],color=colors.color(1), linestyle='--', marker=colors.marker(3),label='$u$ ($k=3$)')
        plt.loglog(data[:,0],data[:,5],color=colors.color(5), linestyle='--', marker=colors.marker(3),label='$\phi$ ($k=3$)')
    else:
        plt.loglog(data[:,0],data[:,2],color=colors.color(2), marker=colors.marker(3),label='$p$ ($k=2$)')
        plt.loglog(data[:,0],data[:,4],color=colors.color(4), marker=colors.marker(3),label='$p_c$ ($k=2$)')
        plt.loglog(data[:,0],data[:,3],color=colors.color(3), marker=colors.marker(3),label='$p_f$ ($k=2$)')


    slopedata=np.array([min(min(data[:,0]),slopedata[0]), max(max(data[:,0]),slopedata[1])])

    print slopedata

    
    #if file=='cont':
    if part==1:
        plt.loglog(slopedata,slopedata**(-1./2.),linestyle=':', color='black', label='linear')
    plt.loglog(slopedata,slopedata**(-2./2.),linestyle='--', color='black', label='quadratic')
    plt.loglog(slopedata,slopedata**(-3./2.),linestyle='-.', color='black', label='cubic')
    if part==1:
        plt.loglog(slopedata,(0.9*slopedata)**(-4./2.),linestyle='-', color='black', label='quartic')


    if part==1:
        plt.xlim([4e3, 6e5])
        plt.ylim([5e-15, 1e-1])
        plt.legend(loc = "lower center",prop=prop, ncol=4)# bbox_to_anchor=(0., 1.02, 1., .102), loc=3
    else:
        plt.xlim([4e3, 6e5])
        plt.ylim([5e-11, 2e-3])
        plt.legend(loc = "lower center",prop=prop, ncol=3)# bbox_to_anchor=(0., 1.02, 1., .102), loc=3,

    plt.xlabel("\# DoFs")
    plt.ylabel("L2 errors")


    #plt.legend(loc = "lower left",prop=prop, ncols=5)
           #mode="expand", borderaxespad=0.)


    plt.savefig('compressible_error'+str(part)+'.pdf',#bbox_extra_artists=(legend,), 
                bbox_inches='tight',dpi=200)

plt.show()

