# Gnuplot script

set title "Root mean square velocity"
set xlabel "Time in years"
set ylabel "Velocity in m/yr"
set key samplen 0.0 at 8.7e8,0.007
set xrange [0:9e8]

set terminal postscript color portrait dashed enhanced 'Arial'
set output 'global_comparison.eps'
set size 1.0,0.6

plot    1/0 with dots linetype 1 linecolor rgb "#4169E1" lw 5 title "no melt migration", \
	1/0 with dots linetype 1 linecolor rgb "#AA0000" lw 5 title "with melt migration, {/Symbol D}{/Symbol r}=200 kg/m^3", \
        "no_melt/statistics" using 2:12 with dots linecolor rgb "#4169E1" lw 2 notitle, \
	"density_200/statistics" using 2:21 with dots linecolor rgb "#AA0000" lw 2 notitle


