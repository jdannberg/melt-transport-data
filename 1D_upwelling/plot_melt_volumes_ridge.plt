# Gnuplot script

f(value, left, right) = (value < left || value > right ? 1/0 : value)


set ylabel "Melt flux in m/s^2"
set key samplen 0.0
set key Left left reverse 
set xrange [70000:0]
set yrange [0:0.016]
set datafile separator ","
unset xtics

set terminal postscript color portrait dashed enhanced 'Arial' size 18cm,15cm
set output 'melt_volumes_ridge.eps'

set multiplot layout 2,1 title "Melt volume"

#set label "deep melting" at 70000,3.2e9 rotate by 73
#set label "shallow melting" at 100000,2.5e9 rotate by 70

#set arrow from 1.0717e+05,6.42700584e+09 to 1.0717e+05,7.15867231e+09 nohead # 11.4%
#set arrow from 1.1954e+05,5.60433522e+09 to 1.1954e+05,6.09381663e+09 nohead # 4.9%

set lmargin 10
set tmargin at screen 0.92; set bmargin at screen 0.4

plot 1/0 with dots linecolor rgb "#4169E1" lw 7 title "incompressible", \
	1/0 with dots linecolor rgb "#AA0000" lw 7 title "fluid density gradient", \
	1/0 with dots linecolor rgb "#FF4500" lw 7 title "solid density gradient" ,\
	1/0 with dots linecolor rgb "orange" lw 7 title "bulk density" ,\
        "ridge_incompressible.csv" using (100000-$26):($11*$5) with lines linecolor rgb "#4169E1" lw 2 lt 1 notitle, \
	"ridge_fluid_density.csv" using (100000-$26):($11*$5) with lines linecolor rgb "#AA0000" lw 2 lt 1 notitle, \
	"ridge_solid_density.csv" using (100000-$26):($11*$5) with lines linecolor rgb "#FF4500" lw 2 lt 1 notitle, \
	"ridge_bulk_density.csv" using (100000-$26):($11*$5) with lines linecolor rgb "orange" lw 2 lt 1 notitle

set xlabel "Depth in m"
set yrange [1.0:1.29]
set datafile missing "0"
set style fill border
set xtics out
#set ytics (1,1.025,1.05,1.075)
set ylabel "Relative melt flux"

set tmargin at screen 0.4; set bmargin at screen 0.15

plot 	"ridge.txt" using (f(100000-$26,0,60000)):(($69*$63)/($40*$34)):1 with filledcu linecolor rgb "#FF4500" lw 2 lt 1 fs pattern 7 title "solid density gradient", \
	"ridge.txt" using (f(100000-$26,0,60000)):(($69*$63)/($40*$34)) with lines linecolor rgb "#FF4500" lw 3 lt 1 notitle, \
	"ridge.txt" using (f(100000-$26,0,60000)):(($11*$5)/($40*$34)):1 with filledcu linecolor rgb "#AA0000" lw 2 lt 1 fs pattern 6 title "fluid density gradient", \
	"ridge.txt" using (f(100000-$26,0,60000)):(($11*$5)/($40*$34)) with lines linecolor rgb "#AA0000" lw 3 lt 1 notitle, \
	"ridge.txt" using (f(100000-$26,0,60000)):(($98*$92)/($40*$34)):1 with filledcu linecolor rgb "orange" lw 2 lt 1 fs pattern 2 title "bulk density", \
	"ridge.txt" using (f(100000-$26,0,60000)):(($98*$92)/($40*$34)):1 with lines linecolor rgb "orange" lw 3 lt 1 notitle





unset multiplot
