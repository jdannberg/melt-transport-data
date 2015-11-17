# Gnuplot script

set title "Melt volume"
set xlabel "Time in years"
set ylabel "Melt area in m^2"
set key samplen 0.0
set key Left reverse at 90000,6.9e9 #box 
set xrange [0:140000]
set yrange [0:7.2e9]

set terminal postscript color portrait dashed enhanced 'Arial'
set output 'melt_volumes.eps'
set size 1.0,0.6

set label "deep melting" at 70000,3.2e9 rotate by 73
set label "shallow melting" at 100000,2.5e9 rotate by 70

#set arrow from 1.0717e+05,6.42700584e+09 to 1.0717e+05,7.15867231e+09 nohead # 11.4%
#set arrow from 1.1954e+05,5.60433522e+09 to 1.1954e+05,6.09381663e+09 nohead # 4.9%

plot 1/0 with dots linecolor rgb "#4169E1" lw 7 title "incompressible", \
	1/0 with dots linecolor rgb "#AA0000" lw 7 title "pressure-dependent density", \
	1/0 with dots linecolor rgb "#FF4500" lw 7 title "compressible" ,\
        "incompressible/statistics" using 2:17 with dots linecolor rgb "#4169E1" lw 2 notitle, \
	"pressure_dependent/statistics" using 2:17 with dots linecolor rgb "#AA0000" lw 2 notitle, \
	"compressible/statistics" using 2:17 with dots linecolor rgb "#FF4500" lw 2 notitle,\
        "hydrous_incompressible/statistics" using 2:17 with dots linecolor rgb "#4169E1" lw 2 notitle, \
	"hydrous_pressure_dependent/statistics" using 2:17 with dots linecolor rgb "#AA0000" lw 2 notitle, \
	"hydrous_compressible/statistics" using 2:17 with dots linecolor rgb "#FF4500" lw 2 notitle
#replot
