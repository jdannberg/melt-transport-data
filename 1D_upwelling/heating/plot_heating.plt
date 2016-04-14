# Gnuplot script

f(value, left, right) = (value < left || value > right ? 1/0 : value)


set ylabel "Total heating rate in W"
set key samplen 0.0
set key bottom Left left reverse 
set xrange [60000:185000]
#set yrange [-1e4:1e4]
set datafile missing "0.00000000e+00"
set xlabel "Time in years"
set format y "%.0g"

set terminal postscript color portrait dashed enhanced 'Arial' size 18cm,15cm
set output 'heating.eps'

set multiplot layout 2,1 #"Heating rate"

#set label "deep melting" at 70000,3.2e9 rotate by 73
#set label "shallow melting" at 100000,2.5e9 rotate by 70

set lmargin 10
set tmargin at screen 0.92; set bmargin at screen 0.5

plot 1/0 with dots linecolor rgb "#00008B" lw 7 title "adiabatic heating without melt", \
	1/0 with dots linecolor rgb "orange" lw 7 title "latent heat", \
	1/0 with dots linecolor rgb "#AA0000" lw 7 title "dissipation heating without melt" ,\
	1/0 with dots linecolor rgb "#4169E1" lw 7 title "adiabatic heating with melt" ,\
	1/0 with dots linecolor rgb "#FF4500" lw 7 title "dissipation heating with melt" ,\
	"heating" using ($2):($28+$34) with dots linecolor rgb "#4169E1" lw 2 lt 1 notitle, \
        "heating" using 2:28 with dots linecolor rgb "#00008B" lw 2 lt 1 notitle, \
	"heating" using 2:30 with lines linecolor rgb "orange" lw 2 lt 1 notitle, \
	"heating" using 2:32 with dots linecolor rgb "#AA0000" lw 2 lt 1 notitle, \
	"heating" using 2:($32+$36) with dots linecolor rgb "#FF4500" lw 2 lt 1 notitle



set xlabel "y in m"
set yrange [-280:280]
set xrange [0:300000]
set style fill border
set ylabel "Excess temperature in K"
set datafile separator ","
set format y "%.0f"

set tmargin at screen 0.37; set bmargin at screen 0.12

plot "heating_profile.csv" using 31:18 with lines linecolor rgb "#FF4500" lw 2 lt 1 notitle ,\
     "no_heating_profile.csv" using 31:18 with lines linecolor rgb "#AA0000" lw 2 lt 1 notitle ,\
     1/0 with dots linecolor rgb "#AA0000" lw 7 title "heating without melt" ,\
     1/0 with dots linecolor rgb "#FF4500" lw 7 title "heating with melt"



unset multiplot
