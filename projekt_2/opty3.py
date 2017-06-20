from sage.all_cmdline import * 

N = int(raw_input(''))

solver = MixedIntegerLinearProgram(maximization=False, solver="GLPK")
variable = solver.new_variable(integer = True, nonnegative = True)

Rw = [0] * N
Ru = [0] * N
wSon = []
uSon = []
for n in range(0, N):
    wSon.append([])
    uSon.append([])

for n in range(0, N):
    line = raw_input('')
    token = line.split(' ')
    Bw = int(token[0])
    Bu = int(token[1])
    Rw[n] = int(token[2])
    Ru[n] = int(token[3])
    if Bw != n:	
        wSon[Bw].append(n)
    if Bu != n:
        uSon[Bu].append(n)

objective = 0
for n in range(0, N):
    objective = objective + variable[n]  
solver.set_objective(objective)

def constrRec(variable, sons, no):
    c = variable[no]
    for i in range(0, len(sons[no])):
        c = c + constrRec(variable, sons, sons[no][i])
    return c

def constr(variable, sons, no, bound):
    return (constrRec(variable, sons, no) >= bound)

for n in range(0, N):
    solver.add_constraint(constr(variable, wSon, n, Rw[n]))
    solver.add_constraint(constr(variable, uSon, n, Ru[n]))

solver.set_max(variable, 1)

#solver.show()

solver.solve()

toDismiss = []
for n, value in solver.get_values(variable).iteritems():
    if value == 0.0:
        toDismiss.append(n)

print len(toDismiss)
for n in toDismiss:
    print n,