from  students_lib import *


def my_problem(outputfile): 
    
    n=10
    k=5
        
    m = model()
    m.name = "SUM of x_i >= " + str(k) + " with additionnal constraints"

    x = m.define_new_list(n) 
    y = encode_sum_at_least(m,x,k)

    c = always_false(x[1])
    m.cls.append(c)
    c = always_false(x[2])
    m.cls.append(c)
    c = always_false(x[0])
    m.cls.append(c)
    c = always_false(x[5])
    m.cls.append(c)
    write_cnf_file(m.cls,m.vars,outputfile)
    return m,x,y


outputfile='./files/example2.cnf'
m,x,y = my_problem(outputfile)

if not RUNSOLVER:
    exit()
else :
    if VERBOSITY : 
        stop = timeit.default_timer()
        print('d GENERATIONTIME', "%.2f" % (stop - start))
        print('c Solving the instance ..')
    outputsolutionfile = outputfile[:len(outputfile) - 4]
    outputsolutionfile=outputsolutionfile+'.sol'
    with open(outputsolutionfile, "w+") as f:
        subprocess.run([SOLVERPATH , outputfile  ] , stdout=f)

sol = []

with open(outputsolutionfile, 'r') as fp:
    for line in fp:
        if "UNSATISFIABLE" in line:
            print ('c The problem in UNSATISFIABLE')
            fp.close()
            exit()
        elif line[0]== 'v':
            #[ 1:] )
            sol +=  [int(x) for x in line.split()[1:] ]
fp.close()

if len(sol) > 0 : 
    
    print('c The solution to the problem of ' , m.name , 'is ' , sol)
    print('c Visualisation: ' )
    for i in range (1,len(y)+1) : 
        print('c X[i] >= ' , len(y) -i  , '?:    ' ,  end='')
        print_solution_values(sol,y[-i])
        
    for i in x:
        print ('---',end=' ')    
        
    print('\n' + 'c X :              ' , end='')
    print_solution_values(sol,x)