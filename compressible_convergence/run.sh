make

looper "mpirun -n 4 ./aspect" loop.prm | tee output.txt
grep Error output.txt >cont.dat

looper "mpirun -n 4 ./aspect" loop3.prm | tee output.txt
grep Error output.txt >cont3.dat

python plot3.py
