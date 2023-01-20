from  students_lib import *

def my_problem(outputfile): 
    #Nombre de nurse
    n=7
    #Nombre de day
    m=7
        
    mdl = model()

    mdl.name = "a day a nurse - a nurse a day"

    #s = mdl.define_new_list(n) 
    #d = mdl.define_new_list(m)

    #W[i][j] == true <==>  La nurse i travaille le jour j 
    w = []
    for i in range(n):
        w.append(mdl.define_new_list(m))


    # sum(wj) pour i >= 1 : nombre de jour travaillé pour la nurse i >= 1
    for wi in w:
        mdl.addcls(encode_clause(wi))
        encode_atmost_one(mdl,wi)

    npw = np.transpose(w)
    for wj in npw:
        mdl.addcls(encode_clause(wj))
        encode_atmost_one(mdl,wj)

    write_cnf_file(mdl.cls,mdl.vars,outputfile)
    return mdl,w


outputfile='./files/modele2.cnf'
mdl,w = my_problem(outputfile)

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
    
    print('c The solution to the problem of ' , mdl.name , 'is ' , sol)
    print('c Visualisation: ' )
    # for i in range (1,len(y)+1) : 
    #     print('c X[i] >= ' , len(y) -i  , '?:    ' ,  end='')
    #     print_solution_values(sol,y[-i])
        
    # for i in x:
    #     print ('---',end=' ')    
        
    # print('\n' + 'c X :              ' , end='')
    for wi in w: 
        print_solution_values(sol,wi)