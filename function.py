from cvxopt.modeling import variable, op

import time

start = time.time()

x = variable(9, 'x')

### себестоимость транспортировки груза
price = [8,3,1,5,7,9,6,4,2]

### объемы перевозимого груза
vol=(price[0]*x[0] + price[1]*x[1] +price[2]* x[2] +price[3]*x[3] + price[4]*x[4] +price[5]* x[5]+price[6]*x[6] +price[7]*x[7] +price[8]* x[8])

### <50, 12, 56> - список одинакового груза в порту 
### <70,67,44> - спрос на груз 
m1 = (x[0] + x[1] +x[2] <= 50)
m2 = (x[3] + x[4] +x[5] <= 12)
m3 = (x[6] + x[7] + x[8] <= 56)
m4 = (x[0] + x[3] + x[6] == 70)
m5 = (x[1] +x[4] + x[7] == 67)
m6 = (x[2] + x[5] + x[8] == 44)
m7 = (x[1] == 30) # минимальный необходимых объем для транспортировки груза

x_non_negative = (x >= 0)    
problem =op(vol,[m1,m2,m3,m4 ,m5,m6, m7,x_non_negative])
problem.solve(solver='glpk')  
print("Результат: ")
for i in x.value:
         print(i)
print("Цена транспортировки: ")
print(problem.objective.value()[0])
stop = time.time()
print ("Длительность транспортировки :")
print(stop - start)
