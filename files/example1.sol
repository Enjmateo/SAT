c ---- [ banner ] ------------------------------------------------------------
c
c Kissat SAT Solver
c 
c Copyright (c) 2021-2022 Armin Biere University of Freiburg
c Copyright (c) 2019-2021 Armin Biere Johannes Kepler University Linz
c 
c Version 3.0.0 unknown
c gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 -W -Wall -O3 -DNDEBUG
c Mon Jan 16 20:07:14 CET 2023 Linux DESKTOP-6PBNNSQ 4.4.0-22000-Microsoft x86_64
c
c ---- [ parsing ] -----------------------------------------------------------
c
c opened and reading DIMACS file:
c
c   ./files/example1.cnf
c
c parsed 'p cnf 21 53' header
c closing input after reading 497 bytes
c finished parsing after 0.00 seconds
c
c ---- [ solving ] -----------------------------------------------------------
c
c  seconds switched rate      trail variables
c         MB reductions conflicts glue  remaining
c          level restarts redundant irredundant
c
c *  0.00  1 0 0 0  0 0   0   0 0% 0  3  5 24%
c {  0.00  1 0 0 0  0 0   0   0 0% 0  3  5 24%
c }  0.00  1 0 0 0  0 0   0   0 0% 0  3  5 24%
c 1  0.00  1 0 0 0  0 0   0   0 0% 0  3  5 24%
c
c ---- [ result ] ------------------------------------------------------------
c
s SATISFIABLE
v -1 2 3 4 5 -6 7 -8 -9 -10 -11 -12 13 -14 15 -16 17 -18 19 -20 21 0
c
c ---- [ profiling ] ---------------------------------------------------------
c
c           0.00    0.00 %  search
c           0.00    0.00 %  simplify
c =============================================
c           0.00    0.00 %  total
c
c ---- [ statistics ] --------------------------------------------------------
c
c conflicts:                                0                0.00 per second
c decisions:                                5                0.00 per conflict
c propagations:                            17                0    per second
c
c ---- [ resources ] ---------------------------------------------------------
c
c maximum-resident-set-size:          1052672 bytes          1 MB
c process-time:                             0s               0.00 seconds
c
c ---- [ shutting down ] -----------------------------------------------------
c
c exit 10
