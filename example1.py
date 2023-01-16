from  students_lib import *


def my_problem(outputfile): 
    m = model()
    m.name = "Hello!"

    #Define a list x of 5 variables 
    x = m.define_new_list(5) 
    #Define a list y of 16 variables 
    y = m.define_new_list(16) 

    c = encode_clause([-x[3], y[7] ,- y[2]])
    m.cls.append (c)


    c = encode_clause([x[0], - y[1] , y[2] , -y[9]])
    c = encode_implication_clause(y[3], c )
    m.cls.append (c)

    c = encode_implication(y[10], x[1])
    m.cls.append (c)

    c = always_true(x[4])
    m.cls.append(c)

    c = always_false(x[0])
    m.cls.append (c)

    c = always_false(y[0])
    m.cls.append (c)

    c = always_false(y[3])
    m.cls.append (c)

    c = always_false(y[5])
    m.cls.append (c)

    L= [ -x[0], -x[4] ]
    for i in range (len(y)): 
        if i % 2  ==0 : 
            L.append(y[i])

    #At most one of the literals in L is true! 
    encode_atmost_one(m,L)

    m.print_my_model()

    write_cnf_file(m.cls,m.vars,outputfile)

    return m,x,y

    

outputfile='./files/example1.cnf'
m,x,y = my_problem(outputfile)

sol = run_solver(outputfile)

if len(sol) > 0 : 
    
    print('c The solution to the problem of ' , m.name , 'is ' , sol)
    print('c Visualisation: ' )
    
    print('c The variables in x are: ', x )
    print('c The values associated to x in the solution are: ' )
    print_solution_values(sol,x)
    
    print('c The variables in y are: ', y )
    print('c The values associated to y in the solution are: ' )
    print_solution_values(sol,y)
else : 
    print ('c The problem in UNSATISFIABLE')
    