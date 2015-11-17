# Gnuplot script

set title "Depletion depth-average"
set xlabel "Time in years"
set ylabel "Depth in m"
unset key
#set key samplen 0.0
#set key at 5.8e8,0.005 box 
set xrange [0:9e8]
set yrange [2.9e6:0]
set cbrange [-0.08:0.12]
#set palette rgb 33,13,10
set xtics out
set ytics out
set pm3d

set terminal postscript color portrait dashed enhanced 'Arial'
set output 'global_depth_average.eps'

set view map
set size 2.0,0.4
set size ratio .15
set label "Depletion" at screen 1.754,0.3
set label "Enrichment" at screen 1.754,0.1

splot "density_200/depth_average.gnuplot" using 2:1:5 with pm3d
