# Gnuplot script

set title "Density relations"
set ylabel "Depth [m]"
set xlabel "Density [kg/m^3]"
set yrange [300000:0]
set key bmargin
set datafile separator ","

set terminal postscript color portrait dashed enhanced 'Arial'
set output 'density_profiles.eps'
set size 0.9,0.7

plot "density_incompressible.csv" using 13:26 with lines linetype 1 linecolor rgb "#4169E1" lw 2 title "Constant solid density 3400 kg/m^3 (incompressible)", \
     "density_incompressible.csv" using 19:26 with lines linetype 2 linecolor rgb "dark-blue" lw 2 title "Constant melt density 3000 kg/m^3 (incompressible)", \
     "density_compressible.csv" using 13:26 with lines linetype 1 linecolor rgb "#FF4500" lw 2 title "Pressure-dependent solid density (compressible)", \
     "density_compressible.csv" using 19:26 with lines linetype 2 linecolor rgb "#AA0000" lw 2 title "Pressure-dependent melt density (compressible)"

#replot
