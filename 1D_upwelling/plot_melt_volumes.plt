# Gnuplot script

f(value, left, right) = (value < left || value > right ? 1/0 : value)


set ylabel "Melt area in m^2"
set key samplen 0.0
set key Left left reverse 
set xrange [60000:185000]
set yrange [0:6e7]
set datafile separator ","
unset xtics

set terminal postscript color portrait dashed enhanced 'Arial' size 18cm,15cm
set output 'melt_volumes.eps'

set multiplot layout 2,1 title "Melt volume"

#set label "deep melting" at 70000,3.2e9 rotate by 73
#set label "shallow melting" at 100000,2.5e9 rotate by 70

#set arrow from 1.0717e+05,6.42700584e+09 to 1.0717e+05,7.15867231e+09 nohead # 11.4%
#set arrow from 1.1954e+05,5.60433522e+09 to 1.1954e+05,6.09381663e+09 nohead # 4.9%

set lmargin 10
set tmargin at screen 0.92; set bmargin at screen 0.4

plot 1/0 with dots linecolor rgb "#4169E1" lw 7 title "incompressible", \
	1/0 with dots linecolor rgb "#AA0000" lw 7 title "fluid density", \
	1/0 with dots linecolor rgb "#FF4500" lw 7 title "solid density" ,\
	1/0 with dots linecolor rgb "orange" lw 7 title "bulk density" ,\
        "plume_incompressible.csv" using 27:12 with lines linecolor rgb "#4169E1" lw 2 lt 1 notitle, \
	"plume_fluid_density.csv" using 27:12 with lines linecolor rgb "#AA0000" lw 2 lt 1 notitle, \
	"plume_solid_density.csv" using 27:12 with lines linecolor rgb "#FF4500" lw 2 lt 1 notitle, \
	"plume_bulk_density.csv" using 27:12 with lines linecolor rgb "orange" lw 2 lt 1 notitle

set xlabel "Time in years"
set yrange [1.0:1.29]
set datafile missing "0"
set style fill border
set xtics out
set ylabel "Relative melt area"

set tmargin at screen 0.4; set bmargin at screen 0.15

plot 	"final.txt" using (f($27,90000,200000)):($12/$42):1 with filledcu linecolor rgb "#AA0000" lw 2 lt 1 fs pattern 7 title "fluid density", \
	"final.txt" using ($27):($12/$42):1 with lines linecolor rgb "#AA0000" lw 3 lt 1 notitle, \
	"final.txt" using (f($117,90000,200000)):($102/$42):1 with filledcu linecolor rgb "orange" lw 2 lt 1 fs pattern 2 title "bulk density", \
	"final.txt" using ($117):($102/$42):1 with lines linecolor rgb "orange" lw 3 lt 1 notitle, \
	"final.txt" using (f($87,90000,200000)):($72/$42):1 with filledcu linecolor rgb "#FF4500" lw 2 lt 1 fs pattern 6 title "solid density", \
	"final.txt" using ($87):($72/$42):1 with lines linecolor rgb "#FF4500" lw 3 lt 1 notitle



unset multiplot
