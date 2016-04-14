# Gnuplot script

f(value, left, right) = (value < left || value > right ? 1/0 : value)


set ylabel "Depth in m"
set xlabel "{/Symbol \321}p_f in Pa/m"
set key samplen 0.0 opaque box height 0.5 width 0.5
unset key 
set xrange [-34990:-27510]
set yrange [150000:0.0]
set datafile separator ","
set datafile missing "nan"
set xtics (-3.5e4, -3.25e4, -3e4, -2.75e4)

set terminal postscript color portrait dashed enhanced 'Arial' size 23cm,15cm
set output 'pressure_gradients.eps'

set multiplot layout 1,3 #title "Model setup"

set lmargin at screen 0.15; set rmargin at screen 0.425
set bmargin at screen 0.15

set title "Mid-ocean ridge"
plot	"ridge_pressure_gradient_incompressible.csv" using (-$13*10):(100000-$29) with lines linecolor rgb "#FF4500" lw 2 lt 1 title "solid density", \
	"ridge_pressure_gradient_incompressible.csv" using (-$20*10):(100000-$29) with lines linecolor rgb "#AA0000" lw 2 lt 1  title "fluid density", \
	"ridge_pressure_gradient_bulk_incompressible.csv" using (-$1*10):(100000-$29) with lines linecolor rgb "orange" lw 3 lt 1  title "bulk density", \
 	"ridge_pressure_gradient_incompressible.csv" using 26:(100000-$29) with lines linecolor rgb "#10000000" lw 2 lt 1 title "pressure gradient", \
	

set xrange [-36000:-28500]
set lmargin at screen 0.425; set rmargin at screen 0.7
set bmargin at screen 0.15
unset ylabel
set ytics format " " 
set key Left reverse at screen 0.455, 0.36
set border 13

set title "Rising mantle plume"
plot 	"plume_pressure_gradient_incompressible.csv" using 26:(300000-$29) with lines linecolor rgb "black" lw 2 lt 2 title "pressure gradient", \
	"plume_pressure_gradient_incompressible.csv" using (-$13*10):(300000-$29) with lines linecolor rgb "#FF4500" lw 2 lt 2 title "solid density", \
	"plume_pressure_gradient_incompressible.csv" using (-$20*10):(300000-$29) with lines linecolor rgb "#AA0000" lw 2 lt 2  title "fluid density", \
	"plume_pressure_gradient_bulk_incompressible.csv" using (-$1*10):(300000-$29) with lines linecolor rgb "orange" lw 2 lt 2  title "bulk density"

set xlabel "Melt fraction"
set style fill pattern 6 border
set xtics (0.2, 0.4, 0.6, 0.8)
set xrange [0:0.75]
set key at screen 0.915, 0.3 
set border

set lmargin at screen 0.75; set rmargin at screen 0.95

set title "Porosity profiles"
plot    "plume_pressure_gradient_incompressible.csv" using 11:(300000-$29) with lines linecolor rgb "black" lw 2 lt 2 title "plume", \
	"ridge_pressure_gradient_incompressible.csv" using 11:(100000-$29) with lines linecolor rgb "black" lw 2 lt 1 title "ridge"

unset multiplot
