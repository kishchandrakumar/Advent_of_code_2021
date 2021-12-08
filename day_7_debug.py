import numpy as np

inp = [int(i) for i in '16,1,2,0,4,2,7,1,2,14'.split(',')]

def fuel_used_steps(steps:int):
    '''calculates how much fuel is used if increases linearly 
    with number of steps'''
    fuel_count = 0
    for i in range(1,steps+1):
        fuel_count += i
    return fuel_count

fuel_expenditures = {'fuel':np.inf, 'position': -1}
for i, position in enumerate(inp):
    total_fuel_for_pos = 0
    for j, position_2 in enumerate(inp):
        if position!=position_2:
            steps = abs(position - position_2)
            fuel_used = fuel_used_steps(steps)
            total_fuel_for_pos += fuel_used
    if fuel_expenditures['fuel'] > total_fuel_for_pos:
        fuel_expenditures['fuel'] = total_fuel_for_pos
        fuel_expenditures['position'] = position

print(fuel_expenditures)
