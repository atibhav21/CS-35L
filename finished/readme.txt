scp srt.tgz atibhav@lnxsrv.seas.ucla.edu:~/35L/lab8
to copy the .tgz file to the SEASNet server

tar -xvzf srt.tgz
To extract the contents of srt.tgz

gimp baseline.ppm 
To view the image before making a change

To see the time taken for files without modification, I ran the command make clean check > unmodified-log.txt

Before modifying main.c:

real	0m48.237s
user	0m48.241s
sys		0m0.001s

After modifying main.c

ran
make clean check > make-log.txt

real	0m48.319s
user	0m48.322s
sys	0m0.001s

real	0m24.502s
user	0m48.787s
sys	0m0.004s

real	0m12.441s
user	0m49.206s
sys	0m0.003s

real	0m6.813s
user	0m52.098s
sys	0m0.002s

To check that 1-test.ppm and baseline.ppm were identical, I ran the command
diff -u baseline.ppm 1-test.ppm > diffImage.txt

diffImage.txt was an empty file as we wanted.

As the above data shows, the time required as the number of thread increases, decreases.
As compared to the initial compilation, it takes almost the same amount of time when only 1 thread is being used.


