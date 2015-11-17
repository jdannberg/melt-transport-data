# Gnuplot script

set title "Total volume of porosity"
set xlabel "Time in years"
set ylabel "Integrated porosity area in m^2"
set key samplen 0.0
set key at 6.8e8,4e11 Left reverse
set xrange [0:9e8]
set yrange [5e8:5e11]
set logscale y
unset x2tics

set terminal postscript color portrait dashed enhanced 'Arial'
set output 'global_melt.eps'
set size 1.0,0.6

plot    1/0 with dots linetype 1 linecolor rgb "#4169E1" lw 5 title "no melt migration", \
	1/0 with dots linetype 1 linecolor rgb "#FA8072" lw 5 title "with melt migration, {/Symbol D}{/Symbol r}=0 kg/m^3", \
	1/0 with dots linetype 1 linecolor rgb "#DC143C" lw 5 title "with melt migration, {/Symbol D}{/Symbol r}=100 kg/m^3", \
	1/0 with dots linetype 1 linecolor rgb "#AA0000" lw 5 title "with melt migration, {/Symbol D}{/Symbol r}=200 kg/m^3", \
        "density_200/statistics" using 2:17 with dots linecolor rgb "#AA0000" lw 2 notitle, \
        "density_100/statistics" using 2:17 with dots linecolor rgb "#DC143C" lw 2 notitle, \
        "no_melt/statistics" using 2:19 with dots linecolor rgb "#4169E1" lw 2 notitle, \
        "density_0/statistics" using 2:17 with dots linecolor rgb "#FA8072" lw 2 notitle

