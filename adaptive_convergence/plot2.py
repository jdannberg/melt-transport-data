#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import colors

for adaptive_file in ['adaptive.dat', 'adaptive_pc.dat']:

    figsize=(8,5)
    prop={'size':12}
    plt.rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = '\usepackage{relsize}'
    plt.rc('font', family='sanserif')
    figure=plt.figure(dpi=100,figsize=figsize)

    # ndofs,u,p,p_f,p_c,phi,u_f
    data=np.genfromtxt(adaptive_file, usecols=(2,4,6,8,10,12,14), dtype = float)
    print data

    plt.loglog(data[:,0],data[:,1],color=colors.color(1), marker=colors.marker(1),label='$u$')
    plt.loglog(data[:,0],data[:,2],color=colors.color(2), marker=colors.marker(1),label='$p$')
    plt.loglog(data[:,0],data[:,3],color=colors.color(3), marker=colors.marker(1),label='$p_f$')
    plt.loglog(data[:,0],data[:,4],color=colors.color(4), marker=colors.marker(1),label='$p_c$')

    plt.loglog(data[:,0],data[:,5],color=colors.color(5), marker=colors.marker(1),label='$\phi$')
    plt.loglog(data[:,0],data[:,6],color=colors.color(6), marker=colors.marker(1),label='$u_f$')


    data=np.genfromtxt('global.dat', usecols=(2,4,6,8,10,12,14), dtype = float)
    print data

    plt.loglog(data[:,0],7e0*data[:,0]**(-1./2.),linestyle=':', color='black', label='linear')
    plt.loglog(data[:,0],7e1*data[:,0]**(-2./2.),linestyle='--', color='black', label='quadratic')
    plt.loglog(data[:,0],4e2*data[:,0]**(-3./2.),linestyle='-.', color='black', label='cubic')

    m=3
    plt.loglog(data[:,0],data[:,1],color=colors.color(1), linestyle="--",marker=colors.marker(m), label='(global ref.)')
#,label='$u$')
    plt.loglog(data[:,0],data[:,2],color=colors.color(2), linestyle="--",marker=colors.marker(m))#,label='$p$')
    plt.loglog(data[:,0],data[:,3],color=colors.color(3), linestyle="--",marker=colors.marker(m))#,label='$p_f$')
    plt.loglog(data[:,0],data[:,4],color=colors.color(4), linestyle="--",marker=colors.marker(m))#,label='$p_c$ global')
    plt.loglog(data[:,0],data[:,5],color=colors.color(5), linestyle="--", marker=colors.marker(m))#,label='$\phi$ global')
    plt.loglog(data[:,0],data[:,6],color=colors.color(6), linestyle="--",marker=colors.marker(m))#,label='$u_f$')

    #plt.loglog(data[:,0],3e1*data[:,0]**(-1./2.),linestyle=':', color='black', label='linear')
    #plt.loglog(data[:,0],1e3*data[:,0]**(-2./2.),linestyle='--', color='black', label='quadratic')
    #plt.loglog(data[:,0],1.5e4*data[:,0]**(-3./2.),linestyle='-.', color='black', label='cubic')


    plt.xlim([1.5e3, 2e5])
    plt.ylim([1.4e-6, 5e-1])
    plt.xlabel("\# DoFs")
    plt.ylabel("L2 errors")


    plt.legend(loc = "lower center",prop=prop, ncol=5)# bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           #mode="expand", borderaxespad=0.)

    filename = adaptive_file.replace('.','_')+'.pdf'
    print "writing "+filename
    plt.savefig(filename, #bbox_extra_artists=(legend,), 
                bbox_inches='tight',dpi=200)

    #plt.show()

